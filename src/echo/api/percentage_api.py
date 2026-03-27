"""百分比API"""

from fastapi import APIRouter

from echo.research.percentage import get_percentage_tool


router = APIRouter(prefix="/api/percentage", tags=["percentage"])


@router.post("/calculate")
async def calculate(part: float, total: float):
    return {"result": get_percentage_tool().calculate(part, total)}


@router.post("/of")
async def percent_of(percent: float, total: float):
    return {"result": get_percentage_tool().of(percent, total)}


@router.post("/format")
async def format_percent(value: float, decimals: int = 2):
    return {"result": get_percentage_tool().format(value, decimals)}