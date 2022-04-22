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
    ACCESS_TOKEN_EXPIRE_MINUTES : int = 60 * 24 * 8  # 60 minutes * 24 hours * 8 days = 8 days
    SECRET_KEY : str = "J9ICKD@QLKF1010'FKfkfkvckoltgñac@493kflqa"
    ALGORITHM : str = "HS512"
    
    class Config:
        case_sensitive : bool = True

@lru_cache
def get_Settings() -> Settings:
    return Settings()


settings = get_Settings()
