from fastapi import APIRouter
from app.core.config import settings
from app.repository.db_connection import get_db_connection
from app.services.llm_factory import get_llm
from app.services.embedding_factory import get_embeddings
import os

router = APIRouter(
    prefix="/health",
    tags=["Health"]
)

@router.get("/")
def health_check():
    health_status = {
        "application": "UP",
        "database": "DOWN",
        "llm_provider": settings.LLM_PROVIDER,
        "llm_status": "DOWN",
        "embedding_provider": settings.EMBEDDING_PROVIDER,
        "embedding_status": "DOWN",
        "vector_db_path": settings.VECTOR_DB_PATH,
        "vector_db_status": "DOWN"
    }

    # ✅ DB Health Check
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT 1")
        cursor.close()
        conn.close()
        health_status["database"] = "UP"
    except Exception as e:
        health_status["database"] = f"ERROR: {str(e)}"

    # ✅ LLM Health Check
    try:
        llm = get_llm()
        health_status["llm_status"] = "CONFIGURED"
    except Exception as e:
        health_status["llm_status"] = f"ERROR: {str(e)}"

    # ✅ Embedding Health Check
    try:
        embeddings = get_embeddings()
        health_status["embedding_status"] = "CONFIGURED"
    except Exception as e:
        health_status["embedding_status"] = f"ERROR: {str(e)}"

    # ✅ Vector DB Folder Check
    try:
        if os.path.exists(settings.VECTOR_DB_PATH):
            health_status["vector_db_status"] = "AVAILABLE"
        else:
            health_status["vector_db_status"] = "NOT FOUND"
    except Exception as e:
        health_status["vector_db_status"] = f"ERROR: {str(e)}"

    return health_status
