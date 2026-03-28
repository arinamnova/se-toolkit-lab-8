# Lab 8 — Report

Paste your checkpoint evidence below. Add screenshots as image files in the repo and reference them with `![description](path)`.

## Task 1A — Bare agent

**Question 1: "What is the agentic loop?"**

I MADE CHANGES

The agentic loop is the core reasoning cycle that enables AI agents to act autonomously. It's the continuous process an
agent follows to perceive, decide, and act in pursuit of a goal.

Core Cycle

 ┌─────────────┐
 │   Perceive  │ ──→ Gather information (input, state, context)
 └──────┬──────┘
        ↓
 ┌─────────────┐
 │    Think    │ ──→ Reason, plan, select tools/actions
 └──────┬──────┘
        ↓
 ┌─────────────┐
 │     Act     │ ──→ Execute tools, make changes, produce output
 └──────┬──────┘
        ↓
 ┌─────────────┐
 │   Observe   │ ──→ Evaluate results, check for success/errors
 └──────┬──────┘
        ↓
     (repeat until goal achieved)

Each Phase

 Phase     What Happens
 ───────────────────────────────────────────────────────────────────
 Perceive  Read inputs, scan environment, collect relevant context
 Think     Analyze goals, reason about next steps, choose tools
 Act       Call tools, modify files, execute commands, send messages
 Observe   Check outputs, detect errors, assess progress

Key Properties

 • Iterative: Continues until the task is complete
 • Adaptive: Adjusts based on feedback and failures
 • Goal-directed: Every cycle moves toward accomplishing the objective
 • Self-correcting: Errors inform better decisions in subsequent iterations

In Practice (This Session)

When you ask me to do something:

 1 I perceive your request and check the workspace
 2 I think about what tools and steps are needed
 3 I act by calling tools (read_file, write_file, exec, etc.)
 4 I observe the results and decide whether to continue or report back

This loop is what makes an agent agentic—capable of independent, multi-step problem-solving rather than just single-turn
responses.

**Question 2: "What labs are available in our LMS?"**

Based on my exploration of the LMS repository, here's what I found:

Course Overview

This is the SET (Software Engineering Toolkit) course, which consists of 10 labs total. Each lab is 3 hours long.

Current Lab Available

You're currently in Lab 8 — The Agent is the Interface, which includes:

Required Tasks:

 1 Task 1: Set Up the Agent — install nanobot, configure Qwen API, add MCP tools, write skill prompt
 2 Task 2: Deploy and Connect a Web Client — Dockerize nanobot, add WebSocket channel + Flutter chat UI
 3 Task 3: Give the Agent New Eyes — explore observability data, write log/trace MCP tools
 4 Task 4: Diagnose a Failure and Make the Agent Proactive — investigate a failure, schedule health checks, fix a
   planted bug

Optional Tasks:

 1 Task 1: Add a Telegram Bot Client — same agent, different interface

Other Resources Available

The repository also contains:

 • Wiki — documentation on various topics (Docker, Git, Linux, Python, HTTP, databases, etc.)
 • Backend source code — the LMS application (FastAPI + PostgreSQL)
 • Infrastructure — Docker Compose setup, Caddy configuration
 • Setup guides — both simple and full setup instructions

The course focuses on computing ecosystem literacy and software engineering methods through hands-on practice with a web
app project, using AI agents as a central tool.

Would you like me to help you with a specific task in Lab 8, or are you looking for information about other labs in the
course?

## Task 1B — Agent with LMS tools

**Question 1: "What labs are available?"**

Here are the available labs:

 1 Lab 01 – Products, Architecture & Roles
 2 Lab 02 — Run, Fix, and Deploy a Backend Service
 3 Lab 03 — Backend API: Explore, Debug, Implement, Deploy
 4 Lab 04 — Testing, Front-end, and AI Agents
 5 Lab 05 — Data Pipeline and Analytics Dashboard
 6 Lab 06 — Build Your Own Agent
 7 Lab 07 — Build a Client with an AI Coding Agent
 8 lab-08

**Question 2: "Is the LMS backend healthy?"**

Yes, the LMS backend is healthy! It's currently tracking 56 items.

**Question 3: "Which lab has the lowest pass rate?"**

Based on the completion rates for all labs:

| Lab     | Completion Rate | Passed | Total |
|---------|-----------------|--------|-------|
| Lab 01  | 100.0%          | 258    | 258   |
| Lab 02  | 89.1%           | 131    | 147   |
| Lab 03  | 89.1%           | 156    | 175   |
| Lab 04  | 96.7%           | 238    | 246   |
| Lab 05  | 98.4%           | 246    | 250   |
| Lab 06  | 98.4%           | 241    | 245   |
| Lab 07  | 99.6%           | 236    | 237   |
| Lab 08  | 0.0%            | 0      | 0     |

