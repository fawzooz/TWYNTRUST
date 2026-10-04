"""Renderers that turn content modules (build/content/*.py) into .docx and .xlsx files.

Content modules are plain Python data, so the wording of the kit can be edited
without touching any formatting code.

DOCX module  ->  DOC = {"id", "summary", "clauses": {"27001": str, "42001": str},
                        "howto": [str], "body": [block, ...]}
XLSX module  ->  WB  = {"id", "summary", "clauses": {...}, "howto": [str], "sheets": [sheet, ...]}

Body blocks (tuples):
  ("h1", text) ("h2", text) ("h3", text)
  ("p", text)                      inline **bold** and [[fill-in placeholder]] supported
  ("bullets", [text, ...])         ("steps", [text, ...])  numbered list
  ("table", headers, rows)         optional 4th item: list of column widths in cm
  ("tip", text)                    "Starter tip" box for first-time implementers
  ("example", title, text|[text])  "Worked example" box
  ("std", text)                    "What the standards expect" box (our own words, not ISO text)
  ("pagebreak",)

Sheet dict:
  name, title, intro, headers, rows, widths (chars per column), optional:
  lists: {header: [allowed values]}  -> drop-down validation for 500 rows
  levels: [header, ...]              -> colour Low/Medium/High/Critical cells
  status: [header, ...]              -> colour status words
  In a cell, the token {r} is replaced by the row number (for formulas).
"""
import re
from pathlib import Path

from docx import Document
from docx.enum.section import WD_ORIENT
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.enum.text import WD_ALIGN_PARAGRAPH, WD_BREAK, WD_COLOR_INDEX
from docx.oxml import OxmlElement
from docx.oxml.ns import qn
from docx.shared import Cm, Pt, RGBColor
from openpyxl import Workbook
from openpyxl.formatting.rule import CellIsRule, FormulaRule
from openpyxl.styles import Alignment, Border, Font, PatternFill, Side
from openpyxl.utils import get_column_letter
from openpyxl.worksheet.datavalidation import DataValidation

import org

NAVY = RGBColor(0x14, 0x2B, 0x4C)
TEAL = RGBColor(0x0F, 0x76, 0x6E)
GREY = RGBColor(0x59, 0x59, 0x59)
HEX_NAVY, HEX_TEAL = "142B4C", "0F766E"
BOX = {"tip": ("E8F1FB", "Starter tip"), "example": ("E9F6EF", "Worked example"),
       "std": ("FFF6E0", "What the standards expect")}
LEVEL_FILL = {"Low": "C6EFCE", "Medium": "FFEB9C", "High": "F8CBAD", "Critical": "FF7C80"}
STATUS_FILL = {"Implemented": "C6EFCE", "Done": "C6EFCE", "Closed": "C6EFCE", "Yes": "C6EFCE", "Met": "C6EFCE",
               "Partially implemented": "FFEB9C", "Partial": "FFEB9C", "Done late": "FFEB9C", "In progress": "FFEB9C", "Open": "FFEB9C",
               "On track": "FFEB9C",
               "Planned": "DDEBF7", "Not started": "F2F2F2",
               "Not implemented": "F8CBAD", "No": "F8CBAD", "Overdue": "F8CBAD", "Not met": "F8CBAD",
               "Excluded": "D9D9D9"}

INLINE = re.compile(r"(\*\*.+?\*\*|\[\[.+?\]\])")


def safe_name(text: str) -> str:
    text = text.replace("—", "-").replace("/", "-").replace(":", "-")
    return re.sub(r"[^A-Za-z0-9 ()+,.&'-]", "", text).strip()


def out_path(root: Path, doc_id: str) -> Path:
    _, title, _, folder, kind = org.DOC_INDEX[doc_id]
    return root / folder / f"{doc_id} {safe_name(title)}.{kind}"


# ---------------------------------------------------------------------------
# DOCX
# ---------------------------------------------------------------------------
def _shade(cell, hex_fill):
    tcPr = cell._tc.get_or_add_tcPr()
    shd = OxmlElement("w:shd")
    shd.set(qn("w:val"), "clear")
    shd.set(qn("w:color"), "auto")
    shd.set(qn("w:fill"), hex_fill)
    tcPr.append(shd)


