"""匹配工具API"""

from fastapi import APIRouter

from echo.research.match_tool import get_match_tool


router = APIRouter(prefix="/api/match", tags=["match"])


@router.post("/match")
async def match(value, patterns: list):
    return {"result": get_match_tool().match(value, patterns)}