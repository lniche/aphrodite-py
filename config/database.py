from pydantic import BaseSettings


class Settings(BaseSettings):
    """pgsql db"""
    DB_HOST: str = '127.0.0.1'
    DB_PORT: int = 5432
    DB_DATABASE: str = 'test'
    DB_USER: str = 'postgres'
    DB_PASSWORD: str = '123123'

    class Config:
        env_file = ".env"


class RedisSettings(BaseSettings):
    """redis"""

    REDIS_HOST: str = 'localhost'
    REDIS_PORT: int = 6379
    REDIS_DB: int = 0
    REDIS_PASSWORD: str = None

    class Config:
        env_file = ".env"


settings = Settings()
redis_settings = RedisSettings()
