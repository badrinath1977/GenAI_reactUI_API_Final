
from pydantic_settings import BaseSettings
from pydantic import Field
from enum import Enum

class LLMProvider(str, Enum):
    OPENAI = "openai"
    AZURE = "azure"
    OLLAMA = "ollama"
    HUGGINGFACE = "huggingface"
    COPILOT = "copilot"

class EmbeddingProvider(str, Enum):
    OPENAI = "openai"
    LOCAL = "local"

class Settings(BaseSettings):

    # JWT
    JWT_SECRET: str
    JWT_HEADER_NAME: str = "X-API-KEY"

    # Database
    DB_SERVER: str
    DB_DATABASE: str
    DB_DRIVER: str = "ODBC Driver 17 for SQL Server"

    # LLM
    LLM_PROVIDER: LLMProvider
    LLM_MODEL_NAME: str
    OPENAI_API_KEY: str | None = None
    AZURE_ENDPOINT: str | None = None
    AZURE_KEY: str | None = None
    OLLAMA_BASE_URL: str | None = None
    HF_MODEL_NAME: str | None = None

    # Embedding
    EMBEDDING_PROVIDER: EmbeddingProvider
    EMBEDDING_MODEL_NAME: str

    # Vector DB
    VECTOR_DB_PATH: str

    class Config:
        env_file = ".env"

settings = Settings()
