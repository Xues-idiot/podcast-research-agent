"""插入API"""

from fastapi import APIRouter

from echo.research.insert_list import get_insert_list


router = APIRouter(prefix="/api/insert", tags=["insert"])


@router.post("/item")
async def insert_item(items: list, index: int, item: str):
    """插入单个元素"""
    tool = get_insert_list()
    return {"items": tool.insert(items, index, item)}


@router.post("/all")
async def insert_all(items: list, index: int, insert_items: list):
    """插入所有元素"""
    tool = get_insert_list()
    return {"items": tool.insert_all(items, index, insert_items)}
