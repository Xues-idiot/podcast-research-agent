"""伯努利分布API"""

from fastapi import APIRouter
from pydantic import BaseModel

from echo.research.bernoulli_distribution import get_bernoulli_distribution


router = APIRouter(prefix="/api/bernoulli", tags=["bernoulli"])


class BernoulliRequest(BaseModel):
    k: int
    p: float


@router.post("/pmf")
async def pmf(request: BernoulliRequest):
    return {"result": get_bernoulli_distribution().pmf(request.k, request.p)}
