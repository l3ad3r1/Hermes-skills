# PROGRESS

## Just completed
- Mirrored `social-media-analyzer` into `skills/data-science/` from
  borghei/Claude-Skills (MIT + Commons Clause, Amin Borghei) — Hermes frontmatter
  (author w/ mirror credit, upstream link, hermes.tags, prerequisites.commands)
  + identical body to canonical (Credits note included) + NOTICE.md + the same
  bundled scripts/assets/references as canonical. README table row + credits
  updated. Note: SKILL.md is ~19.9KB, above the 15KB SkillConstraints soft cap
  (brandkit already exceeds it too) — trim later if the Android loader complains.
  Parity with Claude-skills-repo verified OK. Released alongside Claude-skills-repo
  v1.7.0.

- Added new `design/` category with the **Taste Skill family** — 12 skills
  mirrored from leonxlnx/taste-skill (MIT, tasteskill.dev): taste-skill,
  soft-skill, minimalist-skill, brutalist-skill, redesign-skill, gpt-tasteskill,
  image-to-code-skill, stitch-skill, brandkit, imagegen-frontend-web,
  imagegen-frontend-mobile, output-skill. Hermes frontmatter (author=Leonxlnx,
  upstream link, hermes.tags) + Credits note appended to each SKILL.md body to
  match canonical. README table + credits updated. Parity OK (25 skills, 2
  expected warnings). Released **v1.4.0**.

- Mirrored `auto-browser` (LvcidPsyche, MIT) and `headroom` (chopratejas,
  Apache-2.0) into skills/software-development/ with Hermes frontmatter, NOTICE.md,
  README table + credits, each with "Installation notes & known issues" covering
  the Windows problems and WSL2 fixes. Parity OK (13 skills). Released **v1.3.0**.

- Applied trigger-disambiguation lines to descriptions (mirrors Claude-skills-repo):
  - markitdown-converter vs docx/pdf/pptx/xlsx toolkits (both directions)
  - dev-browser: scripted Playwright automation note
- Ported `animejs` skill from Claude-skills-repo into
  skills/software-development/animejs (Hermes frontmatter: version/author/
  license/platforms/metadata.hermes.tags)
- Updated README skills table + credits and the software-development
  DESCRIPTION.md to include animejs

- Pushed main and cut first release **v1.0.0** (9 skills).
- Added `clone-website` (adapted from JCodesMore template, MIT); pushed and
  released **v1.1.0** (10 skills).
- Added `agent-reach` under software-development (documents/drives the
  Panniantong/agent-reach CLI, MIT); pushed and released **v1.2.0** (11 skills).

## In progress
- (none)

## Next steps
- This repo is the DERIVED copy; Claude-skills-repo is canonical. Mirror
  new/changed skills here and run its tools/check_parity.py before release.
