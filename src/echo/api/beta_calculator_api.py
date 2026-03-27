"""贝塔函数API"""

from fastapi import APIRouter
from pydantic import BaseModel

from echo.research.beta_calculator import get_beta_calculator


router = APIRouter(prefix="/api/beta-calc", tags=["beta-calc"])


class BetaRequest(BaseModel):
    a: float
    b: float


@router.post("/beta")
async def beta(request: BetaRequest):
    return {"result": get_beta_calculator().beta(request.a, request.b)}
