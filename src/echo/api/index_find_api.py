"""索引查找API"""

from fastapi import APIRouter

from echo.research.index_of import get_index_of


router = APIRouter(prefix="/api/index-find", tags=["index-find"])


@router.post("/of")
async def index_of(items: list, item: str):
    """查找元素索引"""
    tool = get_index_of()
    return {"index": tool.index_of(items, item)}


@router.post("/last-of")
async def last_index_of(items: list, item: str):
    """查找最后元素索引"""
    tool = get_index_of()
    return {"index": tool.last_index_of(items, item)}


@router.post("/find")
async def find_index(items: list, pred: str):
    """按条件查找索引"""
    tool = get_index_of()
    pred_func = eval(pred)
    return {"index": tool.find_index(items, pred_func)}
