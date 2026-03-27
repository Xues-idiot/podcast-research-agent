"""去除空白API"""

from fastapi import APIRouter

from echo.research.strip_tool import get_strip_tool


router = APIRouter(prefix="/api/strip", tags=["strip"])


@router.post("/strip")
async def strip(text: str):
    return {"result": get_strip_tool().strip(text)}