def _cell_margins(table, cm=0.15):
    tblPr = table._tbl.tblPr
    mar = OxmlElement("w:tblCellMar")
    for side in ("top", "bottom", "left", "right"):
        el = OxmlElement(f"w:{side}")
        el.set(qn("w:w"), str(int(cm * 567)))
        el.set(qn("w:type"), "dxa")
        mar.append(el)
    tblPr.append(mar)


def _repeat_header(row):
    trPr = row._tr.get_or_add_trPr()
    el = OxmlElement("w:tblHeader")
    el.set(qn("w:val"), "true")
    trPr.append(el)


def _field(paragraph, code):
    run = paragraph.add_run()
    for tag, text in (("begin", None), (None, code), ("separate", None), (None, "1"), ("end", None)):
        if tag:
            el = OxmlElement("w:fldChar")
            el.set(qn("w:fldCharType"), tag)
            run._r.append(el)
        elif text == code:
            el = OxmlElement("w:instrText")
            el.set(qn("xml:space"), "preserve")
            el.text = f" {code} "
            run._r.append(el)
        else:
            t = OxmlElement("w:t")
            t.text = text
            run._r.append(t)
    return run


def add_rich(paragraph, text, size=None, color=None, bold=False):
    for part in INLINE.split(text):
        if not part:
            continue
        if part.startswith("**") and part.endswith("**"):
            run = paragraph.add_run(part[2:-2])
            run.bold = True
        elif part.startswith("[[") and part.endswith("]]"):
            run = paragraph.add_run("[" + part[2:-2] + "]")
            run.font.highlight_color = WD_COLOR_INDEX.YELLOW
        else:
            run = paragraph.add_run(part)
            run.bold = bold or None
        if size:
            run.font.size = Pt(size)
        if color:
            run.font.color.rgb = color
    return paragraph


def _setup_styles(doc):
    st = doc.styles
    normal = st["Normal"]
    normal.font.name = "Calibri"
    normal.element.rPr.rFonts.set(qn("w:eastAsia"), "Calibri")
    normal.font.size = Pt(10.5)
    normal.paragraph_format.space_after = Pt(6)
    normal.paragraph_format.line_spacing = 1.12
    for name, size, color, before in (("Heading 1", 16, NAVY, 18), ("Heading 2", 13, TEAL, 12),
                                      ("Heading 3", 11.5, NAVY, 10), ("Title", 26, NAVY, 0)):
        s = st[name]
        s.font.name = "Calibri"
        rfonts = s.element.rPr.find(qn("w:rFonts"))
        if rfonts is not None:
            for a in ("w:asciiTheme", "w:hAnsiTheme", "w:eastAsiaTheme", "w:cstheme"):
                rfonts.attrib.pop(qn(a), None)
            rfonts.set(qn("w:ascii"), "Calibri")
            rfonts.set(qn("w:hAnsi"), "Calibri")
        s.font.size = Pt(size)
        s.font.bold = True
        s.font.color.rgb = color
        s.paragraph_format.space_before = Pt(before)
        s.paragraph_format.space_after = Pt(6)
        s.paragraph_format.keep_with_next = True


def _table(doc, headers, rows, widths=None, header_fill=HEX_NAVY):
    t = doc.add_table(rows=1, cols=len(headers))
    t.style = "Table Grid"
    t.alignment = WD_TABLE_ALIGNMENT.CENTER
    _cell_margins(t)
    for i, h in enumerate(headers):
        c = t.rows[0].cells[i]
        c.text = ""
        add_rich(c.paragraphs[0], str(h), size=9.5, color=RGBColor(0xFF, 0xFF, 0xFF), bold=True)
        _shade(c, header_fill)
    _repeat_header(t.rows[0])
    for r_i, row in enumerate(rows):
        cells = t.add_row().cells
        for i, val in enumerate(row):
            cells[i].text = ""
            lines = str(val).split("\n")
            add_rich(cells[i].paragraphs[0], lines[0], size=9.5)
            for extra in lines[1:]:
                add_rich(cells[i].add_paragraph(), extra, size=9.5)
            for p in cells[i].paragraphs:
                p.paragraph_format.space_after = Pt(2)
            if r_i % 2 == 1:
                _shade(cells[i], "F5F7FA")
    if widths:
        for row in t.rows:
            for i, w in enumerate(widths):
                row.cells[i].width = Cm(w)
    doc.add_paragraph()
    return t


