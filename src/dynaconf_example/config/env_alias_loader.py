"""Custom Dynaconf loader for environment variable aliasing."""

import os
from typing import Any

ALIASES = {
    "DBS_PASSWORD": "DATABASE.PASSWORD",
}


# Dynaconf loader protocol requires specific signature with **kwargs even though we don't
# use them. Using Any type since Dynaconf lacks type stubs.
def load_aliases(settings: Any, **kwargs: Any) -> None:  # noqa: ARG001, ANN401
    """Maps legacy environment variables to Dynaconf config paths.

    Args:
        settings: The Dynaconf settings instance
        **kwargs: Unused parameters required by Dynaconf loader protocol
    """
    for legacy_var, config_path in ALIASES.items():
        if legacy_var not in os.environ or settings.get(config_path):  # type: ignore[attr-defined]
            continue

        settings.set(config_path, os.environ[legacy_var])  # type: ignore[attr-defined]
