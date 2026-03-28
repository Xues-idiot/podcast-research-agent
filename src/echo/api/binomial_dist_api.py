"""二项分布API"""

from fastapi import APIRouter

from echo.research.binomial_distribution import get_binomial_distribution


router = APIRouter(prefix="/api/binomial", tags=["binomial"])


@router.post("/pmf")
async def binomial_pmf(k: int, n: int, p: float):
    dist = get_binomial_distribution()
    return {"pmf": dist.pmf(k, n, p)}
