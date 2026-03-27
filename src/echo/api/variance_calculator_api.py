"""方差计算器API"""

from fastapi import APIRouter

from echo.research.variance_calculator import get_variance_calculator


router = APIRouter(prefix="/api/variance-calc", tags=["variance-calc"])


@router.post("/variance")
async def variance(items: list):
    return {"result": get_variance_calculator().variance(items)}
