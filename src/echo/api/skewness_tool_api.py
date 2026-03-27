"""偏度API"""

from fastapi import APIRouter

from echo.research.skewness_tool import get_skewness_tool


router = APIRouter(prefix="/api/skewness", tags=["skewness"])


@router.post("/calculate")
async def calculate(data: list):
    return {"result": get_skewness_tool().skewness(data)}
