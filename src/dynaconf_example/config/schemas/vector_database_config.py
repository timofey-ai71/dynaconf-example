"""Typed schema for the vector database configuration."""

from pydantic import BaseModel


class VectorDatabaseConfig(BaseModel):
    """Vector database configuration."""

    RETRY_ATTEMPTS: int
    RETRY_WAIT_TIME: int
    INIT_TIMEOUT_SEC: int
    QUERY_TIMEOUT_SEC: int
