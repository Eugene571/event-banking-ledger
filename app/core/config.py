from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    # FastAPI / serv
    app_host: str = "0.0.0.0"
    app_port: int = 8000
    app_reload: bool = True

    database_url: str = "postgresql+asyncpg://ledger_user:secret123@localhost:5433/ledger_dev"

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        case_sensitive=False,
        extra="ignore",
    )


settings = Settings()
