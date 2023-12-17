from typing import Optional

from pydantic_settings import BaseSettings, SettingsConfigDict


class APIConfig(BaseSettings):
    model_config = SettingsConfigDict(env_file="src/.env")

    # Constants
    DEBUG: bool = False
    PORT: int = 8000
    HOST: str = "0.0.0.0"
    VERSION: str = "0.0.1"
    LOGGING_LEVEL: str = "info"
    LOGGING_FORMAT: str = "%(asctime)s %(name)s %(levelname)s: %(message)s"

    # Database secrets
    db_name: str
    db_user: str
    db_password: str
    db_host: str
    db_port: int

    # SMS-Agent secrets
    sms_agent_login: str
    sms_agent_password: str
    sms_agent_api_url: str


    # Nats
    NATS_SERVER_URL: str
    TEMP_FILES_BUCKET: str = "temp_files"

    @property
    def sync_alchemy_url(self):
        return (
            f"postgresql+psycopg2://{self.db_user}:{self.db_password}@"
            f"{self.db_host}:{self.db_port}/{self.db_name}"
        )

    @property
    def async_alchemy_url(self):
        return (
            f"postgresql+asyncpg://{self.db_user}:{self.db_password}@"
            f"{self.db_host}:{self.db_port}/{self.db_name}"
        )


config = APIConfig()
