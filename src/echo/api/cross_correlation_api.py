"""互相关API"""

from fastapi import APIRouter
from pydantic import BaseModel

from echo.research.cross_correlation import get_cross_correlation


router = APIRouter(prefix="/api/cross-corr", tags=["cross-corr"])


class CrossCorrRequest(BaseModel):
    x: list
    y: list
    lag: int = 0


@router.post("/calculate")
async def calculate(request: CrossCorrRequest):
    return {"result": get_cross_correlation().cross_corr(request.x, request.y, request.lag)}
