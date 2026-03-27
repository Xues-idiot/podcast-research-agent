"""比例API"""

from fastapi import APIRouter

from echo.research.ratio_tool import get_ratio_tool


router = APIRouter(prefix="/api/ratio", tags=["ratio"])


@router.post("/calculate")
async def calculate_ratio(a: float, b: float):
    return {"result": get_ratio_tool().calculate_ratio(a, b)}


@router.post("/simplify")
async def simplify_ratio(a: float, b: float):
    return {"result": get_ratio_tool().simplify_ratio(a, b)}


@router.post("/scale")
async def scale_ratio(a: float, b: float, factor: float):
    return {"result": get_ratio_tool().scale_ratio(a, b, factor)}