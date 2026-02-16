app/
│
├── main.py
│
├── api/
│   ├── __init__.py
│   ├── chat_routes.py
│   └── upload_routes.py
│
├── services/
│   ├── __init__.py
│   ├── embedding_service.py
│   ├── llm_service.py
│   └── vector_store_service.py
│
├── ingestion/
│   ├── __init__.py
│   └── document_ingestor.py
│
├── repository/
│   ├── __init__.py
│   ├── file_repository.py
│   ├── error_repository.py
│   └── prompt_repository.py
│
└── core/
    ├── __init__.py
    └── config.py
