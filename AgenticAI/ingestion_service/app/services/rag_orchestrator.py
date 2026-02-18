
from app.services.llm.llm_factory import LLMFactory
from app.services.vector_store_service import VectorStoreService

class RAGOrchestrator:

    def __init__(self):
        self.llm = LLMFactory.create()
        self.vector = VectorStoreService()

    def ask(self, question: str):
        context = self.vector.search(question)
        prompt = f"Context: {context}\nQuestion: {question}"
        return self.llm.generate(prompt)
