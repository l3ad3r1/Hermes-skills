---
name: docx-toolkit
description: Create, read, and edit Microsoft Word (.docx) documents — add headings,
  paragraphs, styled runs, tables, images, page breaks, and read existing documents'
  text and tables. Built on the MIT-licensed python-docx library. Use this skill whenever
  the user wants to generate a Word document, edit an existing .docx, extract text
  or tables from a Word file, or produce a formatted report/letter/memo as .docx. For converting a Word file to Markdown or handling batches of mixed file types, use markitdown-converter instead.
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
    - Word
    - DOCX
    - python-docx
    - Documents
    - Reports
    related_skills: []
prerequisites:
  commands:
  - python
  python:
  - python-docx
---

# DOCX Toolkit

Create and edit Word documents with [`python-docx`](https://github.com/python-openxml/python-docx)
(MIT licensed).

## When to Use

- Generate a `.docx` report, letter, memo, or template.
- Edit an existing Word document (add/replace content, tables, images).
- Extract text or tables from a `.docx`.

> To convert a `.docx` *to Markdown* for analysis, use `markitdown-converter`.
> Use this skill to author or edit Word files.

## Setup

```bash
pip install python-docx
```

## Create a document

```python
from docx import Document
from docx.shared import Pt, Inches

doc = Document()
doc.add_heading("Quarterly Report", level=0)          # title
doc.add_heading("Summary", level=1)
p = doc.add_paragraph("Revenue grew ")
p.add_run("15%").bold = True
p.add_run(" quarter over quarter.")

# table
table = doc.add_table(rows=1, cols=3)
table.style = "Light Grid Accent 1"
hdr = table.rows[0].cells
hdr[0].text, hdr[1].text, hdr[2].text = "Product", "Q1", "Q2"
for name, q1, q2 in [("Email Course", "19", "34"), ("Workflow Kit", "40", "53")]:
    cells = table.add_row().cells
    cells[0].text, cells[1].text, cells[2].text = name, q1, q2

doc.add_picture("chart.png", width=Inches(5))         # optional
doc.add_page_break()
doc.save("report.docx")
```

## Read / extract

```python
from docx import Document
doc = Document("report.docx")
text = "\n".join(p.text for p in doc.paragraphs)
for table in doc.tables:
    for row in table.rows:
        print([c.text for c in row.cells])
```

## Edit an existing document

Open it, mutate paragraphs/runs/tables, and `save()` (to a new path to keep the
original). For find-and-replace, iterate `doc.paragraphs` and each
`paragraph.runs`, replacing `run.text`.

## Notes & Limits

- `python-docx` does not render to PDF; use LibreOffice/Word for conversion.
- Editing complex tracked-changes or footnote structures is limited.

## Credits

Original skill by Rinu (l3ad3r1) in collaboration with Claude (Anthropic).
Powered by [python-docx](https://github.com/python-openxml/python-docx) (MIT) —
all credit for the underlying capability belongs to its authors.
