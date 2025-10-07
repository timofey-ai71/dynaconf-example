"""Typed schema for the database configuration."""

from pydantic import BaseModel


class DatabaseConfig(BaseModel):
    """Database configuration."""

    USER: str
    PASSWORD: str
    HOST: str
    PORT: int
    DB: str
    SCHEMAS: list[str]
