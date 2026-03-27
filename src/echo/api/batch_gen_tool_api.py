"""批处理API"""

from fastapi import APIRouter

from echo.research.batch_gen_tool import get_batch_gen_tool


router = APIRouter(prefix="/api/batch-gen", tags=["batch-gen"])


@router.post("/batch")
async def batch(items: list, size: int):
    return {"result": get_batch_gen_tool().batch(items, size)}