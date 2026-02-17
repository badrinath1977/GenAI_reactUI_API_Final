import os
from langchain_community.vectorstores import FAISS
from app.services.embedding_factory import get_embeddings
from app.core.config import settings


# Global cache per department
_vector_cache = {}


class VectorStoreService:

    def __init__(self, department: str):

        self.department = department

        if department in _vector_cache:
            self.vectorstore = _vector_cache[department]
            return

        embeddings = get_embeddings()

        if settings.VECTOR_PER_DEPARTMENT:
            vector_path = os.path.join(settings.VECTOR_DB_PATH, department)
        else:
            vector_path = settings.VECTOR_DB_PATH

        if not os.path.exists(vector_path):
            raise Exception(f"Vector store not found for department: {department}")

        self.vectorstore = FAISS.load_local(
            vector_path,
            embeddings,
            allow_dangerous_deserialization=True
        )

        _vector_cache[department] = self.vectorstore

    def get_retriever(self):
        return self.vectorstore.as_retriever(search_kwargs={"k": 4})
