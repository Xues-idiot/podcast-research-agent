"""序列API"""

from fastapi import APIRouter

from echo.research.sequence_tool import get_sequence_tool


router = APIRouter(prefix="/api/sequence", tags=["sequence"])


@router.post("/repeat")
async def repeat(item, count: int):
    return {"result": get_sequence_tool().repeat(item, count)}


@router.post("/cycle")
async def cycle(items: list, count: int):
    return {"result": get_sequence_tool().cycle(items, count)}