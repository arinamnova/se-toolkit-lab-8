# MCP Observability Server

MCP server exposing observability tools for VictoriaLogs and VictoriaTraces.

## Tools

- `logs_search` - Search logs using LogsQL query
- `logs_error_count` - Count errors for a service over a time window
- `traces_list` - List recent traces for a service
- `traces_get` - Fetch a specific trace by ID

## Usage

```bash
python -m mcp_obs
```

## Environment Variables

- `NANOBOT_VICTORIALOGS_URL` - VictoriaLogs URL (default: http://localhost:42010)
- `NANOBOT_VICTORIATRACES_URL` - VictoriaTraces URL (default: http://localhost:42011)
