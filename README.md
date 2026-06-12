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

A Claude-format version of these skills also lives at
[l3ad3r1/Claude-skills-repo](https://github.com/l3ad3r1/Claude-skills-repo).

## License

[MIT](LICENSE) © 2026 l3ad3r1. Bundled upstream projects keep their own licenses.
