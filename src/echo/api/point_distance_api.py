"""点距离API"""

from fastapi import APIRouter
from pydantic import BaseModel

from echo.research.point_distance import get_point_distance


router = APIRouter(prefix="/api/point-distance", tags=["point-distance"])


class PointDistanceRequest(BaseModel):
    x1: float
    y1: float
    x2: float
    y2: float


@router.post("/euclidean")
async def euclidean(request: PointDistanceRequest):
    return {"result": get_point_distance().euclidean(
        request.x1, request.y1, request.x2, request.y2
    )}
