
from app.core.config import settings
from app.core.config import LLMProvider
from app.services.llm.openai_llm import OpenAILLM
from app.services.llm.ollama_llm import OllamaLLM

class LLMFactory:

    @staticmethod
    def create():
        if settings.LLM_PROVIDER == LLMProvider.OPENAI:
            return OpenAILLM()
        if settings.LLM_PROVIDER == LLMProvider.OLLAMA:
            return OllamaLLM()
        raise ValueError("Unsupported LLM Provider")
