"""积分API"""

from fastapi import APIRouter
from pydantic import BaseModel

from echo.research.integral_tool import get_integral_tool


router = APIRouter(prefix="/api/integral-tool", tags=["integral-tool"])


class IntegralRequest(BaseModel):
    points: list
    dt: float = 1.0


@router.post("/trapezoidal")
async def trapezoidal(request: IntegralRequest):
    return {"result": get_integral_tool().trapezoidal(request.points, request.dt)}
