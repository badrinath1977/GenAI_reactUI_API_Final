import os
from langchain_community.vectorstores import FAISS
from app.services.embedding_factory import get_embeddings
from app.core.config import settings


class VectorStoreService:

    def __init__(self, department: str):

        self.department = department
        self.embeddings = get_embeddings()

        if settings.VECTOR_PER_DEPARTMENT:
            self.vector_path = os.path.join(settings.VECTOR_DB_PATH, department)
        else:
            self.vector_path = settings.VECTOR_DB_PATH

        os.makedirs(self.vector_path, exist_ok=True)

        if os.path.exists(os.path.join(self.vector_path, "index.faiss")):
            self.vectorstore = FAISS.load_local(
                self.vector_path,
                self.embeddings,
                allow_dangerous_deserialization=True
            )
        else:
            self.vectorstore = None

    # Add documents and persist
    def add_documents(self, documents):

        if self.vectorstore:
            self.vectorstore.add_documents(documents)
        else:
            self.vectorstore = FAISS.from_documents(
                documents,
                self.embeddings
            )

        self.vectorstore.save_local(self.vector_path)

    def get_retriever(self):

        if not self.vectorstore:
            raise Exception("Vector store empty. Upload documents first.")

        return self.vectorstore.as_retriever(search_kwargs={"k": 4})
