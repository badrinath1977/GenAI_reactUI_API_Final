from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
import traceback

from app.services.llm_factory import get_llm
from app.services.vector_store_service import VectorStoreService
from app.repository.prompt_repository import insert_user_prompt_log
from app.repository.error_repository import insert_error_log
from app.core.logger import logger

router = APIRouter(prefix="/chat", tags=["Chat"])


class ChatRequest(BaseModel):
    user_id: str
    question: str
    department: str


@router.post("/")
async def chat(request: ChatRequest):

    try:
        logger.info(f"Chat request from User={request.user_id}")

        vector_service = VectorStoreService(department=request.department)
        retriever = vector_service.get_retriever()

        docs = retriever.invoke(request.question)

        if not docs:
            return {
                "answer": "No relevant information found.",
                "department": request.department
            }

        context = "\n\n".join(doc.page_content for doc in docs)

        llm = get_llm()

        final_prompt = f"""
You are an enterprise AI assistant.

Rules:
- Answer strictly using the provided context.
- If answer not found, say: Information not available.

Context:
{context}

Question:
{request.question}
"""

        response = llm.invoke(final_prompt)
        answer = response.content

        insert_user_prompt_log(
            user_name=request.user_id,
            question=request.question,
            response=answer,
            model_used="gpt-3.5-turbo",
            provider="openai",
            department=request.department,
            tokens_used=None
        )

        return {
            "answer": answer.strip(),
            "department": request.department
        }

    except Exception as ex:

        insert_error_log(
            user_id=request.user_id,
            error_type="ChatError",
            error_message=str(ex),
            stack_trace=traceback.format_exc()
        )

        raise HTTPException(status_code=500, detail="Internal Server Error")
