"""Beta二项分布API"""

from fastapi import APIRouter
from pydantic import BaseModel

from echo.research.beta_binomial import get_beta_binomial


router = APIRouter(prefix="/api/beta-binomial", tags=["beta-binomial"])


class BetaBinomialRequest(BaseModel):
    k: int
    n: int
    alpha: float
    beta: float


@router.post("/pmf")
async def pmf(request: BetaBinomialRequest):
    return {"result": get_beta_binomial().pmf(request.k, request.n, request.alpha, request.beta)}
