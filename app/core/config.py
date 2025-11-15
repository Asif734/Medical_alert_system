from pydantic import BaseSettings

class Settings(BaseSettings):
    DATABASE_URL: str
    API_KEY: str
    ALERT_THRESHOLD: int

    class Config:
        env_file = ".env"

settings = Settings()