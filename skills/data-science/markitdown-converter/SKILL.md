---
name: markitdown-converter
description: "Convert PDF/Office/HTML/CSV/JSON/XML/images/audio/EPub/ZIP to clean Markdown via Microsoft MarkItDown; then optionally analyze."
version: 1.0.0
author: Rinu (l3ad3r1) in collaboration with Claude (Anthropic)
license: MIT
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: [Markdown, MarkItDown, Document Conversion, PDF, Office, OCR, LLM Pipeline, Text Extraction]
    related_skills: []
prerequisites:
  commands: [python]
  python: ["markitdown[all]"]
---

# MarkItDown Converter

Convert almost any document into clean, structure-preserving Markdown using
Microsoft's [MarkItDown](https://github.com/microsoft/markitdown), then either
deliver the file or analyze its contents.

## When to Use

- User wants a PDF / Word / Excel / PowerPoint / HTML / CSV file as Markdown.
- User wants a folder or ZIP of mixed files turned into one Markdown file.
- User uploads a format you can't read natively and wants its text.
- User asks a question *about* a non-text file — convert quietly, then answer.

## Prerequisites

```bash
pip install "markitdown[all]"
```

## Usage

The bundled script handles single files, multiple files, folders, and ZIPs, and
keeps going if one file in a batch fails.

```bash
# single file -> single .md
python scripts/convert.py report.pdf -o report.md

# folder or ZIP of mixed files -> ONE combined .md
python scripts/convert.py mixed_docs.zip -o combined.md
python scripts/convert.py ./docs -o combined.md
```

## Two Modes

1. **Convert-and-deliver** — user wants the `.md`. Convert, hand it over, stop.
2. **Convert-then-analyze** — user asks a question about a file. Convert quietly
   to a temp path, read the Markdown yourself, answer. Don't dump a file.

## Combined Output Rules

When more than one document is produced:
- Each document gets a `# <filename>` header; documents split by `---`.
- Content headings are **demoted one level** so `#` stays reserved for the file
  separators (no heading collisions).
- The common DOCX empty-header-row table quirk is auto-repaired.

## Known Limits

- Scanned/image-only PDFs may come out empty (text-layer extraction, not OCR).
- Plain PDFs carry no heading metadata — titles convert to plain text.
- Audio transcription and YouTube URLs need network access.

## Credits

Conversion powered by [Microsoft MarkItDown](https://github.com/microsoft/markitdown)
(MIT). Skill by Rinu (l3ad3r1) with Claude (Anthropic). Also published at
https://github.com/l3ad3r1/Claude-skills-repo
