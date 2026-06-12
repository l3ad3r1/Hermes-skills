---
name: dev-browser
description: "Drive a real browser (navigate, click, fill, screenshot, full Playwright API) via sandboxed JS using the open-source dev-browser CLI."
version: 1.0.0
author: Sawyer Hood (upstream, MIT); skill packaged by Rinu (l3ad3r1) with Claude (Anthropic)
license: MIT
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: [Browser Automation, Playwright, Web Scraping, Chromium, Web Testing, dev-browser]
    related_skills: []
prerequisites:
  commands: [node, npm, dev-browser]
---

# Dev Browser

Control a real browser with sandboxed JavaScript scripts, powered by the
open-source [`dev-browser`](https://github.com/SawyerHood/dev-browser) CLI
(a thin, safe wrapper over the full Playwright API).

## When to Use

- Open a URL and read / screenshot it.
- Scrape or extract data from a page (especially JS-rendered sites).
- Fill in and submit a web form, or click through a flow.
- End-to-end test a web app in a real browser.
- Anything a plain HTTP fetch can't do (logins, dynamic SPA content).

## Prerequisites

```bash
npm install -g dev-browser
dev-browser install     # installs Playwright + Chromium
```

Requires Node.js. On Windows the installer pulls the native
`dev-browser-windows-x64.exe` automatically.

## Usage

Pipe a JavaScript snippet into `dev-browser`. Scripts run in a QuickJS WASM
sandbox (no host filesystem access); a `browser` object is provided, and pages
persist across invocations.

```bash
dev-browser --headless <<'EOF'
const page = await browser.getPage("main");
await page.goto("https://example.com", { waitUntil: "domcontentloaded" });
console.log(await page.title());
EOF
```

Windows PowerShell uses a here-string:

```powershell
@"
const page = await browser.getPage("main");
await page.goto("https://example.com", { waitUntil: "domcontentloaded" });
console.log(await page.title());
"@ | dev-browser --headless
```

Run `dev-browser --help` for the full LLM usage guide and API reference
(`goto`, `click`, `fill`, locators, `evaluate`, `screenshot`, …).

## Notes & Limits

- Needs Node.js and a one-time `dev-browser install` for Chromium.
- Sandboxed scripts can't touch the host FS — pass data via stdin, read results
  from stdout (`console.log`).
- `--connect` attaches to a running Chrome (start it with
  `--remote-debugging-port=9222`); `--headless` launches fresh Chromium.

## Credits

Wraps the open-source **[dev-browser](https://github.com/SawyerHood/dev-browser)**
CLI by **Sawyer Hood** (MIT), brought to you by [Do Browser](https://dobrowser.io).
All credit for the engine belongs to its authors; this skill only adds usage
guidance. Packaged by Rinu (l3ad3r1) with Claude (Anthropic).
