"""转小写API"""

from fastapi import APIRouter

from echo.research.lower_tool import get_lower_tool


router = APIRouter(prefix="/api/lower", tags=["lower"])


@router.post("/lower")
async def lower(text: str):
    return {"result": get_lower_tool().lower(text)}