from app.core.config import settings
from langchain_openai import ChatOpenAI
from langchain_community.llms import Ollama


def get_llm():
    provider = settings.LLM_PROVIDER.lower()

    if provider == "openai":
        return ChatOpenAI(
            model=settings.LLM_MODEL_NAME,
            openai_api_key=settings.OPENAI_API_KEY,
            temperature=0
        )

    elif provider == "ollama":
        return Ollama(
            model=settings.LLM_MODEL_NAME
        )

    else:
        raise ValueError(f"Unsupported LLM provider: {provider}")
