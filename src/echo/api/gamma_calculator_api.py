"""伽马函数API"""

from fastapi import APIRouter
from pydantic import BaseModel

from echo.research.gamma_calculator import get_gamma_calculator


router = APIRouter(prefix="/api/gamma-calc", tags=["gamma-calc"])


class GammaRequest(BaseModel):
    n: float


@router.post("/gamma")
async def gamma(request: GammaRequest):
    return {"result": get_gamma_calculator().gamma(request.n)}
