from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    DATABASE_URL: str 
    secret_key: str
    algorithm: str
    class Config:
        env_file = ".env"
        case_sensitive = False

settings = Settings()
