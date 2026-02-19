User Uploads File
        │
        ▼
Generate SHA256 Hash
        │
        ▼
Check SQL for ContentHash
        │
 ┌──────┴─────────────┐
 │                    │
Hash Exists?        Hash Not Exists
 │                    │
 ▼                    ▼
Prompt User        Check Same FileName?
(Skip or Reuse)       │
                      ▼
             Same Name + Diff Hash?
                      │
          ┌───────────┴───────────┐
          │                       │
        Yes                      No
          │                       │
          ▼                       ▼
Ask Replace?                New Upload
          │
          ▼
Mark Old Inactive (SQL)
Delete Vectors by file_id
Insert New Metadata
Generate Embeddings
Store in Vector DB





# QUERY RAG FLOW 

User Question
      │
      ▼
RAG Service
      │
      ▼
Retriever (Filter is_active=True)
      │
      ▼
Relevant Chunks
      │
      ▼
LLM
      │
      ▼
Response
