"""范围生成工具API"""

from fastapi import APIRouter

from echo.research.range_gen_tool import get_range_gen_tool


router = APIRouter(prefix="/api/range-gen", tags=["range-gen"])


@router.post("/int-range")
async def int_range(start: int, stop: int, step: int = 1):
    return {"result": get_range_gen_tool().int_range(start, stop, step)}


@router.post("/float-range")
async def float_range(start: float, stop: float, step: float):
    return {"result": get_range_gen_tool().float_range(start, stop, step)}