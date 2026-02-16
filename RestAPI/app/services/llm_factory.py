from app.core.config import settings
from langchain_openai import ChatOpenAI
from langchain_community.chat_models import ChatOllama


def get_llm(provider: str = None, model_name: str = None):

    selected_provider = (provider or settings.LLM_PROVIDER).lower()
    selected_model = model_name or settings.LLM_MODEL_NAME

    if selected_provider == "openai":
        return ChatOpenAI(
            model=selected_model,
            openai_api_key=settings.OPENAI_API_KEY,
            temperature=0.2
        )

    elif selected_provider == "ollama":
        return ChatOllama(
            model=selected_model,
            temperature=0.2
        )

    else:
        raise Exception(f"Unsupported LLM provider: {selected_provider}")
