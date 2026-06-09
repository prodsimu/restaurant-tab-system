from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    database_url: str
    app_name: str
    debug: bool

    class Config:
        env_file = ".env"


settings = Settings()
