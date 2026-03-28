"""MCP server exposing observability tools for VictoriaLogs and VictoriaTraces."""

import asyncio
import json
from typing import Any

import httpx
from mcp.server import Server
from mcp.server.stdio import stdio_server
from mcp.types import TextContent, Tool
from pydantic import BaseModel


class LogsSearchParams(BaseModel):
    query: str = "severity:ERROR"
    limit: int = 10


class LogsErrorCountParams(BaseModel):
    service: str = "Learning Management Service"
    minutes: int = 60


class TracesListParams(BaseModel):
    service: str = "Learning Management Service"
    limit: int = 10


class TracesGetParams(BaseModel):
    trace_id: str


async def _logs_search(client: ObservabilityClient, args: LogsSearchParams) -> dict:
    """Search logs in VictoriaLogs using LogsQL query."""
    url = f"{client.victorialogs_url}/select/logsql/query"
    params = {"query": args.query, "limit": args.limit}
    async with httpx.AsyncClient() as http:
        resp = await http.get(url, params=params, timeout=30.0)
        resp.raise_for_status()
        return resp.json()


async def _logs_error_count(client: ObservabilityClient, args: LogsErrorCountParams) -> dict:
    """Count errors per service over a time window."""
    query = f"_time:{args.minutes}m service.name:\"{args.service}\" severity:ERROR"
    url = f"{client.victorialogs_url}/select/logsql/query"
    params = {"query": query, "limit": 100}
    async with httpx.AsyncClient() as http:
        resp = await http.get(url, params=params, timeout=30.0)
        resp.raise_for_status()
        results = resp.json()
        # Count the number of error entries
        if isinstance(results, list):
            return {"service": args.service, "error_count": len(results), "window_minutes": args.minutes}
        return {"service": args.service, "error_count": 0, "window_minutes": args.minutes}


async def _traces_list(client: ObservabilityClient, args: TracesListParams) -> dict:
    """List recent traces for a service from VictoriaTraces."""
    url = f"{client.victoriatraces_url}/select/jaeger/api/traces"
    params = {"service": args.service, "limit": args.limit}
    async with httpx.AsyncClient() as http:
        resp = await http.get(url, params=params, timeout=30.0)
        resp.raise_for_status()
        return resp.json()


async def _traces_get(client: ObservabilityClient, args: TracesGetParams) -> dict:
    """Fetch a specific trace by ID from VictoriaTraces."""
    url = f"{client.victoriatraces_url}/select/jaeger/api/traces/{args.trace_id}"
    async with httpx.AsyncClient() as http:
        resp = await http.get(url, timeout=30.0)
        resp.raise_for_status()
        return resp.json()


class ObservabilityClient:
    def __init__(self, victorialogs_url: str, victoriatraces_url: str):
        self.victorialogs_url = victorialogs_url
        self.victoriatraces_url = victoriatraces_url


def create_server(client: ObservabilityClient) -> Server:
    server = Server("mcp-obs")

    @server.list_tools()
    async def list_tools() -> list[Tool]:
        return [
            Tool(
                name="logs_search",
                description="Search logs in VictoriaLogs using LogsQL query. Use severity:ERROR for errors, service.name for filtering by service.",
                inputSchema=LogsSearchParams.model_json_schema(),
            ),
            Tool(
                name="logs_error_count",
                description="Count errors for a specific service over a time window (in minutes).",
                inputSchema=LogsErrorCountParams.model_json_schema(),
            ),
            Tool(
                name="traces_list",
                description="List recent traces for a service from VictoriaTraces.",
                inputSchema=TracesListParams.model_json_schema(),
            ),
            Tool(
                name="traces_get",
                description="Fetch a specific trace by ID to see the full span hierarchy and find where errors occurred.",
                inputSchema=TracesGetParams.model_json_schema(),
            ),
        ]

    @server.call_tool()
    async def call_tool(name: str, arguments: dict[str, Any] | None) -> list[TextContent]:
        handlers = {
            "logs_search": lambda args: _logs_search(client, LogsSearchParams(**(args or {}))),
            "logs_error_count": lambda args: _logs_error_count(client, LogsErrorCountParams(**(args or {"service": "Learning Management Service", "minutes": 60}))),
            "traces_list": lambda args: _traces_list(client, TracesListParams(**(args or {"service": "Learning Management Service", "limit": 10}))),
            "traces_get": lambda args: _traces_get(client, TracesGetParams(**(args or {"trace_id": ""}))),
        }
        handler = handlers.get(name)
        if handler is None:
            return [TextContent(type="text", text=f"Unknown tool: {name}")]
        try:
            result = await handler(arguments)
            return [TextContent(type="text", text=json.dumps(result, indent=2, ensure_ascii=False))]
        except Exception as exc:
            return [TextContent(type="text", text=f"Error: {type(exc).__name__}: {exc}")]

    _ = list_tools, call_tool
    return server


async def main() -> None:
    import os

    victorialogs_url = os.environ.get("NANOBOT_VICTORIALOGS_URL", "http://localhost:42010")
    victoriatraces_url = os.environ.get("NANOBOT_VICTORIATRACES_URL", "http://localhost:42011")

    client = ObservabilityClient(victorialogs_url, victoriatraces_url)
    server = create_server(client)
    async with stdio_server() as (read_stream, write_stream):
        init_options = server.create_initialization_options()
        await server.run(read_stream, write_stream, init_options)


if __name__ == "__main__":
    asyncio.run(main())
