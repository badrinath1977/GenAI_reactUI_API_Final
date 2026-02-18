
from langchain_community.document_loaders import (
    PyPDFLoader,
    UnstructuredWordDocumentLoader,
    UnstructuredExcelLoader,
    UnstructuredPowerPointLoader,
    TextLoader
)

class DocumentIngestor:

    def ingest(self, file_path: str):
        ext = file_path.split('.')[-1].lower()

        if ext == "pdf":
            loader = PyPDFLoader(file_path)
        elif ext in ["doc", "docx"]:
            loader = UnstructuredWordDocumentLoader(file_path)
        elif ext in ["xls", "xlsx"]:
            loader = UnstructuredExcelLoader(file_path)
        elif ext in ["ppt", "pptx"]:
            loader = UnstructuredPowerPointLoader(file_path)
        elif ext == "txt":
            loader = TextLoader(file_path)
        else:
            raise ValueError("Unsupported file type")

        return loader.load()