def _box(doc, kind, body, title=None):
    fill, label = BOX[kind]
    t = doc.add_table(rows=1, cols=1)
    t.alignment = WD_TABLE_ALIGNMENT.CENTER
    _cell_margins(t, 0.25)
    c = t.rows[0].cells[0]
    _shade(c, fill)
    p = c.paragraphs[0]
    add_rich(p, label + (f" — {title}" if title else ""), size=10, color=NAVY, bold=True)
    items = body if isinstance(body, list) else [body]
    for item in items:
        q = c.add_paragraph()
        add_rich(q, ("•  " if isinstance(body, list) else "") + item, size=10)
        q.paragraph_format.space_after = Pt(3)
    doc.add_paragraph()


def _header_footer(doc, doc_id, title):
    sec = doc.sections[0]
    hp = sec.header.paragraphs[0]
    add_rich(hp, f"{org.ORG['name']}  ·  {org.FRAMEWORK} Integrated Management System", size=8.5, color=GREY)
    hp.add_run("\t\t")
    add_rich(hp, doc_id, size=8.5, color=GREY, bold=True)
    fp = sec.footer.paragraphs[0]
    add_rich(fp, f"{doc_id} · v{org.KIT_VERSION} · Classification: {org.CLASSIFICATION} · "
                 f"Uncontrolled when printed · Page ", size=8, color=GREY)
    _field(fp, "PAGE").font.size = Pt(8)
    add_rich(fp, " of ", size=8, color=GREY)
    _field(fp, "NUMPAGES").font.size = Pt(8)


def _front_matter(doc, spec):
    doc_id = spec["id"]
    _, title, owner, folder, _ = org.DOC_INDEX[doc_id]
    p = doc.add_paragraph()
    add_rich(p, f"{org.FRAMEWORK} FRAMEWORK  ·  {org.ORG['name'].upper()}", size=10, color=TEAL, bold=True)
    doc.add_paragraph(title, style="Title")
    if spec.get("summary"):
        add_rich(doc.add_paragraph(), spec["summary"], size=11.5, color=GREY)
    clauses = spec.get("clauses", {})
    rows = [
        ("Document ID", doc_id), ("Version", org.KIT_VERSION), ("Prepared by", org.AUTHOR_FULL), ("License", org.LICENSE),
        ("Status", "Approved — SAMPLE for adaptation"),
        ("Classification", org.CLASSIFICATION),
        ("Document owner", org.who(owner)),
        ("Approved by", f"{org.who('CEO')}, on behalf of the Trust Council"),
        ("Effective date", org.EFFECTIVE_DATE), ("Next review", org.NEXT_REVIEW + " or after a significant change"),
        (f"{org.FRAMEWORK} strand / kit folder", folder),
        ("ISO/IEC 27001:2022", clauses.get("27001", "—")),
        ("ISO/IEC 42001:2023", clauses.get("42001", "—")),
    ]
    t = doc.add_table(rows=0, cols=2)
    t.style = "Table Grid"
    _cell_margins(t)
    for k, v in rows:
        cells = t.add_row().cells
        cells[0].text = ""
        add_rich(cells[0].paragraphs[0], k, size=9.5, bold=True)
        _shade(cells[0], "EEF2F7")
        cells[1].text = ""
        add_rich(cells[1].paragraphs[0], v, size=9.5)
        cells[0].width, cells[1].width = Cm(5), Cm(11.5)
    doc.add_paragraph()
    doc.add_heading("Revision history", level=3)
    _table(doc, ["Version", "Date", "Author", "Change"], [
        ("1.0", "2025-05-19", org.AUTHOR, "First release under the earlier TRACE framework (AIMS only)."),
        (org.KIT_VERSION, org.EFFECTIVE_DATE, org.AUTHOR,
         f"Rebuilt as an integrated ISMS + AIMS document under the {org.FRAMEWORK} framework."),
    ], widths=[2, 2.5, 3.5, 8.5])
    _box(doc, "tip", [
        "This is a **sample**. Text is written for the example company " + org.ORG["name"] +
        ". Replace names, systems and numbers with your own before approval.",
        "Yellow [[highlighted brackets]] mark values you must fill in or confirm.",
        "Green 'Worked example' boxes show what a good answer looks like. Blue boxes like this one "
        "are guidance for you — delete them in your final version.",
    ] + spec.get("howto", []), title="How to use this document")
    doc.add_page_break()


