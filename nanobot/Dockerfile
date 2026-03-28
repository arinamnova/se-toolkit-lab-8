# syntax=docker/dockerfile:1

# Stage 1: Build dependencies with uv
FROM harbor.pg.innopolis.university/docker-hub-cache/astral/uv:python3.14-bookworm-slim AS builder

WORKDIR /app

# Copy workspace-level dependency files first (from workspace context)
COPY --from=workspace pyproject.toml uv.lock ./

# Copy all workspace packages needed for uv sync
COPY --from=workspace backend/ backend/
COPY --from=workspace mcp/ mcp/
COPY --from=workspace qwen-code-api/ qwen-code-api/
COPY --from=workspace nanobot/ nanobot/
COPY --from=workspace nanobot-websocket-channel/ nanobot-websocket-channel/

# Sync all dependencies from workspace root
RUN --mount=type=cache,target=/root/.cache/uv \
    uv sync --frozen

# Stage 2: Runtime image
FROM harbor.pg.innopolis.university/docker-hub-cache/python:3.14.2-slim-bookworm AS runtime

# Create non-root user with configurable UID/GID
ARG APP_UID=999
ARG APP_GID=999
RUN groupadd --system --gid "${APP_GID}" nonroot \
    && useradd --system --gid "${APP_GID}" --uid "${APP_UID}" --create-home nonroot

WORKDIR /app

# Copy the built environment from builder
COPY --from=builder --chown=nonroot:nonroot /app /app

# Create directory for Qwen credentials
RUN mkdir -p /home/nonroot/.qwen && chown nonroot:nonroot /home/nonroot/.qwen

# Switch to non-root user
USER nonroot

# Set environment for Python path
ENV PATH="/app/.venv/bin:$PATH"

# Run the entrypoint script
CMD ["python", "/app/nanobot/entrypoint.py"]
