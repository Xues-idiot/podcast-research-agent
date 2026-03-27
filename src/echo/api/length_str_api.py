"""字符串长度API"""

from fastapi import APIRouter

from echo.research.length_str_tool import get_length_str_tool


router = APIRouter(prefix="/api/length-str", tags=["length-str"])


@router.post("/length")
async def length(text: str):
    return {"result": get_length_str_tool().length(text)}