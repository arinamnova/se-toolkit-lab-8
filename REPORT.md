# Lab 8 — Report

Paste your checkpoint evidence below. Add screenshots as image files in the repo and reference them with `![description](path)`.

## Task 1A — Bare agent

**Question 1: "What is the agentic loop?"**

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

<!-- Paste a short nanobot startup log excerpt showing the gateway started inside Docker -->

## Task 2B — Web client

<!-- Screenshot of a conversation with the agent in the Flutter web app -->

## Task 3A — Structured logging

<!-- Paste happy-path and error-path log excerpts, VictoriaLogs query screenshot -->

## Task 3B — Traces

<!-- Screenshots: healthy trace span hierarchy, error trace -->

## Task 3C — Observability MCP tools

<!-- Paste agent responses to "any errors in the last hour?" under normal and failure conditions -->

## Task 4A — Multi-step investigation

<!-- Paste the agent's response to "What went wrong?" showing chained log + trace investigation -->

## Task 4B — Proactive health check

<!-- Screenshot or transcript of the proactive health report that appears in the Flutter chat -->

## Task 4C — Bug fix and recovery

<!-- 1. Root cause identified
     2. Code fix (diff or description)
     3. Post-fix response to "What went wrong?" showing the real underlying failure
     4. Healthy follow-up report or transcript after recovery -->
