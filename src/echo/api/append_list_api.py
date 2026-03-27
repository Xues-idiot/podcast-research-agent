"""追加API"""

from fastapi import APIRouter

from echo.research.append_list import get_append_list


router = APIRouter(prefix="/api/append", tags=["append"])


@router.post("/item")
async def append_item(items: list, item: str):
    """追加单个元素"""
    tool = get_append_list()
    return {"items": tool.append(items, item)}


@router.post("/all")
async def append_all(items: list, append_items: list):
    """追加所有元素"""
    tool = get_append_list()
    return {"items": tool.append_all(items, append_items)}
