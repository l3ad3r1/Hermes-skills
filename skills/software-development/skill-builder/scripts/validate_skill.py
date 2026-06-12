#!/usr/bin/env python3
"""Validate an Agent Skill folder.

Checks that a skill directory contains a well-formed SKILL.md:
  - YAML frontmatter delimited by `---`
  - required `name` and `description` fields
  - `name` is kebab-case and matches the folder name
  - a non-empty Markdown body after the frontmatter

Usage:
    python validate_skill.py path/to/skill-folder
Exit code 0 = valid, 1 = problems found.

Requires: pip install pyyaml
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

try:
    import yaml
except ImportError:
    sys.exit("pyyaml is not installed. Run:  pip install pyyaml")

KEBAB = re.compile(r"^[a-z0-9]+(-[a-z0-9]+)*$")


def validate(folder: Path) -> list[str]:
    errs: list[str] = []
    skill_md = folder / "SKILL.md"
    if not skill_md.is_file():
        return [f"missing SKILL.md in {folder}"]

    text = skill_md.read_text(encoding="utf-8")
    if not text.startswith("---"):
        return ["SKILL.md must start with a `---` YAML frontmatter block"]

    parts = text.split("---", 2)
    if len(parts) < 3:
        return ["frontmatter is not closed with a second `---`"]

    try:
        meta = yaml.safe_load(parts[1]) or {}
    except yaml.YAMLError as exc:
        return [f"frontmatter is not valid YAML: {exc}"]

    name = meta.get("name")
    if not name:
        errs.append("frontmatter missing `name`")
    else:
        if not KEBAB.match(str(name)):
            errs.append(f"`name` should be kebab-case, got: {name!r}")
        if str(name) != folder.name:
            errs.append(f"`name` ({name!r}) should match folder name ({folder.name!r})")

    desc = meta.get("description")
    if not desc:
        errs.append("frontmatter missing `description`")
    elif len(str(desc)) < 20:
        errs.append("`description` is very short — describe what it does AND when to use it")

    if not parts[2].strip():
        errs.append("SKILL.md has no body content after the frontmatter")

    return errs


def main() -> int:
    if len(sys.argv) != 2:
        sys.exit("usage: python validate_skill.py path/to/skill-folder")
    folder = Path(sys.argv[1])
    errs = validate(folder)
    if errs:
        print(f"INVALID: {folder}")
        for e in errs:
            print(f"  - {e}")
        return 1
    print(f"OK: {folder} is a valid skill")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
