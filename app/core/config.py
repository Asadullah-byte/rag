from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    PROJECT_NAME: str = "backend-api"
    PREFIX: str = "/api"
    API_VERSION: str = "v1"
    SUPABASE_URL: str
    SUPABASE_KEY: str
    DATABASE_URL: str
    REDIS_URL: str

    @property
    def API_V1_STR(self) -> str:
        return f"{self.PREFIX}/{self.API_VERSION}"

    class Config:
        env_file = ".env"


try:
    settings = Settings()
except Exception as e:
    raise RuntimeError(f"Failed to load settings: {e}") from e
