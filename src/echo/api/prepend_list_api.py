"""前缀API"""

from fastapi import APIRouter

from echo.research.prepend_list import get_prepend_list


router = APIRouter(prefix="/api/prepend", tags=["prepend"])


@router.post("/item")
async def prepend_item(items: list, item: str):
    """添加前缀元素"""
    tool = get_prepend_list()
    return {"items": tool.prepend(items, item)}


@router.post("/all")
async def prepend_all(items: list, prefix_items: list):
    """添加所有前缀元素"""
    tool = get_prepend_list()
    return {"items": tool.prepend_all(items, prefix_items)}
