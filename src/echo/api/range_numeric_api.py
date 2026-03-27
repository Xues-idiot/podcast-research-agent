"""数字范围API"""

from fastapi import APIRouter

from echo.research.range_numeric import get_range_numeric


router = APIRouter(prefix="/api/range", tags=["range"])


@router.post("/generate")
async def generate_range(start: int, end: int, step: int = 1):
    """生成范围"""
    tool = get_range_numeric()
    return {"range": tool.range(start, end, step)}


@router.post("/to")
async def range_to(end: int):
    """生成0到end的范围"""
    tool = get_range_numeric()
    return {"range": tool.range_to(end)}


@router.post("/from-to")
async def range_from_to(start: int, end: int):
    """生成从start到end的范围"""
    tool = get_range_numeric()
    return {"range": tool.range_from_to(start, end)}


@router.post("/inclusive")
async def inclusive_range(start: int, end: int, step: int = 1):
    """生成包含end的范围"""
    tool = get_range_numeric()
    return {"range": tool.inclusive_range(start, end, step)}
