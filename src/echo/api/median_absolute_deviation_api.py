"""中位数绝对偏差API"""

from fastapi import APIRouter

from echo.research.median_absolute_deviation import get_median_absolute_deviation


router = APIRouter(prefix="/api/mad", tags=["mad"])


@router.post("/calculate")
async def calculate(data: list):
    return {"result": get_median_absolute_deviation().mad(data)}
