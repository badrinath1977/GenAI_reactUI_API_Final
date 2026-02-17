from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import Optional
import traceback

from app.services.llm_factory import get_llm
from app.services.vector_store_service import VectorStoreService
from app.repository.prompt_repository import insert_user_prompt_log
from app.repository.error_repository import insert_error_log
from app.core.logger import logger


router = APIRouter(prefix="/chat", tags=["Chat"])


# ------------------------------------------
# Request Model
# ------------------------------------------

class ChatRequest(BaseModel):
    user_id: str
    question: str
    department: str
    provider: Optional[str] = None
    model_name: Optional[str] = None


# ------------------------------------------
# Chat Endpoint
# ------------------------------------------

@router.post("/")
async def chat(request: ChatRequest):
    """
    Enterprise RAG Chat Endpoint

    Features:
    - Department-based vector isolation
    - Dynamic LLM provider selection
    - Prompt logging
    - Error logging
    """

    try:
        logger.info(f"Chat request from User={request.user_id}")

        # -----------------------------------
        # 1️⃣ Load Department Vector Store
        # -----------------------------------
        vector_service = VectorStoreService(department=request.department)

        retriever = vector_service.get_retriever()

        # -----------------------------------
        # 2️⃣ Retrieve Relevant Documents
        # -----------------------------------
        docs = retriever.invoke(request.question)

        if not docs:
            return {
                "answer": "No relevant information found in the selected department.",
                "department": request.department
            }

        context = "\n\n".join(doc.page_content for doc in docs)

        # -----------------------------------
        # 3️⃣ Get LLM Dynamically
        # -----------------------------------
        from app.core.config import settings
        print("LLM Provider:", request.provider or settings.LLM_PROVIDER)
        print("LLM Model:", request.model_name or settings.LLM_MODEL_NAME)
        print("ENV LLM_PROVIDER:", settings.LLM_PROVIDER)
        print("ENV LLM_MODEL_NAME:", settings.LLM_MODEL_NAME)
        print("REQUEST PROVIDER:", request.provider)
        print("REQUEST MODEL:", request.model_name)
        llm = get_llm(
            provider=request.provider,
            model_name=request.model_name
        )

        # -----------------------------------
        # 4️⃣ Construct RAG Prompt
        # -----------------------------------
        final_prompt = f"""
You are an enterprise AI assistant.

Rules:
- Answer strictly using the provided context.
- If answer is not in the context, say: "Information not available in provided documents."
- Do not hallucinate.

Context:
{context}

Question:
{request.question}
"""

        # -----------------------------------
        # 5️⃣ Invoke LLM
        # -----------------------------------
        response = llm.invoke(final_prompt)

        answer = response.content if hasattr(response, "content") else str(response)

        # -----------------------------------
        # 6️⃣ Log User Prompt
        # -----------------------------------
        insert_user_prompt_log(
            user_id=request.user_id,
            prompt=request.question,
            model_used=request.model_name,
            provider=request.provider
        )

        return {
            "answer": answer.strip(),
            "department": request.department
        }

    except Exception as ex:
        logger.error(f"Chat Error: {str(ex)}")

        insert_error_log(
            user_id=request.user_id if request else None,
            error_type="ChatError",
            error_message=str(ex),
            stack_trace=traceback.format_exc()
        )

        raise HTTPException(status_code=500, detail="Internal Server Error")
