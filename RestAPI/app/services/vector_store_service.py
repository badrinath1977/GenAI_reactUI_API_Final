import os
from langchain_community.vectorstores import FAISS
from app.core.config import settings
from app.services.embedding_factory import get_embeddings


class VectorStoreService:

    def __init__(self, department: str):
        self.department = department
        self.embeddings = get_embeddings()

        # Create department-specific path
        self.vector_path = os.path.join(settings.VECTOR_DB_PATH, department)

        if not os.path.exists(self.vector_path):
            os.makedirs(self.vector_path, exist_ok=True)

        # Load if exists
        if os.path.exists(os.path.join(self.vector_path, "index.faiss")):
            self.vectorstore = FAISS.load_local(
                self.vector_path,
                self.embeddings,
                allow_dangerous_deserialization=True
            )
        else:
            self.vectorstore = None

    # ---------------------------------------
    # Add documents to vector store
    # ---------------------------------------
    def add_documents(self, documents):
        if self.vectorstore is None:
            self.vectorstore = FAISS.from_documents(
                documents,
                self.embeddings
            )
        else:
            self.vectorstore.add_documents(documents)

        self.vectorstore.save_local(self.vector_path)

    # ---------------------------------------
    # Return retriever (THIS WAS MISSING)
    # ---------------------------------------
    def get_retriever(self, k: int = 4):
        if self.vectorstore is None:
            raise ValueError("Vector store is empty. Upload documents first.")

        return self.vectorstore.as_retriever(search_kwargs={"k": k})

    # ---------------------------------------
    # Direct similarity search (optional)
    # ---------------------------------------
    def similarity_search(self, query: str, k: int = 4):
        if self.vectorstore is None:
            raise ValueError("Vector store is empty. Upload documents first.")

        return self.vectorstore.similarity_search(query, k=k)
