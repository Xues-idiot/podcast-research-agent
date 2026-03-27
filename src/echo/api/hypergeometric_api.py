"""超几何分布API"""

from fastapi import APIRouter
from pydantic import BaseModel

from echo.research.hypergeometric import get_hypergeometric


router = APIRouter(prefix="/api/hypergeometric", tags=["hypergeometric"])


class HypergeometricRequest(BaseModel):
    N: int
    K: int
    n: int
    k: int


@router.post("/probability")
async def probability(request: HypergeometricRequest):
    return {"result": get_hypergeometric().probability(
        request.N, request.K, request.n, request.k
    )}
