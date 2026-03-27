"""威布尔API"""

from fastapi import APIRouter
from pydantic import BaseModel

from echo.research.weibull_tool import get_weibull_tool


router = APIRouter(prefix="/api/weibull", tags=["weibull"])


class WeibullRequest(BaseModel):
    x: float
    k: float
    lam: float


@router.post("/pdf")
async def pdf(request: WeibullRequest):
    return {"result": get_weibull_tool().pdf(request.x, request.k, request.lam)}
