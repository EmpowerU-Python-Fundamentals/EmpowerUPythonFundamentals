from pathlib import Path

from pydantic import BaseModel, Field
from pydantic_settings import BaseSettings, SettingsConfigDict

BASE_DIR = Path(__file__).resolve().parent.parent

ENV_FILE = BASE_DIR / ".env"


class DatabaseSettings(BaseModel):
    driver: str = Field(
        "sqlite+aiosqlite",
        description="Database driver in SQLAlchemy format. Example: 'postgresql+asyncpg', 'sqlite+aiosqlite'",
    )
    host: str = Field(
        "localhost", description="Hostname or IP address of the database server"
    )
    port: int | None = Field(
        None, description="Port number to connect to the database. Optional for SQLite"
    )
    name: str = Field(
        "database.db", description="Name of the database or path to SQLite file"
    )
    username: str | None = Field(
        None, description="Username for database authentication"
    )
    password: str | None = Field(
        None, description="Password for database authentication"
    )


class Settings(BaseSettings):
    token: str = Field(
        description="Bot token can be obtained via https://t.me/BotFather"
    )
    post_interval: int = 10
    database: DatabaseSettings

    model_config = SettingsConfigDict(
        env_file=ENV_FILE,
        env_file_encoding="utf-8",
        env_nested_delimiter="__",
        extra="ignore",
    )


settings = Settings()  # type: ignore
