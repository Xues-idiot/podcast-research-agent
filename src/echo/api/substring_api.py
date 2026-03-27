"""子串API"""

from fastapi import APIRouter

from echo.research.substring_tool import get_substring_tool


router = APIRouter(prefix="/api/substring", tags=["substring"])


@router.post("/substring")
async def substring(text: str, start: int, end: int = None):
    return {"result": get_substring_tool().substring(text, start, end)}