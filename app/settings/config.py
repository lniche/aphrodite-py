import os

from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    NAME: str = "aphrodite-py"
    DEBUG: bool = False
    ENV: str = "dev"

    BASE_PATH: str = os.path.dirname(
        os.path.dirname((os.path.abspath(__file__))))

    SERVER_HOST: str = "0.0.0.0"
    SERVER_PORT: int = 8000

    URL: str = "http://127.0.0.1"
    TIME_ZONE: str = "UTC"

    class Config:
        env_prefix = 'APP_'
        env_file = "config/.env"
        env_file_encoding = 'utf-8'
        extra = "allow"


settings = Settings()
