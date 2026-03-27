"""协方差API"""

from fastapi import APIRouter
from pydantic import BaseModel

from echo.research.covariance_calculator import get_covariance_calculator


router = APIRouter(prefix="/api/covariance-calc", tags=["covariance-calc"])


class CovarianceRequest(BaseModel):
    x: list
    y: list


@router.post("/covariance")
async def covariance(request: CovarianceRequest):
    return {"result": get_covariance_calculator().covariance(request.x, request.y)}
