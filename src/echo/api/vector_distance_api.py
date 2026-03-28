"""向量距离API"""

from fastapi import APIRouter
from pydantic import BaseModel

from echo.research.vector_distance import get_vector_distance_tool


router = APIRouter(prefix="/api/vector-distance", tags=["vector-distance"])


class DistanceRequest(BaseModel):
    a: list[float]
    b: list[float]


@router.post("/distance")
async def distance(request: DistanceRequest):
    tool = get_vector_distance_tool()
    return {"result": tool.distance(request.a, request.b)}