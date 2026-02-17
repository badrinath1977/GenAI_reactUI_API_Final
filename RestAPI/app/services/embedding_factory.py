from app.core.config import settings

# Global cache
_embedding_instance = None


def get_embeddings():
    global _embedding_instance

    if _embedding_instance is not None:
        return _embedding_instance

    provider = settings.EMBEDDING_PROVIDER.lower()

    # --------------------------
    # OpenAI Embeddings
    # --------------------------
    if provider == "openai":
        from langchain_openai import OpenAIEmbeddings

        _embedding_instance = OpenAIEmbeddings(
            api_key=settings.OPENAI_API_KEY,
            model=settings.EMBEDDING_MODEL_NAME
        )

    # --------------------------
    # Local HuggingFace
    # --------------------------
    elif provider in ["local", "huggingface"]:
        from langchain_huggingface import HuggingFaceEmbeddings

        _embedding_instance = HuggingFaceEmbeddings(
            model_name=settings.EMBEDDING_MODEL_NAME
        )

    # --------------------------
    # Ollama Embeddings
    # --------------------------
    elif provider == "ollama":
        from langchain_community.embeddings import OllamaEmbeddings

        _embedding_instance = OllamaEmbeddings(
            model=settings.EMBEDDING_MODEL_NAME,
            base_url=settings.OLLAMA_BASE_URL
        )

    else:
        raise ValueError(f"Unsupported embedding provider: {provider}")

    return _embedding_instance
