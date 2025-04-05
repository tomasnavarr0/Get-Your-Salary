from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """
    Clase para cargar configuraciones desde variables de entorno utilizando Pydantic.
    """

    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8")

    # OPEN_AI_API_KEY: str


Settings = Settings()  # type: ignore
