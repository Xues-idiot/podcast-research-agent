"""加权平均API"""

from fastapi import APIRouter
from pydantic import BaseModel

from echo.research.weighted_mean import get_weighted_mean


router = APIRouter(prefix="/api/weighted-mean", tags=["weighted-mean"])


class WeightedMeanRequest(BaseModel):
    values: list
    weights: list


@router.post("/calculate")
async def calculate(request: WeightedMeanRequest):
    return {"result": get_weighted_mean().weighted_mean(request.values, request.weights)}
