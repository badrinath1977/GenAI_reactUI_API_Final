genai_engine/
│
├── api/
│   ├── middleware/
│   │   ├── request_context.py
│   │   └── exception_handler.py
│   ├── routes/
│   │   ├── upload_routes.py
│   │   ├── query_routes.py
│   │   └── admin_routes.py
│   └── app.py
│
├── core/
│   ├── config.py
│   ├── logger.py
│   ├── tracing.py
│   └── constants.py
│
├── services/
│   ├── file_service.py
│   ├── ingestion_service.py
│   ├── vector_store_service.py
│   ├── rag_service.py
│   └── hash_service.py
│
├── repository/
│   ├── file_repository.py
│   ├── error_log_repository.py
│   └── vector_mapping_repository.py
│
├── logging/
│   └── logs/
│       ├── application.log
│       ├── error.log
│       └── vector.log
│
├── background_jobs/
│   └── cleanup_vectors.py
│
└── requirements.txt




enterprise_genai/
│
├── api/
│   ├── app.py
│   │
│   ├── routes/
│   │   ├── upload_routes.py
│   │   ├── query_routes.py
│   │   ├── admin_routes.py
│   │   └── health_routes.py
│   │
│   └── middleware/
│       ├── request_context.py
│       └── exception_handler.py
│
├── core/
│   ├── config.py
│   ├── logger.py
│   ├── database.py
│   ├── tracing.py
│   └── constants.py
│
├── services/
│   ├── file_service.py
│   ├── hash_service.py
│   ├── ingestion_service.py
│   ├── vector_store_service.py
│   ├── rag_service.py
│   └── prompt_service.py
│
├── repository/
│   ├── file_repository.py
│   ├── error_log_repository.py
│   ├── prompt_log_repository.py
│   └── config_repository.py
│
├── vector_store/
│   ├── qdrant_client.py
│   └── collection_manager.py
│
├── models/
│   ├── file_model.py
│   ├── query_model.py
│   └── response_model.py
│
├── utils/
│   ├── file_loader.py
│   ├── chunking.py
│   ├── encryption.py
│   └── helpers.py
│
├── background_jobs/
│   └── vector_cleanup_job.py
│
├── logging/
│   └── logs/
│       ├── application.log
│       ├── error.log
│       └── vector.log
│
├── tests/
│   ├── test_upload.py
│   ├── test_rag.py
│   ├── test_replace.py
│   └── test_sp_calls.py
│
├── .env
├── requirements.txt
└── README.md
