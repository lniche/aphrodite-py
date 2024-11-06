from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    JWT_TTL: int = 60 * 24 * 8
    JWT_SECRET_KEY: str = ""
    JWT_ALGORITHM: str = 'HS256'

    class Config:
        env_file = "config/.env"
        env_file_encoding = 'utf-8'
        extra = "allow"


settings = Settings()
