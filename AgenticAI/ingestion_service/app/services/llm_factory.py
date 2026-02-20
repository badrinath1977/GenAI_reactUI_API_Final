# app/services/llm_factory.py

from langchain_openai import ChatOpenAI
from app.core.config import settings

_llm_instance = None


def get_llm() -> ChatOpenAI:
    global _llm_instance

    if _llm_instance is None:
        _llm_instance = ChatOpenAI(
            model=settings.OPENAI_MODEL,      # e.g. gpt-4o-mini
            api_key=settings.OPENAI_API_KEY,
            temperature=0,
            max_retries=2,
            timeout=30
        )

    return _llm_instance
