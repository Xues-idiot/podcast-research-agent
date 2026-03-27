"""平均值API"""

from fastapi import APIRouter

from echo.research.mean_calculator import get_mean_calculator


router = APIRouter(prefix="/api/mean-calc", tags=["mean-calc"])


@router.post("/mean")
async def mean(items: list):
    return {"result": get_mean_calculator().mean(items)}
