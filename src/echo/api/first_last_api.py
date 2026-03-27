"""首尾元素API"""

from fastapi import APIRouter

from echo.research.first_last import get_first_last


router = APIRouter(prefix="/api/first-last", tags=["first-last"])


@router.post("/first")
async def first_item(items: list):
    """获取第一个元素"""
    tool = get_first_last()
    return {"item": tool.first(items)}


@router.post("/last")
async def last_item(items: list):
    """获取最后一个元素"""
    tool = get_first_last()
    return {"item": tool.last(items)}


@router.post("/rest")
async def rest_items(items: list):
    """获取除第一个外的所有元素"""
    tool = get_first_last()
    return {"items": tool.rest(items)}


@router.post("/but-last")
async def but_last_items(items: list):
    """获取除最后一个外的所有元素"""
    tool = get_first_last()
    return {"items": tool.but_last(items)}
