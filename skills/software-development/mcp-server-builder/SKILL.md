---
name: mcp-server-builder
description: Build Model Context Protocol (MCP) servers that expose tools, resources,
  and prompts to LLM clients. Covers the official Python SDK (FastMCP) and the Node/TypeScript
  SDK, transports (stdio vs HTTP), registering servers with clients, and tool-design
  best practices. Use this skill whenever the user wants to create an MCP server,
  wrap an API or service as MCP tools, or connect a custom backend to Claude/other
  MCP clients.
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
    - MCP
    - Model Context Protocol
    - FastMCP
    - Tools
    - SDK
    related_skills: []
prerequisites:
  commands:
  - python
  - node
  python:
  - mcp[cli]
---

# MCP Server Builder

Build [Model Context Protocol](https://modelcontextprotocol.io) servers that
give LLM clients well-designed tools, resources, and prompts. Uses the official
open-source SDKs (both MIT licensed).

## When to Use

- "Build an MCP server for X" / "wrap this API as MCP tools."
- "Connect my custom backend to Claude Code / an MCP client."
- Designing tool schemas, choosing a transport, or debugging an MCP server.

## Python (FastMCP — recommended for most servers)

```bash
pip install "mcp[cli]"
```

A complete starter server lives in [`templates/server.py`](templates/server.py).
The core pattern:

```python
from mcp.server.fastmcp import FastMCP
mcp = FastMCP("my-server")

@mcp.tool()
def add(a: float, b: float) -> float:
    """Add two numbers. The docstring IS the model-facing description."""
    return a + b

if __name__ == "__main__":
    mcp.run()   # stdio transport by default
```

Run it and register with a client:

```bash
python templates/server.py
claude mcp add my-server -- python /abs/path/to/server.py
```

## Node / TypeScript

```bash
npm install @modelcontextprotocol/sdk zod
```

```ts
import { McpServer } from "@modelcontextprotocol/sdk/server/mcp.js";
import { StdioServerTransport } from "@modelcontextprotocol/sdk/server/stdio.js";
import { z } from "zod";

const server = new McpServer({ name: "my-server", version: "1.0.0" });
server.tool("add", { a: z.number(), b: z.number() }, async ({ a, b }) => ({
  content: [{ type: "text", text: String(a + b) }],
}));
await server.connect(new StdioServerTransport());
```

## Transports

- **stdio** — default for local clients (Claude Code, desktop). The client
  launches your process and talks over stdin/stdout. Never write logs to
  stdout — use stderr.
- **streamable-http** — for remote/hosted servers. In Python: `mcp.run(transport="streamable-http")`.

## Tool-design best practices

- **Name tools by action** and write a precise docstring/description — it's what
  the model uses to decide when to call the tool.
- **Keep parameters typed and minimal**; use enums/constraints so bad calls fail
  fast. FastMCP derives the JSON schema from type hints; the TS SDK uses `zod`.
- **Return concise, structured text**; avoid dumping huge payloads.
- **Make tools idempotent where possible** and validate inputs.
- **One job per tool** — prefer several focused tools over one mega-tool.

## Notes & Limits

- Test locally with the MCP Inspector (`npx @modelcontextprotocol/inspector`).
- For stdio servers, anything on stdout that isn't protocol traffic breaks the
  client — log to stderr.

## Credits

Original skill by Rinu (l3ad3r1) in collaboration with Claude (Anthropic).
Built on the official [MCP Python SDK](https://github.com/modelcontextprotocol/python-sdk)
and [TypeScript SDK](https://github.com/modelcontextprotocol/typescript-sdk)
(both MIT). The Model Context Protocol is an open standard; all credit for the
SDKs and spec belongs to their authors.
