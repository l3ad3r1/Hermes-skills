# Hermes Skills

Open-source skills for the **Hermes Agent**, in Hermes' `SKILL.md` format
(`skills/<category>/<skill-name>/`). Each skill carries Hermes frontmatter —
`name`, `version`, `author`, `license`, `prerequisites`, and `metadata.hermes`
tags — so it drops straight into a Hermes skills tree.

## Skills

| Category | Skill | What it does |
|---|---|---|
| `data-science` | [`markitdown-converter`](skills/data-science/markitdown-converter/) | Convert PDF / Office / HTML / CSV / JSON / XML / images / audio / EPub / ZIP into clean, structure-preserving Markdown via Microsoft MarkItDown — then optionally analyze. |
| `data-science` | [`social-media-analyzer`](skills/data-science/social-media-analyzer/) | Analyze social media campaign performance — engagement rate, CTR, ROI (CPE/CPC/CPM/ROAS), and top-performer ranking, benchmarked per platform (Instagram, Facebook, Twitter/X, LinkedIn, TikTok). Bundled Python metric/analysis scripts + sample I/O + 2026 benchmark reference. From the [Claude Skills Library](https://github.com/borghei/Claude-Skills) by Amin Borghei (MIT + Commons Clause). |
| `software-development` | [`dev-browser`](skills/software-development/dev-browser/) | Drive a real browser (navigate, click, fill, screenshot, full Playwright API) via sandboxed JavaScript, wrapping the open-source [dev-browser](https://github.com/SawyerHood/dev-browser) CLI by Sawyer Hood (MIT). |
| `software-development` | [`mcp-server-builder`](skills/software-development/mcp-server-builder/) | Build MCP servers (tools/resources/prompts) in Python (FastMCP) or Node/TS — with a working template and best practices. |
| `software-development` | [`skill-builder`](skills/software-development/skill-builder/) | Author, validate, and package Agent Skills into installable `.skill` archives — with bundled validator and packager. |
| `software-development` | [`animejs`](skills/software-development/animejs/) | Build web animations with [anime.js](https://animejs.com) v4 (DOM/CSS/SVG/timelines/stagger/scroll/draggable) by Julian Garnier (MIT). |
| `software-development` | [`clone-website`](skills/software-development/clone-website/) | Reverse-engineer and clone any website into a Next.js + shadcn/ui + Tailwind codebase via a browser MCP + parallel builder agents. Adapts [ai-website-cloner-template](https://github.com/JCodesMore/ai-website-cloner-template) by JCodesMore (MIT). |
| `software-development` | [`agent-reach`](skills/software-development/agent-reach/) | Give the agent live internet access — installs/drives the open-source [Agent Reach](https://github.com/Panniantong/agent-reach) CLI to read/search web pages, Twitter/X, YouTube, Reddit, GitHub, RSS, Bilibili, Xiaohongshu, LinkedIn, podcasts, and Exa search via one zero-API-fee tool with backend failover. By Panniantong (MIT); installed from upstream, not vendored. |
| `software-development` | [`auto-browser`](skills/software-development/auto-browser/) | Real human-in-the-loop browser automation via the open-source [auto-browser](https://github.com/LvcidPsyche/auto-browser) MCP control plane by LvcidPsyche (MIT) — Playwright controller + Chromium, auth-profile reuse, noVNC takeover. Runs as a local Docker stack; includes Windows-via-WSL2 deployment notes. |
| `software-development` | [`headroom`](skills/software-development/headroom/) | Context compression for AI agents — 60–95% fewer tokens by compressing tool outputs/logs/files/history before the model. Wraps the open-source [headroom](https://github.com/chopratejas/headroom) (`headroom-ai`) by chopratejas (Apache-2.0): MCP `headroom_compress`/`retrieve`/`stats` + optional proxy; Windows-via-WSL2 install notes. |
| `design` | [`taste-skill`](skills/design/taste-skill/) | Anti-slop frontend skill for landing pages, portfolios, and redesigns — reads the brief, sets variance/motion/density dials, and ships interfaces that don't look templated. By Leonxlnx (MIT). |
| `design` | [`soft-skill`](skills/design/soft-skill/) | Design like a high-end agency — exact fonts, spacing, shadows, card structures, and motion that make a UI feel expensive; blocks the cheap AI defaults. By Leonxlnx (MIT). |
| `design` | [`minimalist-skill`](skills/design/minimalist-skill/) | Clean editorial interfaces — warm monochrome, typographic contrast, flat bento grids, muted pastels; no gradients or heavy shadows. By Leonxlnx (MIT). |
| `design` | [`brutalist-skill`](skills/design/brutalist-skill/) | Raw mechanical interfaces — Swiss typographic print × military-terminal, rigid grids, extreme type contrast, analog degradation. By Leonxlnx (MIT). |
| `design` | [`redesign-skill`](skills/design/redesign-skill/) | Upgrade existing sites/apps to premium quality — audits the design, flags generic AI patterns, applies high-end standards without breaking functionality. By Leonxlnx (MIT). |
| `design` | [`gpt-tasteskill`](skills/design/gpt-tasteskill/) | Elite UX/UI + advanced GSAP motion — Python-randomized layouts, AIDA structure, wide editorial type, gapless bento, strict ScrollTriggers. By Leonxlnx (MIT). |
| `design` | [`image-to-code-skill`](skills/design/image-to-code-skill/) | Image-to-code for Codex — generate large section-specific design images first, analyze, then implement to match; bans lazy under-generation and card-in-card UI. By Leonxlnx (MIT). |
| `design` | [`stitch-skill`](skills/design/stitch-skill/) | Semantic design-system skill for Google Stitch — emits agent-friendly `DESIGN.md` enforcing strict typography, calibrated color, asymmetric layouts, micro-motion. By Leonxlnx (MIT). |
| `design` | [`brandkit`](skills/design/brandkit/) | Premium brand-kit image generation — brand-guideline boards, logo systems, identity decks, visual-world presentations across minimalist/luxury/dark-tech/consumer systems. By Leonxlnx (MIT). |
| `design` | [`imagegen-frontend-web`](skills/design/imagegen-frontend-web/) | Generate premium website design references — one horizontal image per section, varied composition/CTAs/hero scales, one consistent palette. Images only. By Leonxlnx (MIT). |
| `design` | [`imagegen-frontend-mobile`](skills/design/imagegen-frontend-mobile/) | Generate premium app-native mobile screen concepts/flows (iOS/Android) — clean hierarchy, multi-screen consistency, custom iconography, phone-mockup framing. Images only. By Leonxlnx (MIT). |
| `design` | [`output-skill`](skills/design/output-skill/) | Override default LLM truncation — enforce complete code generation, ban placeholders, handle token-limit splits cleanly. By Leonxlnx (MIT). |
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
- `agent-reach` documents and drives the [Agent Reach](https://github.com/Panniantong/agent-reach) CLI by Panniantong (MIT); the CLI and its backends are installed from upstream, not vendored.
- `auto-browser` documents and wires up the [auto-browser](https://github.com/LvcidPsyche/auto-browser) MCP control plane by LvcidPsyche (MIT); the stack (`docker compose`) and the `auto-browser-mcp` bridge are installed from upstream, not vendored.
- `headroom` documents and wires up [headroom](https://github.com/chopratejas/headroom) by chopratejas (Apache-2.0), distributed on PyPI as `headroom-ai`; installed from upstream, not vendored.
- The `design` category (`taste-skill`, `soft-skill`, `minimalist-skill`, `brutalist-skill`, `redesign-skill`, `gpt-tasteskill`, `image-to-code-skill`, `stitch-skill`, `brandkit`, `imagegen-frontend-web`, `imagegen-frontend-mobile`, `output-skill`) is mirrored from the [Taste Skill](https://github.com/leonxlnx/taste-skill) collection ([tasteskill.dev](https://tasteskill.dev)) by [Leonxlnx](https://github.com/leonxlnx) (MIT) — all credit for the design systems belongs to its author; content is reproduced unmodified except for a credits note.

- `social-media-analyzer` is mirrored from the [Claude Skills Library](https://github.com/borghei/Claude-Skills) by [Amin Borghei](https://github.com/borghei) (**MIT + Commons Clause**) — all credit for the metrics logic, ROI model, and platform benchmarks belongs to its author. Redistribution is permitted; the Commons Clause forbids *selling* the software (see the skill's `NOTICE.md`).

Skills outside the `design` category and `social-media-analyzer` are **original,
permissively-licensed** implementations — no proprietary skill content is
included or derived.

A Claude-format version of these skills also lives at
[l3ad3r1/Claude-skills-repo](https://github.com/l3ad3r1/Claude-skills-repo).

## License

[MIT](LICENSE) © 2026 l3ad3r1. Bundled upstream projects keep their own licenses.
