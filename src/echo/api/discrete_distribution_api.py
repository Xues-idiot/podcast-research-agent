"""离散分布API"""

from fastapi import APIRouter
from pydantic import BaseModel

from echo.research.discrete_distribution import get_discrete_distribution


router = APIRouter(prefix="/api/discrete-dist", tags=["discrete-dist"])


class DiscreteRequest(BaseModel):
    values: list
    probabilities: list


@router.post("/sample")
async def sample(request: DiscreteRequest):
    return {"result": get_discrete_distribution().sample(request.values, request.probabilities)}
