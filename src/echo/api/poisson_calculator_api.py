"""泊松分布API"""

from fastapi import APIRouter
from pydantic import BaseModel

from echo.research.poisson_calculator import get_poisson_calculator


router = APIRouter(prefix="/api/poisson-calc", tags=["poisson-calc"])


class PoissonRequest(BaseModel):
    lambda_val: float
    k: int


@router.post("/probability")
async def probability(request: PoissonRequest):
    return {"result": get_poisson_calculator().poisson(request.lambda_val, request.k)}
