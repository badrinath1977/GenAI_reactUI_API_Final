from app.core.config import settings


def get_embeddings():
    provider = settings.EMBEDDING_PROVIDER.lower()

    # --------------------------
    # OpenAI Embeddings
    # --------------------------
    if provider == "openai":
        from langchain_openai import OpenAIEmbeddings

        return OpenAIEmbeddings(
            api_key=settings.OPENAI_API_KEY,
            model=settings.EMBEDDING_MODEL_NAME
        )

    # --------------------------
    # Local / HuggingFace
    # --------------------------
    elif provider in ["local", "huggingface"]:
        from langchain_huggingface import HuggingFaceEmbeddings

        return HuggingFaceEmbeddings(
            model_name=settings.EMBEDDING_MODEL_NAME
        )

    # --------------------------
    # Ollama Embeddings
    # --------------------------
    elif provider == "ollama":
        from langchain_community.embeddings import OllamaEmbeddings

        return OllamaEmbeddings(
            model=settings.EMBEDDING_MODEL_NAME
        )

    else:
        raise ValueError(f"Unsupported embedding provider: {provider}")
