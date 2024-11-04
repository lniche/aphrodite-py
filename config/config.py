import os

from pydantic import BaseSettings, Field


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
        env_file = ".env"
        env_file_encoding = 'utf-8'


settings = Settings()
