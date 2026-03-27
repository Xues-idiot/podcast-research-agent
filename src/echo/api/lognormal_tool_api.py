"""对数正态API"""

from fastapi import APIRouter
from pydantic import BaseModel

from echo.research.lognormal_tool import get_lognormal_tool


router = APIRouter(prefix="/api/lognormal", tags=["lognormal"])


class LognormalRequest(BaseModel):
    x: float
    mu: float
    sigma: float


@router.post("/pdf")
async def pdf(request: LognormalRequest):
    return {"result": get_lognormal_tool().pdf(request.x, request.mu, request.sigma)}