Lab 08 has the lowest pass rate at 0.0%, though this appears to be because no students have attempted it yet (0 total submissions).

Among labs with actual submissions, Lab 02 and Lab 03 are tied for the lowest pass rate at 89.1%.

## Task 1C — Skill prompt

**Question: "Show me the scores" (without specifying a lab)**

I'll check what labs are available first, then show you the scores.

Here are the available labs:

 1 Lab 01 – Products, Architecture & Roles
 2 Lab 02 — Run, Fix, and Deploy a Backend Service
 3 Lab 03 — Backend API: Explore, Debug, Implement, Deploy
 4 Lab 04 — Testing, Front-end, and AI Agents
 5 Lab 05 — Data Pipeline and Analytics Dashboard
 6 Lab 06 — Build Your Own Agent
 7 Lab 07 — Build a Client with an AI Coding Agent
 8 Lab 08 — lab-08

Which lab would you like to see the scores for?

**Skill prompt created at:** `nanobot/workspace/skills/lms/SKILL.md`

The skill prompt teaches the agent:

- To call `lms_labs` first when the user asks about scores, pass rates, completion, groups, timeline, or top learners without naming a lab
- To present lab choices using the lab title as the label
- To ask the user to choose a lab before proceeding
- How to format numeric results (percentages, counts)
- How to handle errors and explain limitations

## Task 2A — Deployed agent

**Nanobot service status:**

```
NAME                                STATUS
se-toolkit-lab-8-nanobot-1          Up (running)
```

**Startup log excerpt:**

```
Using config: /app/nanobot/config.resolved.json
🐈 Starting nanobot gateway version 0.1.4.post5 on port 18790...
MCP server 'lms': connected, 9 tools registered
Agent loop started
```

The nanobot gateway is running as a Docker Compose service with:

- LMS MCP tools connected (9 tools: lms_health, lms_labs, lms_learners, lms_pass_rates, lms_timeline, lms_groups, lms_top_learners, lms_completion_rate, lms_sync_pipeline)
- Gateway listening on port 18790
- Qwen Code API configured as the LLM provider

## Task 2B — Web client

**WebSocket test response:**

```json
{
  "type": "text",
  "content": "Here are the available labs in the LMS:\n\n| # | Lab ID | Title |\n|---|--------|-------|\n| 1 | lab-01 | Lab 01 – Products, Architecture & Roles |\n| 2 | lab-02 | Lab 02 — Run, Fix, and Deploy a Backend Service |\n| 3 | lab-03 | Lab 03 — Backend API: Explore, Debug, Implement, Deploy |\n| 4 | lab-04 | Lab 04 — Testing, Front-end, and AI Agents |\n| 5 | lab-05 | Lab 05 — Data Pipeline and Analytics Dashboard |\n| 6 | lab-06 | Lab 06 — Build Your Own Agent |\n| 7 | lab-07 | Lab 07 — Build a Client with an AI Coding Agent |\n| 8 | lab-08 | lab-08 |\n\nWould you like to see details about a specific lab, such as pass rates, completion rates, group performance, or top learners?",
  "format": "markdown"
}
```

**Flutter web client:** Accessible at `http://<vm-ip>:42002/flutter/`

**What was built:**

- Added `nanobot-websocket-channel` as a git submodule
- Installed `nanobot-webchat` channel plugin and `mcp-webchat` MCP server
- Updated `entrypoint.py` to configure webchat channel and MCP server from env vars
- Enabled `/ws/chat` route in Caddyfile
- Enabled `/flutter` route in Caddyfile with Flutter build output volume
- Created sessions directory for nanobot session storage

**Files modified:**

- `pyproject.toml` - Added webchat workspace members and sources
- `docker-compose.yml` - Enabled nanobot, client-web-flutter services, updated volumes and env vars
- `caddy/Caddyfile` - Uncommented `/ws/chat` and `/flutter` routes
- `nanobot/Dockerfile` - Added nanobot-websocket-channel to build context
- `nanobot/config.json` - Added webchat channel and mcp-webchat server config
- `nanobot/entrypoint.py` - Already had webchat config (no changes needed)
- `nanobot/workspace/sessions/` - Created directory for session storage

## Task 3A — Structured logging

<!-- Paste happy-path and error-path log excerpts, VictoriaLogs query screenshot -->

## Task 3B — Traces

<!-- Screenshots: healthy trace span hierarchy, error trace -->

## Task 3C — Observability MCP tools

<!-- Paste agent responses to "any errors in the last hour?" under normal and failure conditions -->

## Task 4A — Multi-step investigation

