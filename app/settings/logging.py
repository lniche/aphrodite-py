from pydantic_settings import BaseSettings
from app.settings.config import settings as app_settings

"""
Configuration reference loguru
"""


class Settings(BaseSettings):
    LOG_LEVEL: str = "INFO"
    LOG_PATH: str = app_settings.BASE_PATH + \
        "/../storage/logs/server-{time:YYYY-MM-DD}.log"
    LOG_RETENTION: str = "14 days"

    class Config:
        env_file = "config/.env"
        env_file_encoding = 'utf-8'
        extra = "allow"


settings = Settings()
