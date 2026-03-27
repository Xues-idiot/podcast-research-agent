"""长度API"""

from fastapi import APIRouter

from echo.research.length_tool import get_length_tool


router = APIRouter(prefix="/api/length", tags=["length"])


@router.post("/length")
async def length(items: list):
    return {"result": get_length_tool().length(items)}