from pydantic import BaseSettings
from typing import Optional
from functools import lru_cache

class Settings(BaseSettings):
    DATABASE_USERNAME : str = 'postgres'
    DATABASE_PASSWORD : str = '123123'
    DATABASE_HOST : str = 'localhost'
    DATABASE_PORT : int = 5432
    DATABASE_NAME : str = 'mydb'

    DATABASE_URI : str = f"postgresql://{DATABASE_USERNAME}:{DATABASE_PASSWORD}@{DATABASE_HOST}:{DATABASE_PORT}/{DATABASE_NAME}"

    class Config:
        case_sensitive : bool = True

@lru_cache
def get_Settings() -> Settings:
    return Settings()


settings = get_Settings()
