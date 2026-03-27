"""映射API"""

from fastapi import APIRouter

from echo.research.map_tool import get_map_tool


router = APIRouter(prefix="/api/map", tags=["map"])


@router.post("/map")
async def map_items(items: list, func):
    return {"result": get_map_tool().map_items(items, func)}