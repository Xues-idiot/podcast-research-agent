"""峰度计算API"""

from fastapi import APIRouter

from echo.research.kurtosis_calc import get_kurtosis_calc


router = APIRouter(prefix="/api/kurtosis", tags=["kurtosis"])


@router.post("/calculate")
async def calculate_kurtosis(values: list[float]):
    calc = get_kurtosis_calc()
    return {"kurtosis": calc.kurtosis(values)}
