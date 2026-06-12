---
name: pptx-toolkit
description: Create, read, and edit PowerPoint (.pptx) presentations — add slides,
  titles, bullet text, images, tables, and speaker notes, and read text out of existing
  decks. Built on the MIT-licensed python-pptx library. Use this skill whenever the
  user wants to generate a slide deck, edit an existing .pptx, extract text or notes
  from a presentation, or produce slides/a pitch deck as a PowerPoint file.
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
    - PowerPoint
    - PPTX
    - python-pptx
    - Slides
    - Decks
    related_skills: []
prerequisites:
  commands:
  - python
  python:
  - python-pptx
---

# PPTX Toolkit

Create and edit PowerPoint decks with [`python-pptx`](https://github.com/scanny/python-pptx)
(MIT licensed).

## When to Use

- Generate a `.pptx` deck or pitch presentation from content.
- Edit an existing presentation (add slides, text, images, tables, notes).
- Extract text or speaker notes from a `.pptx`.

> To convert a deck *to Markdown* for analysis, use `markitdown-converter`.
> Use this skill to author or edit `.pptx` files.

## Setup

```bash
pip install python-pptx
```

## Create a deck

```python
from pptx import Presentation
from pptx.util import Inches, Pt

prs = Presentation()

# Title slide (layout 0)
slide = prs.slides.add_slide(prs.slide_layouts[0])
slide.shapes.title.text = "Q2 Review"
slide.placeholders[1].text = "Prepared by the team"

# Title + content (layout 1) with bullets
slide = prs.slides.add_slide(prs.slide_layouts[1])
slide.shapes.title.text = "Highlights"
body = slide.placeholders[1].text_frame
body.text = "Revenue up 15%"
for line in ["Email Course led growth", "Workflow Kit steady"]:
    p = body.add_paragraph()
    p.text = line
    p.level = 1

# Blank slide (layout 6) with an image + speaker notes
slide = prs.slides.add_slide(prs.slide_layouts[6])
slide.shapes.add_picture("chart.png", Inches(1), Inches(1), width=Inches(8))
slide.notes_slide.notes_text_frame.text = "Walk through the chart for 30s."

prs.save("review.pptx")
```

## Read / extract

```python
from pptx import Presentation
prs = Presentation("review.pptx")
for i, slide in enumerate(prs.slides, 1):
    for shape in slide.shapes:
        if shape.has_text_frame:
            print(i, shape.text_frame.text)
    if slide.has_notes_slide:
        print("notes:", slide.notes_slide.notes_text_frame.text)
```

## Notes & Limits

- Available layouts depend on the template (`prs.slide_layouts`); indices 0/1/6
  are typical for title / title+content / blank in the default template.
- `python-pptx` does not render slides to images/PDF — use LibreOffice/PowerPoint
  for that.

## Credits

Original skill by Rinu (l3ad3r1) in collaboration with Claude (Anthropic).
Powered by [python-pptx](https://github.com/scanny/python-pptx) (MIT) — all
credit for the underlying capability belongs to its authors.
