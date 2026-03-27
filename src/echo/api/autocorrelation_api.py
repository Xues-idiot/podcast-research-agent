"""自相关API"""

from fastapi import APIRouter
from pydantic import BaseModel

from echo.research.autocorrelation import get_autocorrelation


router = APIRouter(prefix="/api/autocorr", tags=["autocorr"])


class AutoCorrRequest(BaseModel):
    data: list
    lag: int = 1


@router.post("/calculate")
async def calculate(request: AutoCorrRequest):
    return {"result": get_autocorrelation().autocorr(request.data, request.lag)}
