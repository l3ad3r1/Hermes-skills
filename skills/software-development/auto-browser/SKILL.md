---
name: auto-browser
description: "Real human-in-the-loop browser automation via the open-source auto-browser MCP control plane (Playwright controller + Chromium, auth-profile reuse, noVNC takeover). Use for browser automation, scraping JS-rendered pages, and authenticated multi-step web flows. Runs as a local Docker stack; on Windows deploy via Docker Engine in WSL2."
version: 1.0.0
author: Rinu (l3ad3r1) in collaboration with Claude (Anthropic)
license: MIT
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: [Browser Automation, Playwright, MCP, Human-in-the-loop, Web Scraping, Auth Profiles, Docker, WSL2, noVNC]
    related_skills: [dev-browser, agent-reach]
prerequisites:
  commands: [docker, uvx, curl]
---

# Auto Browser

Give the agent a **real, human-in-the-loop browser**. Auto Browser is an
MCP-native browser control plane (a FastAPI controller + a Chromium browser node)
with shared sessions, reusable auth profiles, approval gates, audit trails, and
noVNC human takeover. This skill documents and wires up the upstream project; it
does not vendor it.

Upstream: [auto-browser](https://github.com/LvcidPsyche/auto-browser) by
LvcidPsyche (MIT).

## When to Use

- Navigating, reading, or interacting with any website — especially JS-rendered
  pages, SPAs, dashboards, and multi-step flows.
- Authenticated, "log in once, reuse later" workflows (saved auth profiles).
- Forms, clicks, and flows where a human may need to step in (noVNC takeover).
- Anywhere a plain HTTP fetch isn't enough (logins, dynamic content, session state).

Not for: CAPTCHA solving, unauthorized scraping, or deceptive automation — the
upstream project explicitly excludes these.

## Setup

Auto Browser runs as a Docker stack (controller + Chromium browser-node):

```bash
git clone https://github.com/LvcidPsyche/auto-browser.git
cd auto-browser
docker compose up --build -d
```

Endpoints once up:
- Controller / MCP: `http://127.0.0.1:8000` (MCP at `/mcp`, dashboard at `/dashboard`)
- Human takeover (noVNC): `http://127.0.0.1:6080/vnc.html`

Register the MCP stdio bridge with your client (needs [uv](https://docs.astral.sh/uv/)):

```jsonc
{
  "mcpServers": {
    "auto-browser": {
      "command": "uvx",
      "args": ["auto-browser-mcp"],
      "env": { "AUTO_BROWSER_BASE_URL": "http://127.0.0.1:8000/mcp" }
    }
  }
}
```

For Claude Code: `claude mcp add-json auto-browser '{ ... }' --scope user`.

Readiness check — note there is **no** `/health` route (it 404s):

```bash
curl -s -o /dev/null -w "%{http_code}" http://127.0.0.1:8000/mcp/tools   # 200 = up
```

## Tools (curated MCP profile, `browser.*`)

Typical loop: `browser.create_session` → `browser.observe` → act
(`browser.execute_action`, `browser.find_by_vision`, `browser.find_elements`,
`browser.wait_for_selector`) → capture (`browser.screenshot`, `browser.get_html`,
`browser.get_network_log`) → reuse auth (`browser.list_auth_profiles`) →
`browser.close_session`. There are ~35 curated tools; set `MCP_TOOL_PROFILE=full`
for the admin/agent/harness surface.

## Installation notes & known issues

These are real problems hit while deploying this skill on Windows 11, and the
fixes that worked — they may save you hours.

**1. Docker Desktop's Windows AF_UNIX socket layer can be broken.**
On one Windows 11 host, Docker Desktop's backend crashed on every start while
binding its internal AF_UNIX sockets (`dockerInference`, then
`docker-secrets-engine\engine.sock`) with *"The file cannot be accessed by the
system / the filename, directory name, or volume label syntax is incorrect."* The
failure recurs **even on a clean directory**, so it isn't stale files — the
socket bind/remove itself fails. `netsh winsock reset` + reboot did **not** fix
it. (Orphaned AF_UNIX socket files left behind also can't be deleted by Windows;
only `rm` from inside WSL removes them.)

**Fix that worked — run the stack as Docker Engine inside WSL2 instead of Docker
Desktop:**
```bash
# inside WSL2 (Ubuntu, systemd enabled):
curl -fsSL https://get.docker.com | sudo sh
sudo usermod -aG docker $USER          # then run `wsl --shutdown` and reopen
sudo systemctl enable --now docker
git clone https://github.com/LvcidPsyche/auto-browser.git ~/auto-browser
cd ~/auto-browser && docker compose up --build -d
```
WSL2 forwards `localhost:8000` to Windows, so the Windows-side `uvx
auto-browser-mcp` bridge connects unchanged. Linux uses native sockets and
sidesteps the broken Windows AF_UNIX layer entirely.

**2. WSL2 shuts the VM down when idle (~8s), killing the stack.**
Containers run with `restart: unless-stopped`, so they restart when dockerd
starts — but the VM must be kept warm. A per-user logon task running
`wsl -d Ubuntu -e bash -lc "cd ~/auto-browser && docker compose up -d && exec sleep infinity"`
keeps the VM alive and the controller reachable across idle periods and reboots.

**3. Build inside the WSL filesystem** (`~/auto-browser`), not a `/mnt/<drive>`
Windows path — NTFS-over-9P builds are slow and can hit CRLF/permission issues. A
fresh `git clone` inside WSL gives clean LF line endings.

## Credits

Upstream project: [auto-browser](https://github.com/LvcidPsyche/auto-browser) by
**LvcidPsyche** (MIT). The MCP stdio bridge ships on PyPI as `auto-browser-mcp`.
This skill documents and wires up the upstream tool for the Agent Skills format;
the source is **not vendored** — install it from the upstream repo / PyPI.

Skill by **Rinu ([l3ad3r1](https://github.com/l3ad3r1)) in collaboration with
Claude (Anthropic)**.
