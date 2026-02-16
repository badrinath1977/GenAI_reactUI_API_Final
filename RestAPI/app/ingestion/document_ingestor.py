import os
from langchain_community.document_loaders import (
    PyPDFLoader,
    TextLoader,
    UnstructuredWordDocumentLoader,
    UnstructuredExcelLoader,
    UnstructuredPowerPointLoader,
    UnstructuredImageLoader,
)

class DocumentIngestor:

    def ingest(self, file_path: str):
        extension = os.path.splitext(file_path)[1].lower()

        if extension == ".pdf":
            loader = PyPDFLoader(file_path)

        elif extension == ".txt":
            loader = TextLoader(file_path)

        elif extension in [".doc", ".docx"]:
            loader = UnstructuredWordDocumentLoader(file_path)

        elif extension in [".xls", ".xlsx"]:
            loader = UnstructuredExcelLoader(file_path)

        elif extension in [".ppt", ".pptx"]:
            loader = UnstructuredPowerPointLoader(file_path)

        elif extension in [".png", ".jpg", ".jpeg"]:
            loader = UnstructuredImageLoader(file_path)

        else:
            raise ValueError(f"Unsupported file type: {extension}")

        return loader.load()
