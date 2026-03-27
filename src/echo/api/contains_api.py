"""包含检查API"""

from fastapi import APIRouter

from echo.research.contains_tool import get_contains_tool


router = APIRouter(prefix="/api/contains", tags=["contains"])


@router.post("/contains")
async def contains(items: list, item):
    return {"result": get_contains_tool().contains(items, item)}