"""压缩API"""

from fastapi import APIRouter

from echo.research.compact_pred import get_compact_pred


router = APIRouter(prefix="/api/compact", tags=["compact"])


@router.post("/items")
async def compact_items(items: list):
    """压缩列表"""
    tool = get_compact_pred()
    return {"items": tool.compact(items)}


@router.post("/by")
async def compact_by(items: list, pred: str):
    """按条件压缩"""
    tool = get_compact_pred()
    pred_func = eval(pred)
    return {"items": tool.compact_by(items, pred_func)}


@router.post("/is-empty")
async def is_empty(items: list):
    """检查是否为空"""
    tool = get_compact_pred()
    return {"is_empty": tool.is_empty(items)}