def build_docx(spec, root: Path) -> Path:
    doc = Document()
    sec = doc.sections[0]
    sec.page_height, sec.page_width = Cm(29.7), Cm(21.0)
    sec.left_margin = sec.right_margin = Cm(2.2)
    sec.top_margin, sec.bottom_margin = Cm(2.2), Cm(2.0)
    _setup_styles(doc)
    _header_footer(doc, spec["id"], org.DOC_INDEX[spec["id"]][1])
    _front_matter(doc, spec)
    for block in spec["body"]:
        kind = block[0]
        if kind in ("h1", "h2", "h3"):
            doc.add_heading(block[1], level=int(kind[1]))
        elif kind == "p":
            add_rich(doc.add_paragraph(), block[1])
        elif kind in ("bullets", "steps"):
            style = "List Bullet" if kind == "bullets" else "List Number"
            for item in block[1]:
                p = doc.add_paragraph(style=style)
                add_rich(p, item)
                p.paragraph_format.space_after = Pt(3)
            if kind == "steps":
                _restart_numbering(doc, block[1])
        elif kind == "table":
            _table(doc, block[1], block[2], block[3] if len(block) > 3 else None)
        elif kind == "tip":
            _box(doc, "tip", block[1])
        elif kind == "std":
            _box(doc, "std", block[1])
        elif kind == "example":
            _box(doc, "example", block[2], title=block[1])
        elif kind == "pagebreak":
            doc.add_page_break()
        else:
            raise ValueError(f"{spec['id']}: unknown block {kind!r}")
    path = out_path(root, spec["id"])
    path.parent.mkdir(parents=True, exist_ok=True)
    doc.core_properties.title = org.DOC_INDEX[spec["id"]][1]
    doc.core_properties.author = org.AUTHOR
    doc.core_properties.last_modified_by = org.AUTHOR
    doc.core_properties.subject = org.FRAMEWORK_FULL
    doc.save(path)
    return path


_num_counter = [0]


def _restart_numbering(doc, items):
    """Make each numbered list start at 1 by giving it its own w:num."""
    numbering = doc.part.numbering_part.numbering_definitions._numbering
    style_num = doc.styles["List Number"].element.pPr.numPr.numId.val
    abstract = None
    for num in numbering.findall(qn("w:num")):
        if num.get(qn("w:numId")) == str(style_num):
            abstract = num.find(qn("w:abstractNumId")).get(qn("w:val"))
    _num_counter[0] += 1
    new_id = 1000 + _num_counter[0]
    num = OxmlElement("w:num")
    num.set(qn("w:numId"), str(new_id))
    an = OxmlElement("w:abstractNumId")
    an.set(qn("w:val"), abstract)
    num.append(an)
    ov = OxmlElement("w:lvlOverride")
    ov.set(qn("w:ilvl"), "0")
    so = OxmlElement("w:startOverride")
    so.set(qn("w:val"), "1")
    ov.append(so)
    num.append(ov)
    numbering.append(num)
    paras = doc.paragraphs[-len(items):]
    for p in paras:
        pPr = p._p.get_or_add_pPr()
        numPr = OxmlElement("w:numPr")
        il = OxmlElement("w:ilvl")
        il.set(qn("w:val"), "0")
        ni = OxmlElement("w:numId")
        ni.set(qn("w:val"), str(new_id))
        numPr.append(il)
        numPr.append(ni)
        pPr.append(numPr)


