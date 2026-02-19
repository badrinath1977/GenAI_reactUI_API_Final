import os
from dotenv import load_dotenv

load_dotenv()

class Settings:
    DB_DRIVER = os.getenv("DB_DRIVER")
    DB_SERVER = os.getenv("DB_SERVER")
    DB_DATABASE = os.getenv("DB_DATABASE")
    DB_TRUSTED_CONNECTION = os.getenv("DB_TRUSTED_CONNECTION")
    VECTOR_DB_PATH = os.getenv("VECTOR_DB_PATH")
    UPLOAD_FOLDER = os.getenv("UPLOAD_FOLDER")
    OPENAI_PROVIDER_NAME = os.getenv("OPENAI_PROVIDER_NAME")

settings = Settings()
