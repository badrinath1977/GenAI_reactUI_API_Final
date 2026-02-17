from app.core.config import settings


def get_llm(provider: str = None, model_name: str = None):

    provider = (provider or settings.LLM_PROVIDER).lower()
    model_name = model_name or settings.LLM_MODEL_NAME

    # ===============================
    # OPENAI
    # ===============================
    if provider == "openai":
        from langchain_openai import ChatOpenAI

        return ChatOpenAI(
            api_key=settings.OPENAI_API_KEY,
            model=model_name,
            temperature=0
        )

    # ===============================
    # AZURE / COPILOT
    # ===============================
    elif provider in ["azure", "copilot"]:
        from langchain_openai import AzureChatOpenAI

        return AzureChatOpenAI(
            azure_endpoint=settings.AZURE_ENDPOINT,
            api_key=settings.AZURE_KEY,
            deployment_name=model_name,
            temperature=0
        )

    # ===============================
    # OLLAMA (Best for CPU)
    # ===============================
    elif provider == "ollama":
        from langchain_community.chat_models import ChatOllama

        return ChatOllama(
            base_url=settings.OLLAMA_BASE_URL,
            model=model_name,
            temperature=0
        )

    # ===============================
    # HUGGINGFACE CLOUD (FREE)
    # ===============================
    elif provider == "huggingface":
        from langchain_huggingface import HuggingFaceEndpoint

        return HuggingFaceEndpoint(
            repo_id=model_name,
            huggingfacehub_api_token=settings.HF_API_TOKEN,
            temperature=0.2,
            max_new_tokens=512
        )

    # ===============================
    # LOCAL HUGGINGFACE
    # ===============================
    elif provider == "hf-local":
        from langchain_huggingface import HuggingFacePipeline
        from transformers import pipeline

        pipe = pipeline(
            "text-generation",
            model=model_name,
            device_map="auto",
            max_new_tokens=512
        )

        return HuggingFacePipeline(pipeline=pipe)

    else:
        raise ValueError(f"Unsupported LLM provider: {provider}")
