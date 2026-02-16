
from langchain_openai import ChatOpenAI
from app.core.config import settings

class OpenAILLM:

    def __init__(self):
        self.model = ChatOpenAI(
            model=settings.LLM_MODEL_NAME,
            api_key=settings.OPENAI_API_KEY
        )

    def generate(self, prompt: str):
        return self.model.invoke(prompt).content
