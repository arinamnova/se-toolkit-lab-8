#!/usr/bin/env python3
"""Resolve environment variables into nanobot config and launch the gateway."""

import json
import os
from pathlib import Path


def resolve_config():
    """Read config.json, override with env vars, write config.resolved.json."""
    config_dir = Path(__file__).parent
    config_path = config_dir / "config.json"
    resolved_path = config_dir / "config.resolved.json"
    workspace_dir = config_dir / "workspace"

    # Load base config
    with open(config_path) as f:
        config = json.load(f)

    # Override LLM provider settings from env vars
    llm_api_key = os.environ.get("LLM_API_KEY")
    llm_api_base = os.environ.get("LLM_API_BASE_URL")
    llm_api_model = os.environ.get("LLM_API_MODEL")

    if llm_api_key:
        config["providers"]["custom"]["apiKey"] = llm_api_key
    if llm_api_base:
        config["providers"]["custom"]["apiBase"] = llm_api_base
    if llm_api_model:
        config["agents"]["defaults"]["model"] = llm_api_model

    # Override gateway settings
    gateway_host = os.environ.get("NANOBOT_GATEWAY_CONTAINER_ADDRESS")
    gateway_port = os.environ.get("NANOBOT_GATEWAY_CONTAINER_PORT")

    if "gateway" not in config:
        config["gateway"] = {}
    if gateway_host:
        config["gateway"]["host"] = gateway_host
    if gateway_port:
        config["gateway"]["port"] = int(gateway_port)

    # Configure MCP servers from env vars
    if "tools" not in config:
        config["tools"] = {"mcpServers": {}}
    if "mcpServers" not in config["tools"]:
        config["tools"]["mcpServers"] = {}

    # LMS MCP server
    lms_backend_url = os.environ.get("NANOBOT_LMS_BACKEND_URL")
    lms_api_key = os.environ.get("NANOBOT_LMS_API_KEY")

    if lms_backend_url or lms_api_key:
        config["tools"]["mcpServers"]["lms"] = {
            "command": "python",
            "args": ["-m", "mcp_lms"],
        }
        env = {}
        if lms_backend_url:
            env["NANOBOT_LMS_BACKEND_URL"] = lms_backend_url
        if lms_api_key:
            env["NANOBOT_LMS_API_KEY"] = lms_api_key
        if env:
            config["tools"]["mcpServers"]["lms"]["env"] = env

    # Webchat MCP server
    webchat_ui_relay_url = os.environ.get("NANOBOT_WEBCHAT_UI_RELAY_URL")
    webchat_ui_token = os.environ.get("NANOBOT_WEBCHAT_UI_TOKEN")

    if webchat_ui_relay_url or webchat_ui_token:
        config["tools"]["mcpServers"]["webchat"] = {
            "command": "python",
            "args": ["-m", "mcp_webchat"],
        }
        env = {}
        if webchat_ui_relay_url:
            env["NANOBOT_WEBCHAT_UI_RELAY_URL"] = webchat_ui_relay_url
        if webchat_ui_token:
            env["NANOBOT_WEBCHAT_UI_TOKEN"] = webchat_ui_token
        if env:
            config["tools"]["mcpServers"]["webchat"]["env"] = env

    # Observability MCP server
    victorialogs_url = os.environ.get("NANOBOT_VICTORIALOGS_URL")
    victoriatraces_url = os.environ.get("NANOBOT_VICTORIATRACES_URL")

    if victorialogs_url or victoriatraces_url:
        if "tools" not in config:
            config["tools"] = {"mcpServers": {}}
        if "mcpServers" not in config["tools"]:
            config["tools"]["mcpServers"] = {}
        config["tools"]["mcpServers"]["obs"] = {
            "command": "python",
            "args": ["-m", "mcp_obs"],
        }
        env = {}
        if victorialogs_url:
            env["NANOBOT_VICTORIALOGS_URL"] = victorialogs_url
        if victoriatraces_url:
            env["NANOBOT_VICTORIATRACES_URL"] = victoriatraces_url
        if env:
            config["tools"]["mcpServers"]["obs"]["env"] = env

    # Webchat channel settings
    webchat_host = os.environ.get("NANOBOT_WEBCHAT_CONTAINER_ADDRESS")
    webchat_port = os.environ.get("NANOBOT_WEBCHAT_CONTAINER_PORT")
    nanobot_access_key = os.environ.get("NANOBOT_ACCESS_KEY")

    if webchat_host or webchat_port:
        if "channels" not in config:
            config["channels"] = {}
        config["channels"]["webchat"] = {
            "enabled": True,
            "host": webchat_host or "0.0.0.0",
            "port": int(webchat_port) if webchat_port else 8765,
        }
        if nanobot_access_key:
            config["channels"]["webchat"]["accessKey"] = nanobot_access_key

    # Write resolved config
    with open(resolved_path, "w") as f:
        json.dump(config, f, indent=2)

    return str(resolved_path), str(workspace_dir)


def main():
    resolved_config, workspace = resolve_config()

    # Launch nanobot gateway
    os.execvp(
        "nanobot",
        [
            "nanobot",
            "gateway",
            "--config",
            resolved_config,
            "--workspace",
            workspace,
        ],
    )


if __name__ == "__main__":
    main()
