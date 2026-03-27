"""第N个元素API"""

from fastapi import APIRouter

from echo.research.nth_item import get_nth_item


router = APIRouter(prefix="/api/nth", tags=["nth"])


@router.post("/item")
async def nth_item(items: list, n: int, default: str = None):
    """获取第N个元素"""
    tool = get_nth_item()
    return {"item": tool.nth(items, n, default)}


@router.post("/second")
async def second_item(items: list):
    """获取第二个元素"""
    tool = get_nth_item()
    return {"item": tool.second(items)}


@router.post("/third")
async def third_item(items: list):
    """获取第三个元素"""
    tool = get_nth_item()
    return {"item": tool.third(items)}
