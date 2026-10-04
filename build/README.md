# Building the TWYNTRUST kit

The Word and Excel files in the kit folders are **generated**. The text and data live here, as plain Python:

| Path | What it holds |
|---|---|
| `org.py` | Everything about the sample organisation: name, people and roles, AI systems, laws, risk scales, ID formats, the master document list, and shared example records (key risks, objectives, the sample incident, audit and corrective actions). |
| `content/<id>.py` | The content of one document (`DOC` for Word, `WB` for Excel). File name = document ID in lower case, e.g. `ims_pro_001.py`. |
| `lib.py` | The renderer: cover page, document control, headers and footers, tables, guidance boxes, drop-downs, formulas, conditional colours. |
| `build.py` | Builds everything, or only the IDs you pass. |

```bash
pip install python-docx openpyxl
python build/build.py                 # whole kit
python build/build.py IMS-POL-001     # one document
```

## Make it yours

1. Edit `org.py`: company facts, people (role tags like `[CEO]` by default — swap in real names if you like), AI systems, laws, risk scales, dates.
2. Rebuild. Every document picks up the new values.
3. Search the content modules for sample-specific stories (for example the worked examples about StoryFrame) and
   rewrite them for your own systems.

## Writing rules

- Never copy text from ISO standards. Reference clause and control numbers and describe requirements in your own words.
- Import names, titles and IDs from `org.py` instead of typing them, so the kit stays consistent.
- Inline formatting: `**bold**` and `[[fill-in placeholder]]` (shown highlighted in yellow).
