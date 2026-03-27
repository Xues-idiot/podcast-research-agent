"""正态分布API"""

from fastapi import APIRouter
from pydantic import BaseModel

from echo.research.normal_distribution import get_normal_distribution


router = APIRouter(prefix="/api/normal-dist", tags=["normal-dist"])


class NormalRequest(BaseModel):
    x: float
    mean: float = 0
    stdev: float = 1


@router.post("/pdf")
async def pdf(request: NormalRequest):
    return {"result": get_normal_distribution().pdf(request.x, request.mean, request.stdev)}
