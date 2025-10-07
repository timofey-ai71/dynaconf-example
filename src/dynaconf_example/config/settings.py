"""Configuration settings for KMS."""

from pathlib import Path

# Waiting for typed.Dynaconf to be released in technical preview
from dynaconf import Dynaconf  # type: ignore[import-untyped]

from dynaconf_example.config.env_alias_loader import load_aliases
from dynaconf_example.config.schemas.app_config import AppConfig

SETTINGS_FILE_NAME = "settings.toml"

dynaconf_instance = Dynaconf(
    envvar_prefix="KMS",
    settings_files=[
        Path(__file__).parent / SETTINGS_FILE_NAME,
        Path.cwd() / SETTINGS_FILE_NAME,
    ],
    environments=True,
    load_dotenv=True,
    merge_enabled=True,
    env_switcher="APP_ENV",
    schema=AppConfig,
)
load_aliases(dynaconf_instance)

config: AppConfig = AppConfig.model_validate(
    # Waiting for typed.Dynaconf to be released in technical preview
    dynaconf_instance.as_dict(),  # type: ignore[no-untyped-call]
)
