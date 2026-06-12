#!/usr/bin/env python3
"""Convert files of almost any format to clean Markdown via Microsoft MarkItDown.

Handles single files, multiple files, folders, and ZIP archives. When more than
one document is produced, the results are written as ONE combined Markdown file
with `# <filename>` separators and `---` rules between documents. In combined
mode, each document's own headings are demoted one level so that `#` stays
reserved for the file separators.

Usage:
    python convert.py INPUT [INPUT ...] [-o OUTPUT.md]

    python convert.py report.pdf -o report.md
    python convert.py mixed_docs.zip -o combined.md
    python convert.py ./folder a.docx b.xlsx -o combined.md

Requires: pip install "markitdown[all]"
"""

from __future__ import annotations

import argparse
import re
import sys
import tempfile
import zipfile
from pathlib import Path

try:
    from markitdown import MarkItDown
except ImportError:
    sys.exit(
        'markitdown is not installed. Run:  pip install "markitdown[all]"'
    )

# Formats MarkItDown can convert. Anything not in here is skipped in folder/zip
# walks (so we don't try to "convert" a .png icon inside a zip, etc.).
SUPPORTED_SUFFIXES = {
    ".pdf", ".docx", ".pptx", ".xlsx", ".xls", ".csv", ".tsv",
    ".html", ".htm", ".json", ".xml", ".txt", ".md", ".rst",
    ".epub", ".msg", ".jpg", ".jpeg", ".png", ".gif", ".bmp",
    ".mp3", ".wav", ".m4a", ".zip",
}

HEADING_RE = re.compile(r"^(#{1,6})(\s+)", re.MULTILINE)


def demote_headings(markdown: str) -> str:
    """Demote every ATX heading one level (max depth 6).

    Used in combined mode so `#` is reserved for file separators and document
    boundaries never collide with a document's own `# Heading`.
    """
    def _bump(match: re.Match) -> str:
        hashes = match.group(1)
        if len(hashes) < 6:
            hashes += "#"
        return hashes + match.group(2)

    return HEADING_RE.sub(_bump, markdown)


def fix_empty_table_header(markdown: str) -> str:
    """Repair the common DOCX quirk where a table renders with a blank header row.

    MarkItDown sometimes emits a table whose header cells are all empty, pushing
    the real header into the first body row, e.g.:

        |  |  |  |
        | --- | --- | --- |
        | Part | Qty | Cost |
        | Bolt | 10 | 2 |

    We promote that first body row into the header so the table reads correctly.
    """
    lines = markdown.split("\n")
    out: list[str] = []
    i = 0
    n = len(lines)

    def is_blank_header(row: str) -> bool:
        cells = [c.strip() for c in row.strip().strip("|").split("|")]
        return bool(cells) and all(c == "" for c in cells)

    def is_separator(row: str) -> bool:
        s = row.strip()
        return s.startswith("|") and bool(re.fullmatch(r"[\s|:-]+", s)) and "-" in s

    while i < n:
        line = lines[i]
        if (
            line.strip().startswith("|")
            and is_blank_header(line)
            and i + 2 < n
            and is_separator(lines[i + 1])
            and lines[i + 2].strip().startswith("|")
        ):
            # Drop the blank header, keep the separator, promote next row to header.
            out.append(lines[i + 2])   # promoted header
            out.append(lines[i + 1])   # separator
            i += 3
            continue
        out.append(line)
        i += 1

    return "\n".join(out)


def gather_inputs(paths: list[Path]) -> list[Path]:
    """Expand folders into their supported files. ZIPs are handled per-file."""
    files: list[Path] = []
    for p in paths:
        if not p.exists():
            print(f"  ! not found, skipping: {p}", file=sys.stderr)
            continue
        if p.is_dir():
            for child in sorted(p.rglob("*")):
                if child.is_file() and child.suffix.lower() in SUPPORTED_SUFFIXES:
                    files.append(child)
        else:
            files.append(p)
    return files


def convert_one(md: MarkItDown, path: Path) -> str:
    """Convert a single file to Markdown text. Raises on failure."""
    result = md.convert(str(path))
    return result.text_content or ""


def expand_zip(md: MarkItDown, zip_path: Path) -> list[tuple[str, str]]:
    """Convert each supported member of a ZIP. Returns (label, markdown) pairs."""
    out: list[tuple[str, str]] = []
    with tempfile.TemporaryDirectory() as tmp:
        with zipfile.ZipFile(zip_path) as zf:
            zf.extractall(tmp)
        for child in sorted(Path(tmp).rglob("*")):
            if child.is_file() and child.suffix.lower() in SUPPORTED_SUFFIXES:
                label = f"{zip_path.name}/{child.relative_to(tmp).as_posix()}"
                try:
                    out.append((label, convert_one(md, child)))
                except Exception as exc:  # noqa: BLE001 - keep going on batch
                    print(f"  ! failed: {label}: {exc}", file=sys.stderr)
    return out


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("inputs", nargs="+", help="files, folders, or .zip archives")
    ap.add_argument("-o", "--output", help="output .md path (default: stdout)")
    args = ap.parse_args()

    md = MarkItDown()
    inputs = gather_inputs([Path(p) for p in args.inputs])

    # (label, markdown) for every produced document.
    docs: list[tuple[str, str]] = []
    for path in inputs:
        if path.suffix.lower() == ".zip":
            docs.extend(expand_zip(md, path))
        else:
            try:
                docs.append((path.name, convert_one(md, path)))
            except Exception as exc:  # noqa: BLE001 - keep going on batch
                print(f"  ! failed: {path}: {exc}", file=sys.stderr)

    if not docs:
        print("No files were converted.", file=sys.stderr)
        return 1

    combined = len(docs) > 1
    parts: list[str] = []
    for label, text in docs:
        text = fix_empty_table_header(text)
        if combined:
            text = demote_headings(text)
            parts.append(f"# {label}\n\n{text.strip()}\n")
        else:
            parts.append(text.strip() + "\n")

    output = ("\n\n---\n\n".join(parts)) if combined else parts[0]

    if args.output:
        Path(args.output).write_text(output, encoding="utf-8")
        print(f"Wrote {args.output} ({len(docs)} document(s)).")
    else:
        sys.stdout.write(output)

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
