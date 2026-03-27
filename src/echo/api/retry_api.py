"""重试API"""

from fastapi import APIRouter

from echo.research.retry_tool import get_retry_tool


router = APIRouter(prefix="/api/retry", tags=["retry"])


@router.post("/retry")
async def retry(func, max_attempts: int = 3):
    return {"result": get_retry_tool().retry(func, max_attempts)}