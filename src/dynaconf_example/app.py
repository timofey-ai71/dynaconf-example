"""Example application using Dynaconf for configuration."""

import json

from dynaconf_example.config.settings import config


def main() -> None:
    """Main entry point for the example."""
    print(json.dumps(config.model_dump(), indent=2))  # noqa: T201 use print


if __name__ == "__main__":
    main()
