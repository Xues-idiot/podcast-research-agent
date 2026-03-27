"""线性插值API"""

from fastapi import APIRouter
from pydantic import BaseModel

from echo.research.linear_interpolator import get_linear_interpolator


router = APIRouter(prefix="/api/linear-interpolator", tags=["linear-interpolator"])


class InterpolatorRequest(BaseModel):
    points: list
    index: float


@router.post("/interpolate")
async def interpolate(request: InterpolatorRequest):
    return {"result": get_linear_interpolator().linear_points(request.points, request.index)}
