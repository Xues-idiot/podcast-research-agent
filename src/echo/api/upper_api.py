"""转大写API"""

from fastapi import APIRouter

from echo.research.upper_tool import get_upper_tool


router = APIRouter(prefix="/api/upper", tags=["upper"])


@router.post("/upper")
async def upper(text: str):
    return {"result": get_upper_tool().upper(text)}