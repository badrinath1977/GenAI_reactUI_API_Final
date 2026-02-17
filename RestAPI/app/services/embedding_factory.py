from app.core.config import settings


def get_embeddings():

    provider = settings.EMBEDDING_PROVIDER.lower()

    # ===============================
    # OPENAI
    # ===============================
    if provider == "openai":
        from langchain_openai import OpenAIEmbeddings

        return OpenAIEmbeddings(
            api_key=settings.OPENAI_API_KEY,
            model=settings.EMBEDDING_MODEL_NAME
        )

    # ===============================
    # LOCAL / HF EMBEDDINGS
    # ===============================
    elif provider in ["local", "huggingface"]:
        from langchain_community.embeddings import HuggingFaceEmbeddings

        return HuggingFaceEmbeddings(
            model_name=settings.EMBEDDING_MODEL_NAME
        )

    # ===============================
    # OLLAMA EMBEDDINGS
    # ===============================
    elif provider == "ollama":
        from langchain_community.embeddings import OllamaEmbeddings

        return OllamaEmbeddings(
            base_url=settings.OLLAMA_BASE_URL,
            model=settings.EMBEDDING_MODEL_NAME
        )

    else:
        raise ValueError(f"Unsupported embedding provider: {provider}")
