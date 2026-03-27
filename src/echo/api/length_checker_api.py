"""长度检查API"""

from fastapi import APIRouter

from echo.research.length_checker import get_length_checker


router = APIRouter(prefix="/api/length-checker", tags=["length-checker"])


@router.post("/length")
async def length(items: list):
    return {"result": get_length_checker().length(items)}