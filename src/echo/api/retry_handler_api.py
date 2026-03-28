"""重试工具API"""

from fastapi import APIRouter
from pydantic import BaseModel

from echo.research.retry_handler import get_retry_handler_tool


router = APIRouter(prefix="/api/retry-handler", tags=["retry-handler"])


class RetryRequest(BaseModel):
    max_attempts: int = 3
    delay: float = 1.0


@router.post("/retry")
async def retry(request: RetryRequest):
    tool = get_retry_handler_tool()
    return {"message": "Retry handler configured", "max_attempts": request.max_attempts, "delay": request.delay}