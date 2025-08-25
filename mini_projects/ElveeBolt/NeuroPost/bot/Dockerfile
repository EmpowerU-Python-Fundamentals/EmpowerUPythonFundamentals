FROM python:3.12-alpine

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PYTHONPATH=/bot \
    PATH="/root/.local/bin:${PATH}"

# Install uv
RUN apk add --no-cache bash curl && \
    curl -LsSf https://astral.sh/uv/install.sh | bash

WORKDIR /bot

# Install dependencies
RUN --mount=type=cache,target=/root/.cache/uv \
    --mount=type=bind,source=uv.lock,target=uv.lock \
    --mount=type=bind,source=pyproject.toml,target=pyproject.toml \
    uv sync --locked --no-install-project

# Copy the project into the image
COPY . /bot

# Sync the project
RUN --mount=type=cache,target=/root/.cache/uv \
    uv sync --locked
