"""查找最后一个API"""

from fastapi import APIRouter

from echo.research.find_last import get_find_last


router = APIRouter(prefix="/api/find-last", tags=["find-last"])


@router.post("/item")
async def find_last_item(items: list, pred: str):
    """查找最后一个满足条件的元素"""
    tool = get_find_last()
    pred_func = eval(pred)
    return {"item": tool.find_last(items, pred_func)}


@router.post("/index")
async def find_last_index(items: list, pred: str):
    """查找最后一个满足条件的元素索引"""
    tool = get_find_last()
    pred_func = eval(pred)
    return {"index": tool.find_last_index(items, pred_func)}
