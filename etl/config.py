from pydantic import PostgresDsn
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    DATABASE_URL: str
    LICHESS_API_TOKEN: str