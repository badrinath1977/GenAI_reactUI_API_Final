from app.core.config import settings

def get_embeddings():
    provider = settings.EMBEDDING_PROVIDER.lower()

    if provider == "local":
        from langchain_huggingface import HuggingFaceEmbeddings
        return HuggingFaceEmbeddings(model_name=settings.EMBEDDING_MODEL_NAME)

    elif provider == "openai":
        from langchain_openai import OpenAIEmbeddings
        return OpenAIEmbeddings(
            api_key=settings.OPENAI_API_KEY,
            model=settings.EMBEDDING_MODEL_NAME
        )

    else:
        raise ValueError(f"Unsupported EMBEDDING_PROVIDER: {provider}")
