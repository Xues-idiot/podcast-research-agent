"""枚举API"""

from fastapi import APIRouter

from echo.research.enumerate_list import get_enumerate_list


router = APIRouter(prefix="/api/enumerate", tags=["enumerate"])


@router.post("/items")
async def enumerate_items(items: list, start: int = 0):
    """枚举列表"""
    tool = get_enumerate_list()
    return {"items": tool.enumerate(items, start)}


@router.post("/with-index")
async def with_index(items: list, start: int = 0):
    """带索引枚举"""
    tool = get_enumerate_list()
    return {"items": tool.with_index(items, start)}
