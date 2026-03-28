"""泊松分布API"""

from fastapi import APIRouter

from echo.research.poisson_distribution import get_poisson_distribution


router = APIRouter(prefix="/api/poisson", tags=["poisson"])


@router.post("/pmf")
async def poisson_pmf(k: int, lam: float):
    dist = get_poisson_distribution()
    return {"pmf": dist.pmf(k, lam)}
