"""样条插值API"""

from fastapi import APIRouter
from pydantic import BaseModel

from echo.research.spline_tool import get_spline_tool


router = APIRouter(prefix="/api/spline", tags=["spline"])


class SplineRequest(BaseModel):
    points: list
    x: float


@router.post("/interpolate")
async def interpolate(request: SplineRequest):
    return {"result": get_spline_tool().linear_interpolate(request.points, request.x)}
