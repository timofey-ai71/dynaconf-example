# Dynaconf example

- Default config is `src/dynaconf_example/config/settings.toml`
- Config is type-annotated with schemas `src/dynaconf_example/config/schemas`
  - If necessary, validations for config values are added to schemas
- If any config value is missing, application won't start showing pydantic validation error
- Config could be overridden by:
  - `settings.toml` in current working dir (so user can store their local config in repo root)
  - Environment variables
  - `.env` file in current working dir

## Running locally in console

Secrets are passed directly from environment

Dynaconf environment variable names:

```bash
APP_ENV=local KMS_DATABASE__PASSWORD=env_password uv run src/dynaconf_example/app.py
```

Aliased old environment variable names:

```bash
APP_ENV=local DBS_PASSWORD=aliased_env_password uv run src/dynaconf_example/app.py
```

## Running locally with `.env`

Secrets are automatically sourced from `.env`, database config is sourced from `settings.toml`
in project root.

```bash
uv run src/dynaconf_example/app.py
```

## Building docker image

```bash
docker build . -t dynaconf
```

## Running locally within docker

```bash
docker run --rm \
  -e APP_ENV=local \
  -e DBS_PASSWORD=docker_env_password \
  dynaconf
```

## Running on dev/stg/prod within docker

```bash
docker run --rm \
  -e APP_ENV=development \
  -e DBS_PASSWORD=dev_db_password \
  dynaconf
```
