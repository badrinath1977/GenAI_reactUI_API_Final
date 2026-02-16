
from langchain_community.chat_models import ChatOllama
from app.core.config import settings

class OllamaLLM:

    def __init__(self):
        self.model = ChatOllama(model=settings.LLM_MODEL_NAME)

    def generate(self, prompt: str):
        return self.model.invoke(prompt).content
