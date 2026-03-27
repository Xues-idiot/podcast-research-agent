"""帕累托分布API"""

from fastapi import APIRouter
from pydantic import BaseModel

from echo.research.pareto_distribution import get_pareto_distribution


router = APIRouter(prefix="/api/pareto-dist", tags=["pareto-dist"])


class ParetoDistRequest(BaseModel):
    alpha: float
    xm: float


@router.post("/mean")
async def mean(request: ParetoDistRequest):
    return {"result": get_pareto_distribution().mean(request.alpha, request.xm)}
