"""切片API"""

from fastapi import APIRouter

from echo.research.slice_list import get_slice_list


router = APIRouter(prefix="/api/slice", tags=["slice"])


@router.post("/items")
async def slice_items(items: list, start: int = 0, end: int = None):
    """切片"""
    tool = get_slice_list()
    return {"items": tool.slice(items, start, end)}


@router.post("/head")
async def head_items(items: list, n: int = 1):
    """获取前N个元素"""
    tool = get_slice_list()
    return {"items": tool.head(items, n)}


@router.post("/tail")
async def tail_items(items: list, n: int = 1):
    """获取后N个元素"""
    tool = get_slice_list()
    return {"items": tool.tail(items, n)}
