from langchain_core.embeddings import Embeddings
from sentence_transformers import SentenceTransformer


class LocalMiniLMEmbeddings(Embeddings):

    def __init__(self):
        self.model = SentenceTransformer("sentence-transformers/all-MiniLM-L6-v2")

    def embed_documents(self, texts):
        return self.model.encode(texts).tolist()

    def embed_query(self, text):
        return self.model.encode([text])[0].tolist()


_embedding_instance = None


def get_embeddings():
    global _embedding_instance

    if _embedding_instance is None:
        _embedding_instance = LocalMiniLMEmbeddings()

    return _embedding_instance
