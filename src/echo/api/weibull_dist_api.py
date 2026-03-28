"""威布尔分布API"""

from fastapi import APIRouter

from echo.research.weibull_calc import get_weibull_distribution


router = APIRouter(prefix="/api/weibull", tags=["weibull"])


@router.post("/pdf")
async def weibull_pdf(x: float, shape: float, scale: float = 1):
    dist = get_weibull_distribution()
    return {"pdf": dist.pdf(x, shape, scale)}
