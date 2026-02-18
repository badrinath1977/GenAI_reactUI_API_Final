from pydantic_settings import BaseSettings


class Settings(BaseSettings):

    # Application
    APP_NAME: str
    APP_ENV: str
    APP_PORT: int
    LOG_LEVEL: str

    # JWT
    JWT_SECRET: str
    JWT_HEADER_NAME: str
    JWT_ALGORITHM: str
    JWT_EXPIRATION_MINUTES: int

    # Database
    DB_DRIVER: str
    DB_SERVER: str
    DB_DATABASE: str
    DB_TRUSTED_CONNECTION: str

    # OpenAI
    OPENAI_API_KEY: str
    LLM_MODEL_NAME: str
    EMBEDDING_MODEL_NAME: str

    # Vector DB
    VECTOR_DB_PATH: str
    VECTOR_PER_DEPARTMENT: bool

    # File Storage
    UPLOAD_FOLDER: str
    MAX_FILE_SIZE_MB: int

    # CORS
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
