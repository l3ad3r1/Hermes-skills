---
name: skill-builder
description: Create, validate, and package Agent Skills from scratch. Explains the
  SKILL.md format and frontmatter, how to write a high-signal description that triggers
  reliably, how to structure bundled scripts and reference files, and ships tools
  to validate and package a skill into an installable .skill archive. Use this skill
  whenever the user wants to author a new skill, fix a skill that isn't triggering,
  or package a skill folder for distribution.
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
    - Agent Skills
    - SKILL.md
    - Validation
    - Packaging
    - Meta
    related_skills: []
prerequisites:
  commands:
  - python
  python:
  - pyyaml
---

# Skill Builder

Author new [Agent Skills](https://modelcontextprotocol.io) — the `SKILL.md`
instruction packages that teach an agent a specialized capability — and validate
and package them for distribution.

## When to Use

- "Create a skill that does X."
- "My skill isn't triggering / improve its description."
- "Package this skill folder so others can install it."

## Skill anatomy

A skill is a folder named in `kebab-case` containing a `SKILL.md`, plus optional
`scripts/`, `references/`, `templates/`, or `assets/`:

```
my-skill/
├── SKILL.md            # required: frontmatter + instructions
├── scripts/            # optional: code the agent runs
└── references/         # optional: docs loaded only when needed
```

`SKILL.md` starts with YAML frontmatter:

```markdown
---
name: my-skill                 # kebab-case, matches the folder name
description: What it does AND when to use it — this is the triggering signal.
license: MIT
---

# My Skill
Instructions for the agent...
```

## Writing a description that triggers

The `description` is how the agent decides whether to load the skill. Make it
carry both halves:

- **What** the skill does (capabilities, file types, verbs).
- **When** to use it — concrete trigger phrases the user might say
  ("convert to markdown", "merge PDFs", "build an MCP server").

Pack real keywords; avoid vague language. Keep the body focused — push long
reference material into `references/` so it loads only when needed.

## Validate

```bash
pip install pyyaml
python scripts/validate_skill.py path/to/my-skill
```

Checks frontmatter is well-formed YAML, `name`/`description` are present,
`name` is kebab-case and matches the folder, and the body is non-empty.

## Package

```bash
python scripts/package_skill.py path/to/my-skill -o my-skill.skill
```

Validates first, then produces an installable `.skill` archive that unpacks as
`my-skill/...`.

## Tips

- One skill = one coherent capability. Split unrelated jobs into separate skills.
- Prefer bundling a small script over re-deriving the same logic each run.
- Test the description by checking it triggers on the phrasings users actually
  use, and doesn't fire on unrelated requests.

## Credits

Original skill by Rinu (l3ad3r1) in collaboration with Claude (Anthropic).
Based on the public Agent Skills / `SKILL.md` conventions. The bundled
`validate_skill.py` and `package_skill.py` are original works (MIT).
