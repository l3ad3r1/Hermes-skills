#!/usr/bin/env python3
"""Minimal MCP server template using FastMCP (official Python MCP SDK).

Run (stdio transport, the default for local MCP clients):
    pip install "mcp[cli]"
    python server.py

Register with a client (e.g. Claude Code):
    claude mcp add my-server -- python /abs/path/to/server.py

Docs: https://modelcontextprotocol.io  •  SDK: https://github.com/modelcontextprotocol/python-sdk
"""
from __future__ import annotations

from mcp.server.fastmcp import FastMCP

mcp = FastMCP("my-server")


@mcp.tool()
def add(a: float, b: float) -> float:
    """Add two numbers and return the sum.

    Tool docstrings ARE the description the model sees — make them clear and
    say exactly what the tool does and when to use it.
    """
    return a + b


@mcp.tool()
def greet(name: str) -> str:
    """Return a friendly greeting for the given name."""
    return f"Hello, {name}!"


@mcp.resource("config://app")
def app_config() -> str:
    """Expose read-only data as a resource the client can fetch."""
    return "app=demo; version=1.0.0"


if __name__ == "__main__":
    # transport="stdio" is the default; use "streamable-http" for a web server.
    mcp.run()
