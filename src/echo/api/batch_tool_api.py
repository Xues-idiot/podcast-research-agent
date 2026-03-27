"""批处理API"""

from fastapi import APIRouter

from echo.research.batch_tool import get_batch_tool


router = APIRouter(prefix="/api/batch", tags=["batch"])


@router.post("/batch")
async def batch(items: list, size: int):
    return {"result": get_batch_tool().batch(items, size)}