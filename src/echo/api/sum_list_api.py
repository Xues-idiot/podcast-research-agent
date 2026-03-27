"""求和API"""

from fastapi import APIRouter

from echo.research.sum_list import get_sum_list


router = APIRouter(prefix="/api/sum", tags=["sum"])


@router.post("/items")
async def sum_items(items: list):
    """求和"""
    tool = get_sum_list()
    return {"sum": tool.sum(items)}


@router.post("/by")
async def sum_by(items: list, key: str):
    """按键求和"""
    tool = get_sum_list()
    key_func = eval(key)
    return {"sum": tool.sum_by(items, key_func)}


@router.post("/product")
async def product_items(items: list):
    """求积"""
    tool = get_sum_list()
    return {"product": tool.product(items)}
