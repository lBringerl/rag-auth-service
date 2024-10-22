from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    """Settings for the app."""

    MAIN_HOST: str = "0.0.0.0"
    MAIN_POR: int = 8000

    class Config:
        env_file = ".env"
