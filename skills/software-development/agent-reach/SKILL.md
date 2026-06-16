---
name: agent-reach
description: Give your AI agent eyes on the whole internet — install and drive the open-source Agent Reach CLI to read and search web pages, Twitter/X, YouTube, Reddit, GitHub, RSS, Bilibili, Xiaohongshu, LinkedIn, V2EX, Xueqiu, podcasts, and global web search (Exa) through one unified, zero-API-fee tool with automatic backend failover. Use whenever the user wants the agent to fetch, read, scrape, or search content from a site or platform a plain HTTP fetch can't reach — especially login-walled or JS-heavy sources like tweets, threads, video transcripts, or Reddit posts — or asks to "install agent-reach", "set up agent reach", or "give you internet access". Optionally pass a URL or search query as the argument.
argument-hint: "[<url-or-search-query>]"
user-invocable: true
version: 1.0.0
author: Panniantong (upstream Agent Reach, MIT); skill packaged by Rinu (l3ad3r1) with Claude (Anthropic)
license: MIT
platforms:
- linux
- macos
- windows
metadata:
  hermes:
    tags:
    - Web Access
    - Agent Tooling
    - Scraping
    - Search
    - CLI
---

# Agent Reach

[Agent Reach](https://github.com/Panniantong/agent-reach) is an open-source CLI
that gives an AI agent practical access to the live internet. It wraps a fleet
of free / open-source backends (Jina Reader, twitter-cli, yt-dlp, OpenCLI,
rdt-cli, bili-cli, `gh`, feedparser, Exa via MCP) behind one tool with a
**primary + fallback** architecture: when one backend fails, it transparently
switches to another, so you keep reading instead of debugging auth.

Use this skill to **install** Agent Reach on the user's machine, **diagnose**
which channels are live, and then **read and search** content from platforms a
plain `WebFetch`/`curl` can't reach.

`$ARGUMENTS` — if the user passed a URL or a search query, that's the target to
fetch or search once the tool is ready.

## When to use this

Reach for Agent Reach when the content lives behind something a simple HTTP
fetch can't handle:

- **Login-walled or JS-heavy pages** — tweets/threads, Xiaohongshu posts,
  LinkedIn, Reddit threads.
- **Media transcripts** — YouTube, Bilibili, podcasts (Xiaoyuzhou).
- **Structured feeds and code hosts** — RSS/Atom, GitHub issues/PRs/repos.
- **Open-web research** — global search via Exa when you need to *find* sources,
  not just read a known URL.

If a plain `WebFetch` of a public static page already works, just use that —
don't install a whole CLI for a one-off readable page.

## Safety boundaries (read before installing)

Agent Reach modifies the user's environment, so honor these limits:

1. **Stay inside `~/.agent-reach/`.** Config, tokens, and tool repos all live
   there (`~/.agent-reach/tools/`). Temp work goes to `/tmp/`. Do **not** clone
   repos or drop files into the user's project workspace.
2. **Never `sudo`** without explicit user approval. If a step needs elevated
   permissions, stop and ask first.
3. **Credentials stay local.** Cookies/tokens are written to
   `~/.agent-reach/config.yaml` with `600` permissions and are never transmitted
   off-machine. Treat that file as secret — never print or commit it.
4. **Account-ban risk on login channels.** Twitter/X and Xiaohongshu can ban
   accounts used for automated reading. Tell the user to log in with a
   **dedicated secondary account**, never their primary.
5. **Prefer a dry run first.** Use `--safe` (preview, no changes) or `--dry-run`
   to show the user what will happen before mutating anything.

## Install

Agent Reach is **not vendored** in this skill — it's installed from upstream.
Detect the OS and pick an install path. Run these in the user's shell (the Bash
tool); on Windows, run them under WSL or a POSIX shell since the upstream tool
targets Unix-like environments.

**Preferred — pipx (isolated):**

