from pydantic import BaseModel
from pydantic_settings import BaseSettings
from pydantic_settings import SettingsConfigDict


class DBSettings(BaseModel):
    # DB config match env variables (see docker-compose.yml)
    POSTGRES_HOST: str
    POSTGRES_PORT: int
    POSTGRES_DB: str
    POSTGRES_USER: str
    POSTGRES_PASSWORD: str


class AppSettings(BaseSettings):
    db: DBSettings
    # Pydantic-settings will automatically load these from environment variables
    # or a .env file (if you use one for local development)
    model_config = SettingsConfigDict(
        env_file=".env", extra="ignore", env_nested_delimiter="__"
    )


settings = AppSettings()
