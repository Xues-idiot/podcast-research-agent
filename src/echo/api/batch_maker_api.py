"""批处理制造API"""

from fastapi import APIRouter

from echo.research.batch_maker import get_batch_maker


router = APIRouter(prefix="/api/batch-maker", tags=["batch-maker"])


@router.post("/make")
async def make_batch(items: list, size: int):
    return {"result": get_batch_maker().make_batch(items, size)}