```bash
pipx install https://github.com/Panniantong/agent-reach/archive/main.zip
agent-reach install --env=auto
```

**Fallback — virtualenv (use if PEP 668 blocks a global install):**

```bash
python3 -m venv ~/.agent-reach-venv
source ~/.agent-reach-venv/bin/activate
pip install https://github.com/Panniantong/agent-reach/archive/main.zip
agent-reach install --env=auto
```

`agent-reach install` detects local-vs-server environment, configures the search
backend, and registers the per-channel capability docs the agent reads later.
`--env=auto` lets it choose; pass `--safe` to preview without changes.

### Optional channels

The default install brings up the no-login channels. Add login/extra channels
explicitly:

```bash
# install specific channels
agent-reach install --env=auto --channels=opencli,twitter

# install everything
agent-reach install --env=auto --channels=all
```

Optional channels include `opencli`, `twitter`, `xiaohongshu`, `reddit`,
`bilibili`, `xueqiu`, `xiaoyuzhou`, and `linkedin`.

## Verify & configure

```bash
agent-reach doctor              # status of every channel (ready / needs login / error)
agent-reach watch               # health + update check
agent-reach configure proxy     # set an outbound proxy URL
agent-reach configure groq-key  # set a Groq API key (for backends that use it)
agent-reach update              # update an existing install
agent-reach uninstall [--keep-config] [--dry-run]
```

Always run `agent-reach doctor` after installing and report the result to the
user — it's the source of truth for what's reachable right now and what still
needs a login.

## Channels at a glance

| Platform | Login required |
|---|---|
| Web pages (Jina Reader) | No |
| YouTube (transcripts) | No |
| RSS / Atom | No |
| GitHub (`gh`) | No (richer with login) |
| Global search (Exa) | No |
| Bilibili | No |
| V2EX | No |
| Xueqiu | No (configurable) |
| Twitter / X | **Yes** (ban risk — use a burner) |
| Reddit | **Yes** |
| Xiaohongshu | **Yes** (ban risk — use a burner) |
| LinkedIn | **Yes** (configurable) |
| Xiaoyuzhou (podcasts) | **Yes** |

## Reading & searching

After install, fetch and search through the channels Agent Reach set up. The
agent-facing reading workflow is driven by the capability docs that
`agent-reach install` registers and that `agent-reach doctor` points to — read
those for the exact, current invocation of each channel rather than guessing,
because the upstream backends evolve.

In practice that means:

1. Run `agent-reach doctor` to confirm the channel for the target URL/query is
   ready (and log in first if it reports "needs login").
2. Follow the registered capability instructions for that channel to read the
   URL or run the search. For some channels you'll call the underlying tool the
   installer placed on `PATH` directly — e.g. `yt-dlp` for YouTube transcripts,
   `gh` for GitHub, `bili` for Bilibili, `rdt` for Reddit, `opencli` for
   Xiaohongshu, and `mcporter`/Exa for open-web search.
3. If a backend errors, let the primary→fallback design retry, or re-run
   `doctor` to see which backend degraded.

If the user gave a target in `$ARGUMENTS`, route it to the matching channel once
`doctor` confirms it's ready, then return the extracted content.

## Compatibility

Agent Reach works with any agent that can run shell commands — Claude Code,
Cursor, Windsurf, OpenClaw, and others. The upstream backends target Unix-like
environments; on Windows, drive it through WSL.

## Credits

Agent Reach is created by **Panniantong** ([@Neo_Reidlab](https://x.com/Neo_Reidlab),
`pnt01@foxmail.com`) and released under the **MIT License** —
<https://github.com/Panniantong/agent-reach>. All credit for the tool and its
backend integrations belongs to its author and contributors. This skill only
documents how to install and drive the upstream CLI; it does not vendor or
modify it.

Skill packaged by Rinu ([l3ad3r1](https://github.com/l3ad3r1)) in collaboration
with Claude (Anthropic).
