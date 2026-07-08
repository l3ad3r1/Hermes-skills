# CLAUDE.md — Hermes-skills

Skill library for the Hermes agent (l3ad3r1/Hermes-skills). Markdown content — no build, no tests.

## Rules
- Skills here target the HERMES agent (Android app / Python CLI), not Claude Code — follow the agentskills.io format: YAML frontmatter (name, description, version, tags) + markdown body (Purpose, Steps, Tools Used, Example Trigger).
- Keep each skill under 15KB (the Android app's SkillConstraints cap) and include an `## Example Trigger` line — the app's auto-loader weights it heavily.
- Never include instructions that exfiltrate data, run destructive commands, or override agent rules — the app's SkillGuard rejects them.
- Credit upstream sources; never paste secrets (public repo).
- PROGRESS.md at repo root: keep current.