# ---------------------------------------------------------------------------
# XLSX
# ---------------------------------------------------------------------------
THIN = Side(style="thin", color="BFC7D5")
BORDER = Border(left=THIN, right=THIN, top=THIN, bottom=THIN)
HEAD_FILL = PatternFill("solid", fgColor=HEX_NAVY)
WRAP = Alignment(wrap_text=True, vertical="top")
HEADER_ROW = 4


def _about_sheet(wb, spec):
    ws = wb.active
    ws.title = "About"
    _, title, owner, folder, _ = org.DOC_INDEX[spec["id"]]
    ws["A1"] = f"{org.FRAMEWORK} FRAMEWORK · {org.ORG['name']}"
    ws["A1"].font = Font(bold=True, color=HEX_TEAL, size=10)
    ws["A2"] = title
    ws["A2"].font = Font(bold=True, color=HEX_NAVY, size=18)
    ws["A3"] = spec.get("summary", "")
    ws["A3"].alignment = WRAP
    ws.merge_cells("A3:B3")
    ws.row_dimensions[3].height = 48
    clauses = spec.get("clauses", {})
    rows = [("Document ID", spec["id"]), ("Version", org.KIT_VERSION), ("Prepared by", org.AUTHOR_FULL), ("License", org.LICENSE), ("Classification", org.CLASSIFICATION),
            ("Owner", org.who(owner)),
            ("Approved by", f"{org.who('CEO')} (Trust Council)"),
            ("Effective date", org.EFFECTIVE_DATE), ("Kit folder", folder),
            ("ISO/IEC 27001:2022", clauses.get("27001", "—")), ("ISO/IEC 42001:2023", clauses.get("42001", "—"))]
    r = 5
    for k, v in rows:
        ws.cell(r, 1, k).font = Font(bold=True)
        ws.cell(r, 1).fill = PatternFill("solid", fgColor="EEF2F7")
        ws.cell(r, 2, v).alignment = WRAP
        for c in (1, 2):
            ws.cell(r, c).border = BORDER
        r += 1
    r += 1
    ws.cell(r, 1, "How to use this workbook").font = Font(bold=True, color=HEX_NAVY, size=12)
    r += 1
    howto = ["This is a SAMPLE filled in for the example company " + org.ORG["name"] +
             ". Keep the structure, replace the example rows with your own.",
             "Yellow cells are fill-in fields. Drop-down cells only accept the listed values.",
             "Cells with formulas (scores, levels, due status) calculate automatically — do not type over them."
             ] + spec.get("howto", [])
    for line in howto:
        ws.cell(r, 1, "•")
        ws.cell(r, 2, line).alignment = WRAP
        ws.row_dimensions[r].height = max(15, 15 * (len(line) // 95 + 1))
        r += 1
    r += 1
    ws.cell(r, 1, "Sheets").font = Font(bold=True, color=HEX_NAVY, size=12)
    r += 1
    for sh in spec["sheets"]:
        ws.cell(r, 1, sh["name"]).font = Font(bold=True)
        ws.cell(r, 2, sh.get("intro", "")).alignment = WRAP
        ws.row_dimensions[r].height = max(15, 15 * (len(sh.get("intro", "")) // 95 + 1))
        r += 1
    ws.column_dimensions["A"].width = 24
    ws.column_dimensions["B"].width = 100
    ws.sheet_view.showGridLines = False


def build_xlsx(spec, root: Path) -> Path:
    wb = Workbook()
    _about_sheet(wb, spec)
    for sh in spec["sheets"]:
        ws = wb.create_sheet(sh["name"][:31])
        headers = sh["headers"]
        ncol = len(headers)
        last = get_column_letter(ncol)
        ws["A1"] = sh.get("title", sh["name"])
        ws["A1"].font = Font(bold=True, color=HEX_NAVY, size=14)
        ws["A2"] = sh.get("intro", "")
        ws["A2"].alignment = WRAP
        ws.merge_cells(f"A2:{last}2")
        ws.row_dimensions[2].height = max(30, 15 * (len(sh.get("intro", "")) // 150 + 1))
        for i, h in enumerate(headers, 1):
            c = ws.cell(HEADER_ROW, i, h)
            c.font = Font(bold=True, color="FFFFFF")
            c.fill = HEAD_FILL
            c.alignment = Alignment(wrap_text=True, vertical="center")
            c.border = BORDER
        ws.row_dimensions[HEADER_ROW].height = 32
        rows = sh["rows"]
        for r_off, row in enumerate(rows):
            r = HEADER_ROW + 1 + r_off
            for i, val in enumerate(row, 1):
                if isinstance(val, str) and "{r}" in val:
                    val = val.replace("{r}", str(r))
                c = ws.cell(r, i, val)
                c.alignment = WRAP
                c.border = BORDER
                if isinstance(val, str) and val.startswith("[[") and val.endswith("]]"):
                    c.value = "[" + val[2:-2] + "]"
                    c.fill = PatternFill("solid", fgColor="FFF2CC")
                elif sh.get("section_rows") and isinstance(row[0], str) and row[0] and all(v in ("", None) for v in row[1:]):
                    c.font = Font(bold=True, color=HEX_NAVY)
                    c.fill = PatternFill("solid", fgColor="E2E8F0")
        first, end = HEADER_ROW + 1, HEADER_ROW + max(len(rows), 1) + sh.get("blank_rows", 30)
        # empty styled rows for the user to continue
        for r in range(HEADER_ROW + 1 + len(rows), end + 1):
            for i in range(1, ncol + 1):
                c = ws.cell(r, i)
                c.border = BORDER
                c.alignment = WRAP
                tmpl = sh.get("formulas", {}).get(headers[i - 1])
                if tmpl:
                    c.value = tmpl.replace("{r}", str(r))
        for name, opts in sh.get("lists", {}).items():
            col = get_column_letter(headers.index(name) + 1)
            joined = ",".join(opts)
            assert len(joined) <= 255, f"{spec['id']} {name}: drop-down list exceeds Excel's 255-character limit"
            dv = DataValidation(type="list", formula1='"' + joined + '"', allow_blank=True)
            dv.error, dv.errorTitle = "Pick a value from the list.", "Invalid value"
            ws.add_data_validation(dv)
            dv.add(f"{col}{first}:{col}{end}")
        rng_end = end
        for name in sh.get("levels", []):
            col = get_column_letter(headers.index(name) + 1)
            for lvl, fill in LEVEL_FILL.items():
                ws.conditional_formatting.add(
                    f"{col}{first}:{col}{rng_end}",
                    CellIsRule(operator="equal", formula=[f'"{lvl}"'], fill=PatternFill("solid", fgColor=fill)))
        for name in sh.get("status", []):
            col = get_column_letter(headers.index(name) + 1)
            for word, fill in STATUS_FILL.items():
                ws.conditional_formatting.add(
                    f"{col}{first}:{col}{rng_end}",
                    CellIsRule(operator="equal", formula=[f'"{word}"'], fill=PatternFill("solid", fgColor=fill)))
        for i, w in enumerate(sh.get("widths", []), 1):
            ws.column_dimensions[get_column_letter(i)].width = w
        ws.freeze_panes = ws.cell(HEADER_ROW + 1, sh.get("freeze_cols", 1) + 1)
        ws.auto_filter.ref = f"A{HEADER_ROW}:{last}{rng_end}"
        ws.sheet_view.zoomScale = 90
        ws.print_title_rows = f"{HEADER_ROW}:{HEADER_ROW}"
        ws.page_setup.orientation = "landscape"
        ws.page_setup.fitToWidth = 1
        ws.page_setup.fitToHeight = 0
        ws.sheet_properties.pageSetUpPr.fitToPage = True
    path = out_path(root, spec["id"])
    path.parent.mkdir(parents=True, exist_ok=True)
    wb.properties.title = org.DOC_INDEX[spec["id"]][1]
    wb.properties.creator = org.AUTHOR
    wb.properties.lastModifiedBy = org.AUTHOR
    wb.save(path)
    return path
