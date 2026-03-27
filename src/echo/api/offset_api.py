"""偏移API"""

from fastapi import APIRouter

from echo.research.offset_tool import get_offset_tool


router = APIRouter(prefix="/api/offset", tags=["offset"])


@router.post("/offset-value")
async def offset_value(value: float, delta: float):
    return {"result": get_offset_tool().offset_value(value, delta)}


@router.post("/offset-list")
async def offset_list(items: list, delta: float):
    return {"result": get_offset_tool().offset_list(items, delta)}