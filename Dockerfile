FROM python:3.12 AS builder

WORKDIR /app

RUN pip install uv

ENV UV_CACHE_DIR=/tmp/uv_cache \
    UV_COMPILE_BYTECODE=1

COPY pyproject.toml uv.lock ./

RUN --mount=type=cache,target=$UV_CACHE_DIR \
    uv sync \
        --no-dev \
        --no-install-workspace \
        --frozen \
        --color never


FROM python:3.12-slim AS runtime

WORKDIR /app

ENV PYTHONUNBUFFERED=1 \
    PYTHONPATH=/app/src \
    VIRTUAL_ENV=/app/.venv \
    PATH="/app/.venv/bin:$PATH"

# Transfer dependencies from builder image
COPY --from=builder ${VIRTUAL_ENV} ${VIRTUAL_ENV}

COPY src ./src

CMD ["python3", "src/dynaconf_example/app.py"]
