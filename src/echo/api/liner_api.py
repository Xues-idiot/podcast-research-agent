"""行处理API"""

from fastapi import APIRouter

from echo.research.liner_tool import get_liner_tool


router = APIRouter(prefix="/api/liner", tags=["liner"])


@router.post("/lines")
async def lines(text: str):
    return {"result": get_liner_tool().lines(text)}


@router.post("/join-lines")
async def join_lines(lines: list):
    return {"result": get_liner_tool().join_lines(lines)}