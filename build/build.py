"""Build every document in the kit.

    pip install python-docx openpyxl
    python build/build.py            # writes the kit into the repository root folders
    python build/build.py IMS-POL-001  # build only the listed IDs
"""
import importlib
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))

import lib  # noqa: E402
import org  # noqa: E402

ROOT = HERE.parent


def module_for(doc_id):
    name = "content." + doc_id.lower().replace("-", "_")
    return importlib.import_module(name)


def main(ids):
    built, missing = [], []
    for doc_id, _, _, _, kind in org.DOCS:
        if ids and doc_id not in ids:
            continue
        try:
            mod = module_for(doc_id)
        except ModuleNotFoundError as e:
            if e.name and e.name.startswith("content."):
                missing.append(doc_id)
                continue
            raise
        if kind == "docx":
            path = lib.build_docx(mod.DOC, ROOT)
        else:
            path = lib.build_xlsx(mod.WB, ROOT)
        built.append(path.relative_to(ROOT))
    for p in built:
        print("built", p)
    if missing:
        print("no content module yet:", ", ".join(missing))
    return 0


if __name__ == "__main__":
    sys.exit(main(set(sys.argv[1:])))
