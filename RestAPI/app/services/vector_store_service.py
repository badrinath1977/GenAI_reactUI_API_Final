# import os
# from langchain_community.vectorstores import FAISS
# from app.core.config import settings


# class VectorStoreService:

#     def __init__(self, embeddings):
#         self.embeddings = embeddings

#     def _get_department_path(self, department: str):
#         base_path = settings.VECTOR_DB_PATH
#         dept_path = os.path.join(base_path, department)
#         os.makedirs(dept_path, exist_ok=True)
#         return dept_path

#     def save(self, docs, department: str):
#         dept_path = self._get_department_path(department)
#         db = FAISS.from_documents(docs, self.embeddings)
#         db.save_local(dept_path)

#     def load(self, department: str):
#         dept_path = self._get_department_path(department)
#         if not os.path.exists(dept_path):
#             raise Exception(f"No vector DB found for department: {department}")
#         return FAISS.load_local(dept_path, self.embeddings)


import os
from langchain.vectorstores import FAISS
from app.core.config import settings
from app.services.embedding_factory import get_embeddings


class VectorStoreService:

    def __init__(self, department: str):
        self.department = department

        # Create department specific vector path
        self.vector_path = os.path.join(settings.VECTOR_DB_PATH, department)

        os.makedirs(self.vector_path, exist_ok=True)

        self.embeddings = get_embeddings()

        if os.path.exists(os.path.join(self.vector_path, "index.faiss")):
            self.db = FAISS.load_local(
                self.vector_path,
                self.embeddings,
                allow_dangerous_deserialization=True
            )
        else:
            self.db = None

    def add_documents(self, documents):
        if self.db:
            self.db.add_documents(documents)
        else:
            self.db = FAISS.from_documents(documents, self.embeddings)

        self.db.save_local(self.vector_path)

    def similarity_search(self, query: str, k: int = 3):
        if not self.db:
            return []

        return self.db.similarity_search(query, k=k)
