"""查找第一个API"""

from fastapi import APIRouter

from echo.research.find_first import get_find_first


router = APIRouter(prefix="/api/find-first", tags=["find-first"])


@router.post("/item")
async def find_first_item(items: list, pred: str):
    """查找第一个满足条件的元素"""
    tool = get_find_first()
    pred_func = eval(pred)
    return {"item": tool.find_first(items, pred_func)}


@router.post("/index")
async def find_first_index(items: list, pred: str):
    """查找第一个满足条件的元素索引"""
    tool = get_find_first()
    pred_func = eval(pred)
    return {"index": tool.find_first_index(items, pred_func)}
