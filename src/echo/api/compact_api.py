"""紧凑API"""

from fastapi import APIRouter

from echo.research.compact_tool import get_compact_tool


router = APIRouter(prefix="/api/compact", tags=["compact"])


@router.post("/compact")
async def compact(items: list):
    return {"result": get_compact_tool().compact(items)}