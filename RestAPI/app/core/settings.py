import os
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    # -------------------------------
    # DATABASE
    # -------------------------------
    DB_DRIVER: str = "ODBC Driver 17 for SQL Server"
    DB_SERVER: str = "localhost\\SQLEXPRESS"
    DB_NAME: str = "GenAI"
    DB_TRUSTED_CONNECTION: str = "yes"

    # -------------------------------
    # JWT CONFIG
    # -------------------------------
    JWT_SECRET_KEY: str = "HardcodedForNowChangeLater"
    JWT_ALGORITHM: str = "HS256"

    # -------------------------------
    # VECTOR DB LOCATION
    # -------------------------------
    VECTOR_DB_PATH: str = "./vectorstore"

    class Config:
        env_file = ".env"
        extra = "ignore"

    @property
    def DB_CONNECTION_STRING(self) -> str:
        return (
            f"Driver={{{self.DB_DRIVER}}};"
            f"Server={self.DB_SERVER};"
            f"Database={self.DB_NAME};"
            f"Trusted_Connection={self.DB_TRUSTED_CONNECTION};"
        )


settings = Settings()
