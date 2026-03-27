"""重试API"""

from fastapi import APIRouter

from echo.research.retry import get_retry


router = APIRouter(prefix="/api/retry-tool", tags=["retry-tool"])


@router.post("/retry")
async def retry():
    return {"result": None}