**Question: "What went wrong?" (with PostgreSQL stopped)**

**Agent Response:**

Based on the trace data, I found the root cause of the issue:

**Root Cause: Database Connection Failure**

The LMS backend is experiencing a critical database connectivity issue. Here's what happened:

**Log Evidence:**

- At 13:11:06 UTC, the `db_query` event failed with error:
  `(sqlalchemy.dialects.postgresql.asyncpg.InterfaceError) <class 'asyncpg.exceptions._base.InterfaceError'>: connection is closed`
- The backend attempted to execute: `SELECT item.id, item.type, item.parent_id, item.title, item.description, item.attributes, item.created_at FROM item`
- The error occurred because the PostgreSQL connection was already closed

**Trace Evidence:**

- Trace ID: `17bad051aa9c4612ada36e45fc46720d`
- Request flow:
  1. HTTP request to `/items/` started
  2. Authentication succeeded
  3. Database query span failed with "connection is closed"
  4. HTTP 500 response returned (after fix) / HTTP 404 (before fix)

**Impact:**

- The `GET /items/` endpoint is returning HTTP 500 errors
- Lab listing functionality is unavailable
- All LMS operations requiring database access are failing

**Resolution:**
Restart the PostgreSQL service to restore database connectivity.

---

## Task 4B — Proactive health check

**Scheduled Job Created:**

The agent created a cron job that runs every 2 minutes to check for LMS backend errors.

**Proactive Health Report (while PostgreSQL was stopped):**

> "⚠️ **Unhealthy** - Backend errors detected
>
> Found 1 error in the Learning Management Service in the last 2 minutes:
>
> - Database connection failure (asyncpg.exceptions.InterfaceError: connection is closed)
> - Affected endpoint: GET /items/
> - HTTP 500 errors being returned
>
> **Recommendation:** Restart PostgreSQL service."

---

## Task 4C — Bug fix and recovery

### 1. Root Cause

**The planted bug** was in `/backend/src/lms_backend/routers/items.py`, lines 22-29:

```python
# BUGGY CODE:
except Exception as exc:
    logger.warning(
        "items_list_failed_as_not_found",
        extra={"event": "items_list_failed_as_not_found"},
    )
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Items not found",
    ) from exc
```

**Problem:** When any exception occurred (including database connection failures), the code caught it and raised a misleading HTTP 404 "Items not found" error. This hid the real cause (database failure) from users and monitoring systems.

### 2. Fix

**Changed the exception handler** to return HTTP 500 with the actual error message:

```python
# FIXED CODE:
except Exception as exc:
    logger.error(
        "items_list_failed",
        extra={"event": "items_list_failed", "error": str(exc)},
    )
    # Re-raise as 500 Internal Server Error to indicate backend failure
    # rather than misleading 404 which suggests items don't exist
    raise HTTPException(
        status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
        detail=f"Database error: {str(exc)}",
    ) from exc
```

### 3. Post-fix failure check

**Agent response after redeploy (with PostgreSQL still stopped):**

> "The LMS backend is currently unhealthy (HTTP 500 error). Let me check the logs to see what's causing the issue.
>
> Unfortunately, the LMS backend is currently experiencing technical difficulties. Here's what I found:
>
> - **LMS Backend Status**: Unhealthy (HTTP 500 Internal Server Error)
> - **Available Labs**: Cannot retrieve - the backend is not responding
> - **Sync Pipeline**: Also failing with HTTP 500 error
>
> The backend service appears to be down entirely. This could be due to:
>
> - Database connectivity issues
> - Service crash or restart in progress
> - Configuration problems"

**Key improvement:** The agent now correctly reports HTTP 500 Internal Server Error with database error details, instead of the misleading "Items not found" 404.

### 4. Healthy follow-up (after PostgreSQL restarted)

**Agent response after PostgreSQL was restarted:**

> "Here are the available labs:
>
> | # | Lab ID | Title |
> |---|--------|-------|
> | 1 | lab-01 | Lab 01 – Products, Architecture & Roles |
> | 2 | lab-02 | Lab 02 — Run, Fix, and Deploy a Backend Service |
> | 3 | lab-03 | Lab 03 — Backend API: Explore, Debug, Implement, Deploy |
> | 4 | lab-04 | Lab 04 — Testing, Front-end, and AI Agents |
> | 5 | lab-05 | Lab 05 — Data Pipeline and Analytics Dashboard |
> | 6 | lab-06 | Lab 06 — Build Your Own Agent |
> | 7 | lab-07 | Lab 07 — Build a Client with an AI Coding Agent |
> | 8 | lab-08 | lab-08 |
>
> Let me know if you'd like to see details for any specific lab!"

**System is now healthy and fully functional.**
