"""加权平均计算API"""

from fastapi import APIRouter

from echo.research.weighted_average_calc import get_weighted_average_calc


router = APIRouter(prefix="/api/weighted-avg", tags=["weighted-average"])


@router.post("/calculate")
async def calculate_weighted_avg(values: list[float], weights: list[float]):
    calc = get_weighted_average_calc()
    return {"result": calc.weighted_avg(values, weights)}
