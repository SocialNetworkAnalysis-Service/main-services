from typing import Optional
from pydantic_settings import BaseSettings, SettingsConfigDict


class AdminPanelConfig(BaseSettings):
    model_config = SettingsConfigDict(env_file=f"src/.env")

    flask_admin_swatch: str
    basic_auth_username: str
    basic_auth_password: str
    basic_auth_force: bool

    db_name: str
    db_user: str
    db_password: str
    db_host: str
    db_port: int

    @property
    def sync_alchemy_url(self):
        return f'postgresql+psycopg2://{self.db_user}:{self.db_password}@' \
               f'{self.db_host}:{self.db_port}/{self.db_name}'


config = AdminPanelConfig()