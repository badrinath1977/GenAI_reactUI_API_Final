from fastapi.responses import JSONResponse
from core.logger import get_logger
from repository.error_log_repository import ErrorLogRepository

logger = get_logger("ExceptionHandler")
error_repo = ErrorLogRepository()

async def global_exception_handler(request, exc):

    trace_id = getattr(request.state, "trace_id", "N/A")

    logger.error(f"TraceId={trace_id} | Exception={str(exc)}")

    error_repo.insert(
        trace_id=trace_id,
        error_message=str(exc),
        endpoint=str(request.url)
    )

    return JSONResponse(
        status_code=500,
        content={"message": "Internal Server Error", "trace_id": trace_id}
    )
