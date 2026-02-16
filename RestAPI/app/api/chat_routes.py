from fastapi import APIRouter, Depends, Header, HTTPException
from pydantic import BaseModel
from typing import Optional
import traceback

from app.services.llm_factory import get_llm
from app.services.vector_store_service import VectorStoreService
from app.repository.prompt_repository import insert_user_prompt_log
from app.repository.error_repository import insert_error_log
from app.core.security import validate_jwt_token
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
# import pdb;pdb.set_trace()
@router.post("/")

async def chat(
   
    request: ChatRequest,
    # authorization: str = Header(...)
):
    """
    Chat Endpoint with:
    - JWT validation
    - Department-based vector store
    - Dynamic LLM selection
    - Prompt logging
    - Error logging
    """

    try:
        # -------------------------------
        # 1️⃣ Validate JWT
        # -------------------------------
        # validate_jwt_token(authorization)

        logger.info(f"Chat request from User={request.user_id}")

        # -------------------------------
        # 2️⃣ Load Vector Store by Department
        # -------------------------------
        vector_service = VectorStoreService(department=request.department)

        retriever = vector_service.get_retriever()

        # -------------------------------
        # 3️⃣ Get LLM Dynamically
        # -------------------------------
        llm = get_llm(
            provider=request.provider,
            model_name=request.model_name
        )
        

        # -------------------------------
        # 4️⃣ Retrieve Context
        # -------------------------------
        docs = retriever.get_relevant_documents(request.question)

        context = "\n".join([doc.page_content for doc in docs])

        # -------------------------------
        # 5️⃣ Build Prompt
        # -------------------------------
        final_prompt = f"""
        You are an enterprise AI assistant.
        Answer strictly using provided context.

        Context:
        {context}

        Question:
        {request.question}
        """

        response = llm.invoke(final_prompt)

        answer = response.content if hasattr(response, "content") else str(response)

        # -------------------------------
        # 6️⃣ Log User Prompt
        # -------------------------------
        insert_user_prompt_log(
            user_id=request.user_id,
            prompt=request.question,
            model_used=request.model_name,
            provider=request.provider
        )

        return {
            "answer": answer,
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
