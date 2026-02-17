from pydantic_settings import BaseSettings
from typing import Optional


class Settings(BaseSettings):

    # ============================================
    # APPLICATION
    # ============================================
    APP_NAME: str
    APP_ENV: str
    APP_PORT: int
    LOG_LEVEL: str

    # ============================================
    # JWT
    # ============================================
    JWT_SECRET: str
    JWT_HEADER_NAME: str
    JWT_ALGORITHM: str
    JWT_EXPIRATION_MINUTES: int

    # ============================================
    # DATABASE
    # ============================================
    DB_DRIVER: str
    DB_SERVER: str
    DB_DATABASE: str
    DB_TRUSTED_CONNECTION: str

    # ============================================
    # LLM
    # ============================================
    LLM_PROVIDER: str
    LLM_MODEL_NAME: str

    OPENAI_API_KEY: Optional[str] = None
    AZURE_ENDPOINT: Optional[str] = None
    AZURE_KEY: Optional[str] = None
    OLLAMA_BASE_URL: Optional[str] = None
    HF_API_TOKEN: Optional[str] = None

    # ============================================
    # EMBEDDING
    # ============================================
    EMBEDDING_PROVIDER: str
    EMBEDDING_MODEL_NAME: str

    # ============================================
    # VECTOR DATABASE
    # ============================================
    VECTOR_DB_PATH: str
    VECTOR_PER_DEPARTMENT: bool

    # ============================================
    # FILE STORAGE
    # ============================================
    UPLOAD_FOLDER: str
    MAX_FILE_SIZE_MB: int

    # ============================================
    # MASKING
    # ============================================
    ENABLE_MASKING: bool
    MASK_CHAR: str
    MASK_EMAIL: bool
    MASK_PHONE: bool
    MASK_SSN: bool

    # ============================================
    # CORS
    # ============================================
    CORS_ALLOW_ORIGINS: str
    CORS_ALLOW_METHODS: str
    CORS_ALLOW_HEADERS: str

    class Config:
        env_file = ".env"
        extra = "ignore"

    @property
    def DB_CONNECTION_STRING(self) -> str:
        return (
            f"Driver={{{self.DB_DRIVER}}};"
            f"Server={self.DB_SERVER};"
            f"Database={self.DB_DATABASE};"
            f"Trusted_Connection={self.DB_TRUSTED_CONNECTION};"
        )


settings = Settings()
