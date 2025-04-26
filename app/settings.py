from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8")

    USER_DB: str
    PASSWORD_DB: str
    HOST_DB: str
    PORT_DB: str
    DATABASE_NAME: str


Settings = Settings()  # type: ignore
