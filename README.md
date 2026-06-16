# Hermes Skills

Open-source skills for the **Hermes Agent**, in Hermes' `SKILL.md` format
(`skills/<category>/<skill-name>/`). Each skill carries Hermes frontmatter —
`name`, `version`, `author`, `license`, `prerequisites`, and `metadata.hermes`
tags — so it drops straight into a Hermes skills tree.

## Skills

| Category | Skill | What it does |
|---|---|---|
| `data-science` | [`markitdown-converter`](skills/data-science/markitdown-converter/) | Convert PDF / Office / HTML / CSV / JSON / XML / images / audio / EPub / ZIP into clean, structure-preserving Markdown via Microsoft MarkItDown — then optionally analyze. |
| `software-development` | [`dev-browser`](skills/software-development/dev-browser/) | Drive a real browser (navigate, click, fill, screenshot, full Playwright API) via sandboxed JavaScript, wrapping the open-source [dev-browser](https://github.com/SawyerHood/dev-browser) CLI by Sawyer Hood (MIT). |
| `software-development` | [`mcp-server-builder`](skills/software-development/mcp-server-builder/) | Build MCP servers (tools/resources/prompts) in Python (FastMCP) or Node/TS — with a working template and best practices. |
| `software-development` | [`skill-builder`](skills/software-development/skill-builder/) | Author, validate, and package Agent Skills into installable `.skill` archives — with bundled validator and packager. |
| `software-development` | [`animejs`](skills/software-development/animejs/) | Build web animations with [anime.js](https://animejs.com) v4 (DOM/CSS/SVG/timelines/stagger/scroll/draggable) by Julian Garnier (MIT). |
| `software-development` | [`clone-website`](skills/software-development/clone-website/) | Reverse-engineer and clone any website into a Next.js + shadcn/ui + Tailwind codebase via a browser MCP + parallel builder agents. Adapts [ai-website-cloner-template](https://github.com/JCodesMore/ai-website-cloner-template) by JCodesMore (MIT). |
| `productivity` | [`pdf-toolkit`](skills/productivity/pdf-toolkit/) | Merge, split, rotate, watermark, extract text/tables, and OCR PDFs — built on `pypdf`, `pdfplumber`, `OCRmyPDF`. |
| `productivity` | [`docx-toolkit`](skills/productivity/docx-toolkit/) | Create, read, and edit Word `.docx` documents — built on `python-docx`. |
| `productivity` | [`xlsx-toolkit`](skills/productivity/xlsx-toolkit/) | Create, read, and edit Excel `.xlsx` workbooks (formulas, charts) — built on `openpyxl`. |
| `productivity` | [`pptx-toolkit`](skills/productivity/pptx-toolkit/) | Create, read, and edit PowerPoint `.pptx` decks — built on `python-pptx`. |

## Install

Copy a skill folder into your Hermes skills directory, keeping the category path:

```bash
cp -r skills/data-science/markitdown-converter \
  ~/AppData/Local/hermes/hermes-agent/skills/data-science/
```

Install each skill's prerequisites (listed in its `SKILL.md`), e.g.:

```bash
pip install "markitdown[all]"
```

## Credits

Skills created by **Rinu ([l3ad3r1](https://github.com/l3ad3r1)) in collaboration
with Claude (Anthropic)**. Upstream libraries are credited inside each skill's
`SKILL.md` and `Credits` section:

- `markitdown-converter` wraps [Microsoft MarkItDown](https://github.com/microsoft/markitdown) (MIT).
- `dev-browser` wraps the [dev-browser](https://github.com/SawyerHood/dev-browser) CLI by Sawyer Hood (MIT), brought to you by [Do Browser](https://dobrowser.io).
- `pdf-toolkit` is built on [pypdf](https://github.com/py-pdf/pypdf) (BSD), [pdfplumber](https://github.com/jsvine/pdfplumber) (MIT), [OCRmyPDF](https://github.com/ocrmypdf/OCRmyPDF) (MPL-2.0).
- `docx-toolkit` / `xlsx-toolkit` / `pptx-toolkit` use [python-docx](https://github.com/python-openxml/python-docx), [openpyxl](https://foss.heptapod.net/openpyxl/openpyxl), [python-pptx](https://github.com/scanny/python-pptx) (all MIT).
- `mcp-server-builder` uses the official [MCP SDKs](https://github.com/modelcontextprotocol) (MIT); `skill-builder` is an original work based on the public Agent Skills spec.
- `animejs` wraps [anime.js](https://animejs.com) v4 by Julian Garnier (MIT).
- `clone-website` adapts [ai-website-cloner-template](https://github.com/JCodesMore/ai-website-cloner-template) by JCodesMore (MIT); the Next.js scaffold and browser tooling are not vendored.

All skills here are **original, permissively-licensed** implementations — no proprietary skill content is included or derived.

A Claude-format version of these skills also lives at
[l3ad3r1/Claude-skills-repo](https://github.com/l3ad3r1/Claude-skills-repo).

## License

[MIT](LICENSE) © 2026 l3ad3r1. Bundled upstream projects keep their own licenses.
