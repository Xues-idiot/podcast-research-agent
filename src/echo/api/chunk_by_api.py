"""滑动计数API"""

from fastapi import APIRouter

from echo.research.chunk_by import get_chunk_by


router = APIRouter(prefix="/api/chunk", tags=["chunk"])


@router.post("/by-size")
async def chunk_by_size(items: list, size: int):
    """按大小分块"""
    tool = get_chunk_by()
    return {"chunks": tool.chunk_by_size(items, size)}


@router.post("/by-pred")
async def chunk_by_pred(items: list, pred: str):
    """按条件分块"""
    tool = get_chunk_by()
    pred_func = eval(pred)
    return {"chunks": tool.chunk_by_pred(items, pred_func)}
