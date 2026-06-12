---
name: pdf-toolkit
description: Read, extract, and manipulate PDF files — extract text and tables, merge
  multiple PDFs, split or extract page ranges, rotate pages, add watermarks, and OCR
  scanned PDFs. Built on the permissively licensed pypdf, pdfplumber, and OCRmyPDF
  libraries. Use this skill whenever the user wants to read a PDF's contents, combine
  or split PDFs, rotate or watermark pages, pull tables out of a PDF, or make a scanned
  PDF searchable.
version: 1.0.0
author: Rinu (l3ad3r1) in collaboration with Claude (Anthropic)
license: MIT
platforms:
- linux
- macos
- windows
metadata:
  hermes:
    tags:
    - PDF
    - Merge
    - Split
    - OCR
    - pypdf
    - pdfplumber
    - Documents
    related_skills: []
prerequisites:
  commands:
  - python
  python:
  - pypdf
  - pdfplumber
  - ocrmypdf
---

# PDF Toolkit

Manipulate and read PDF files using open-source Python libraries:
[`pypdf`](https://github.com/py-pdf/pypdf) (BSD) for page operations,
[`pdfplumber`](https://github.com/jsvine/pdfplumber) (MIT) for text/table
extraction, and [`OCRmyPDF`](https://github.com/ocrmypdf/OCRmyPDF) (MPL-2.0)
for OCR.

## When to Use

- Extract text or tables from a PDF.
- Merge several PDFs into one, or split / extract page ranges.
- Rotate pages or add a watermark/stamp.
- OCR a scanned (image-only) PDF to make it searchable.

> For *converting* a PDF to clean Markdown for analysis, prefer the
> `markitdown-converter` skill. Use this skill for structural PDF operations.

## Setup

```bash
pip install pypdf pdfplumber
# OCR (optional) also needs the system tools:
pip install ocrmypdf            # plus Tesseract + Ghostscript installed
```

## How to Use

A bundled CLI (`scripts/pdf_tools.py`) covers the common operations:

```bash
# merge
python scripts/pdf_tools.py merge a.pdf b.pdf c.pdf -o combined.pdf

# split into one file per page, OR extract specific ranges
python scripts/pdf_tools.py split in.pdf -o pages_dir/
python scripts/pdf_tools.py split in.pdf --ranges 1-3 8 10-12 -o excerpt.pdf

# rotate (90/180/270)
python scripts/pdf_tools.py rotate in.pdf --deg 90 -o rotated.pdf

# extract text (stdout or -o file)
python scripts/pdf_tools.py text in.pdf -o out.txt

# watermark every page with a 1-page stamp PDF
python scripts/pdf_tools.py watermark in.pdf --stamp mark.pdf -o stamped.pdf
```

### Tables

For table extraction, use `pdfplumber` directly — it exposes per-page tables:

```python
import pdfplumber
with pdfplumber.open("report.pdf") as pdf:
    for page in pdf.pages:
        for table in page.extract_tables():
            print(table)   # list of rows
```

### OCR a scanned PDF

```bash
ocrmypdf input_scanned.pdf output_searchable.pdf
```

This adds a searchable text layer (requires Tesseract + Ghostscript installed
on the system).

## Notes & Limits

- `pypdf` handles structure (pages, rotation, merge, overlays) but does not
  re-flow or re-render content.
- `pdfplumber` reads the embedded text layer; for image-only PDFs run OCR first.
- Encrypted PDFs may need a password (`PdfReader(path).decrypt(pw)`).

## Credits

Original skill by Rinu (l3ad3r1) in collaboration with Claude (Anthropic).
Powered by [pypdf](https://github.com/py-pdf/pypdf) (BSD-3-Clause),
[pdfplumber](https://github.com/jsvine/pdfplumber) (MIT), and
[OCRmyPDF](https://github.com/ocrmypdf/OCRmyPDF) (MPL-2.0). All credit for the
underlying capabilities belongs to those projects' authors.
