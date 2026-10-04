"""Consistency checks for the generated kit.

    python build/check.py

Opens every generated file, counts words, and flags:
- references to document IDs that are not in org.DOCS
- references to risk / incident / NC / CA / audit IDs that are never defined anywhere
- leftover words from the earlier sample (mental wellness, clinic...) or the old framework name
"""
import re
import sys
import zipfile
from collections import defaultdict
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import lib  # noqa: E402
import org  # noqa: E402

ROOT = HERE.parent
BANNED = re.compile(r"mental[- ]wellness|clinic(?!al trial)|therapist|patient|Fawzooz AI\b|HELIX|Serene|MoodSense|ClinAssist",
                    re.I)
DOC_ID = re.compile(r"\bIMS-[A-Z]{3}-\d{3}\b")
REC_ID = re.compile(r"\b(?:RSK-(?:IS|AI)-\d{3}|INC-\d{4}-\d{3}|NC-\d{4}-\d{3}|CA-\d{4}-\d{3}|AUD-\d{4}-\d{2}|"
                    r"OBJ-\d{2}|AST-\d{3}|AI-SYS-\d{3}|AIIA-\d{4}-\d{2}|OFI-\d{4}-\d{2})\b")


def text_of(path: Path) -> str:
    with zipfile.ZipFile(path) as z:
        parts = [n for n in z.namelist() if n.endswith(".xml") and (
            n.startswith("word/") or n.startswith("xl/worksheets/") or n == "xl/sharedStrings.xml")]
        raw = " ".join(z.read(n).decode("utf8", "ignore") for n in parts)
    return re.sub(r"<[^>]+>", " ", raw)


def main():
    problems = 0
    texts = {}
    for doc_id, title, _, _, kind in org.DOCS:
        p = lib.out_path(ROOT, doc_id)
        if not p.exists():
            print(f"MISSING  {doc_id} {title}")
            problems += 1
            continue
        texts[doc_id] = text_of(p)
    all_text = " ".join(texts.values())
    # IDs defined somewhere: anything in org's shared records counts as defined, plus any ID used at least twice
    counts = defaultdict(int)
    for t in texts.values():
        for m in set(REC_ID.findall(t)):
            counts[m] += 1
    defined_in_org = set(REC_ID.findall(open(HERE / "org.py").read()))
    for doc_id, t in texts.items():
        words = len(t.split())
        bad_docs = sorted(set(DOC_ID.findall(t)) - set(org.DOC_INDEX))
        banned = sorted(set(m.group(0) for m in BANNED.finditer(t)))
        orphans = sorted(i for i in set(REC_ID.findall(t)) if counts[i] == 1 and i not in defined_in_org)
        flag = []
        if bad_docs:
            flag.append(f"unknown doc refs {bad_docs}")
        if banned:
            flag.append(f"leftover terms {banned}")
        print(f"{'OK  ' if not flag else 'WARN'}  {doc_id}  {words:>6} words  " + "; ".join(flag))
        if orphans:
            print(f"        IDs used only in this file (check they are defined here): {', '.join(orphans[:12])}"
                  + (" ..." if len(orphans) > 12 else ""))
        problems += bool(flag)
    print(f"\nTotal words: {len(all_text.split()):,}. Files with problems: {problems}.")
    return 1 if problems else 0


if __name__ == "__main__":
    sys.exit(main())
