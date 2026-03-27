"""重复API"""

from fastapi import APIRouter

from echo.research.repeat_list import get_repeat_list


router = APIRouter(prefix="/api/repeat", tags=["repeat"])


@router.post("/item")
async def repeat_item(item: str, n: int):
    """重复元素"""
    tool = get_repeat_list()
    return {"items": tool.repeat(item, n)}


@router.post("/cycle")
async def cycle_items(items: list, n: int):
    """重复列表n次"""
    tool = get_repeat_list()
    return {"items": tool.cycle(items, n)}
