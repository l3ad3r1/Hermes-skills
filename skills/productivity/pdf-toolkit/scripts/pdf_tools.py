#!/usr/bin/env python3
"""PDF toolkit — merge, split, rotate, extract text, and watermark PDFs.

Wraps the permissively licensed pypdf (BSD) and pdfplumber (MIT) libraries.

Usage:
    python pdf_tools.py merge a.pdf b.pdf c.pdf -o out.pdf
    python pdf_tools.py split in.pdf -o outdir            # one file per page
    python pdf_tools.py split in.pdf --ranges 1-3 8 10-12 -o part.pdf
    python pdf_tools.py rotate in.pdf --deg 90 -o out.pdf
    python pdf_tools.py text in.pdf [-o out.txt]          # extract text
    python pdf_tools.py watermark in.pdf --stamp mark.pdf -o out.pdf

Install:  pip install pypdf pdfplumber
"""
from __future__ import annotations

import argparse
import sys
from pathlib import Path

try:
    from pypdf import PdfReader, PdfWriter
except ImportError:
    sys.exit("pypdf is not installed. Run:  pip install pypdf")


def merge(inputs: list[str], out: str) -> None:
    writer = PdfWriter()
    for f in inputs:
        for page in PdfReader(f).pages:
            writer.add_page(page)
    with open(out, "wb") as fh:
        writer.write(fh)
    print(f"Merged {len(inputs)} file(s) -> {out}")


def _parse_ranges(spec: list[str], n: int) -> list[int]:
    """1-based, inclusive ranges -> sorted 0-based page indices."""
    pages: set[int] = set()
    for token in spec:
        if "-" in token:
            a, b = token.split("-", 1)
            for i in range(int(a), int(b) + 1):
                pages.add(i - 1)
        else:
            pages.add(int(token) - 1)
    return [p for p in sorted(pages) if 0 <= p < n]


def split(inp: str, out: str, ranges: list[str] | None) -> None:
    reader = PdfReader(inp)
    n = len(reader.pages)
    if ranges:
        writer = PdfWriter()
        for idx in _parse_ranges(ranges, n):
            writer.add_page(reader.pages[idx])
        with open(out, "wb") as fh:
            writer.write(fh)
        print(f"Wrote selected pages -> {out}")
    else:
        outdir = Path(out)
        outdir.mkdir(parents=True, exist_ok=True)
        for i, page in enumerate(reader.pages, 1):
            writer = PdfWriter()
            writer.add_page(page)
            target = outdir / f"page_{i:03d}.pdf"
            with open(target, "wb") as fh:
                writer.write(fh)
        print(f"Split {n} page(s) -> {outdir}/")


def rotate(inp: str, out: str, deg: int) -> None:
    reader = PdfReader(inp)
    writer = PdfWriter()
    for page in reader.pages:
        page.rotate(deg)
        writer.add_page(page)
    with open(out, "wb") as fh:
        writer.write(fh)
    print(f"Rotated by {deg}deg -> {out}")


def extract_text(inp: str, out: str | None) -> None:
    try:
        import pdfplumber
    except ImportError:
        sys.exit("pdfplumber is not installed. Run:  pip install pdfplumber")
    parts: list[str] = []
    with pdfplumber.open(inp) as pdf:
        for i, page in enumerate(pdf.pages, 1):
            parts.append(f"--- page {i} ---\n{page.extract_text() or ''}")
    text = "\n\n".join(parts)
    if out:
        Path(out).write_text(text, encoding="utf-8")
        print(f"Wrote text -> {out}")
    else:
        sys.stdout.write(text)


def watermark(inp: str, out: str, stamp: str) -> None:
    """Overlay every page of `inp` with the first page of `stamp`."""
    reader = PdfReader(inp)
    mark = PdfReader(stamp).pages[0]
    writer = PdfWriter()
    for page in reader.pages:
        page.merge_page(mark)
        writer.add_page(page)
    with open(out, "wb") as fh:
        writer.write(fh)
    print(f"Watermarked -> {out}")


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = ap.add_subparsers(dest="cmd", required=True)

    m = sub.add_parser("merge"); m.add_argument("inputs", nargs="+"); m.add_argument("-o", required=True)
    s = sub.add_parser("split"); s.add_argument("input"); s.add_argument("-o", required=True)
    s.add_argument("--ranges", nargs="*", help="e.g. 1-3 8 10-12 (omit to burst per page)")
    r = sub.add_parser("rotate"); r.add_argument("input"); r.add_argument("-o", required=True)
    r.add_argument("--deg", type=int, default=90, choices=[90, 180, 270])
    t = sub.add_parser("text"); t.add_argument("input"); t.add_argument("-o")
    w = sub.add_parser("watermark"); w.add_argument("input"); w.add_argument("-o", required=True)
    w.add_argument("--stamp", required=True, help="a 1-page PDF used as the overlay")

    a = ap.parse_args()
    if a.cmd == "merge":
        merge(a.inputs, a.o)
    elif a.cmd == "split":
        split(a.input, a.o, a.ranges)
    elif a.cmd == "rotate":
        rotate(a.input, a.o, a.deg)
    elif a.cmd == "text":
        extract_text(a.input, a.o)
    elif a.cmd == "watermark":
        watermark(a.input, a.o, a.stamp)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
