"""峰度API"""

from fastapi import APIRouter

from echo.research.kurtosis_tool import get_kurtosis_tool


router = APIRouter(prefix="/api/kurtosis", tags=["kurtosis"])


@router.post("/calculate")
async def calculate(data: list):
    return {"result": get_kurtosis_tool().kurtosis(data)}
