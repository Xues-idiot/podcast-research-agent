"""偏度计算API"""

from fastapi import APIRouter

from echo.research.skewness_calc import get_skewness_calc


router = APIRouter(prefix="/api/skewness", tags=["skewness"])


@router.post("/calculate")
async def calculate_skewness(values: list[float]):
    calc = get_skewness_calc()
    return {"skewness": calc.skewness(values)}
