---
name: observability
description: Use observability MCP tools to investigate errors and traces
always: true
---

# Observability Skill

You have access to observability tools that can query VictoriaLogs and VictoriaTraces to investigate errors and trace request flows.

## Available Tools

| Tool               | Description                                                                                                    |
| ------------------ | -------------------------------------------------------------------------------------------------------------- |
| `logs_search`      | Search logs using LogsQL query. Use `severity:ERROR` for errors, `service.name:"..."` for filtering by service |
| `logs_error_count` | Count errors for a specific service over a time window                                                         |
| `traces_list`      | List recent traces for a service                                                                               |
| `traces_get`       | Fetch a specific trace by ID to see the full span hierarchy                                                    |
| `cron`             | Schedule recurring jobs (for health checks)                                                                    |

## Strategy Rules

### When the user asks "What went wrong?" or "Check system health":

1. **Start with `logs_error_count`** to see if there are recent errors
   - Use a narrow time window (2-10 minutes) for recent issues
   - Specify the service name (e.g., "Learning Management Service" for LMS backend)

2. **If errors exist, use `logs_search`** to inspect the relevant logs
   - Query: `_time:10m service.name:"Learning Management Service" severity:ERROR`
   - Look for `trace_id` in the error logs
   - Note the error message and timestamp

3. **If you find a trace_id, use `traces_get`** to fetch the full trace
   - This shows the span hierarchy and where the error occurred
   - Look for spans with `error` or `exception` attributes
   - Note which operation failed and why

4. **Summarize findings concisely** - cite both log and trace evidence:
   - State what the logs show (error type, time, service)
   - State what the trace shows (request flow, failing operation)
   - Explain the root cause in plain language
   - Don't dump raw JSON

### When the user asks about errors or failures:

1. **Start with `logs_error_count`** to see if there are recent errors
   - Use a narrow time window (10 minutes) for recent issues
   - Specify the service name (e.g., "Learning Management Service" for LMS backend)

2. **If errors exist, use `logs_search`** to inspect the relevant logs
   - Query: `_time:10m service.name:"Learning Management Service" severity:ERROR`
   - Look for `trace_id` in the error logs

3. **If you find a trace_id, use `traces_get`** to fetch the full trace
   - This shows the span hierarchy and where the error occurred
   - Look for spans with `error` or `exception` attributes

4. **Summarize findings concisely**
   - Don't dump raw JSON
   - Explain what went wrong in plain language
   - Mention which service/component failed and why

### When the user asks to create a health check:

1. Use the `cron` tool to schedule a recurring job
2. Each run should:
   - Call `logs_error_count` for the last 2 minutes
   - If errors exist, call `logs_search` to get details
   - If a trace_id is found, call `traces_get` to inspect
   - Post a short summary to the chat

### When the user asks to list scheduled jobs:

1. Use `cron({"action": "list"})` to show all scheduled jobs

### Query tips:

- **Time format**: `_time:10m` for last 10 minutes, `_time:1h` for last hour
- **Service filter**: `service.name:"Learning Management Service"`
- **Severity filter**: `severity:ERROR` or `severity:WARN`
- **Event filter**: `event:db_query` for database queries

### Example queries:

```
# Recent errors in LMS backend
_time:10m service.name:"Learning Management Service" severity:ERROR

# All database errors
_time:1h event:db_query severity:ERROR

# Errors in a specific time range
_time:2026-03-28T09:50:00Z_2026-03-28T10:00:00Z severity:ERROR
```

## Response format

When reporting errors:

1. State whether errors were found
2. Summarize the error (what, where, when)
3. If applicable, explain the root cause from the trace
4. Suggest what to check or fix

Example investigation response:

> "Found 1 error in the LMS backend in the last 10 minutes.
>
> **Log evidence:** At 09:59:12 UTC, the `db_query` event failed with `asyncpg.exceptions.InterfaceError: connection is closed` when executing a SELECT on the `item` table.
>
> **Trace evidence:** Trace `17bad051...` shows the request flow: HTTP request → auth success → db_query span failed → HTTP 404 returned.
>
> **Root cause:** PostgreSQL was unreachable. The database connection pool had a stale connection that was already closed."
