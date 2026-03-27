"""二项分布API"""

from fastapi import APIRouter
from pydantic import BaseModel

from echo.research.binomial_calculator import get_binomial_calculator


router = APIRouter(prefix="/api/binomial-calc", tags=["binomial-calc"])


class BinomialRequest(BaseModel):
    n: int
    p: float
    k: int


@router.post("/probability")
async def probability(request: BinomialRequest):
    return {"result": get_binomial_calculator().binomial(request.n, request.p, request.k)}
