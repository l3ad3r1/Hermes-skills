#!/usr/bin/env python3
"""Package an Agent Skill folder into an installable `.skill` archive.

Validates the skill first (via validate_skill.py), then zips the folder so it
unpacks as `<skill-name>/...`, ready to upload to a client that accepts `.skill`
files.

Usage:
    python package_skill.py path/to/skill-folder [-o out.skill]
"""
from __future__ import annotations

import argparse
import os
import sys
import zipfile
from pathlib import Path

sys.path.insert(0, os.path.dirname(__file__))
from validate_skill import validate  # noqa: E402

EXCLUDE = {".git", "__pycache__", ".DS_Store", "node_modules"}


def package(folder: Path, out: Path) -> None:
    errs = validate(folder)
    if errs:
        print(f"Refusing to package — {folder} is invalid:")
        for e in errs:
            print(f"  - {e}")
        raise SystemExit(1)

    parent = folder.parent
    with zipfile.ZipFile(out, "w", zipfile.ZIP_DEFLATED) as z:
        for dp, dirs, files in os.walk(folder):
            dirs[:] = [d for d in dirs if d not in EXCLUDE]
            for f in files:
                if f in EXCLUDE:
                    continue
                full = Path(dp) / f
                z.write(full, full.relative_to(parent))  # rooted at <skill-name>/
    print(f"Packaged {folder.name} -> {out}")


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("folder")
    ap.add_argument("-o", "--output")
    a = ap.parse_args()
    folder = Path(a.folder)
    out = Path(a.output) if a.output else folder.parent / f"{folder.name}.skill"
    package(folder, out)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
