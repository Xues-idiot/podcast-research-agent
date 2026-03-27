"""幂计算API"""

from fastapi import APIRouter
from pydantic import BaseModel

from echo.research.power_calculator import get_power_calculator


router = APIRouter(prefix="/api/power-calc", tags=["power-calc"])


class PowerRequest(BaseModel):
    base: float
    exp: float


@router.post("/power")
async def power(request: PowerRequest):
    return {"result": get_power_calculator().power(request.base, request.exp)}
