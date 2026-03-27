"""分布API"""

from fastapi import APIRouter

from echo.research.distribution_tool import get_distribution_tool


router = APIRouter(prefix="/api/distribution", tags=["distribution"])


@router.post("/normal")
async def normal(mean: float, std_dev: float, count: int):
    return {"result": get_distribution_tool().normal(mean, std_dev, count)}


@router.post("/uniform")
async def uniform(low: float, high: float, count: int):
    return {"result": get_distribution_tool().uniform(low, high, count)}