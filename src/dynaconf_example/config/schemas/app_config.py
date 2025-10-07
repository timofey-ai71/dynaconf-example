"""Typed schema for KMS configuration."""

from pydantic import BaseModel

from dynaconf_example.config.schemas.database_config import DatabaseConfig
from dynaconf_example.config.schemas.vector_database_config import VectorDatabaseConfig


class AppConfig(BaseModel):
    """KMS configuration."""

    APP_NAME: str
    APP_ENVIRONMENT: str
    PRODUCT_NAME: str
    PRODUCT_TYPE: str
    FASTAPI_ROOT_PATH: str
    USER_AGENT: str
    LOG_LEVEL: str
    LOG_DIR: str

    DATABASE: DatabaseConfig
    VECTOR_DATABASE: VectorDatabaseConfig
