"""点是否在多边形内API"""

from fastapi import APIRouter
from pydantic import BaseModel

from echo.research.point_in_polygon import get_point_in_polygon_tool


router = APIRouter(prefix="/api/point-in-polygon", tags=["point-in-polygon"])


class ContainsRequest(BaseModel):
    point: list[float]
    vertices: list[list[float]]


@router.post("/contains")
async def contains(request: ContainsRequest):
    tool = get_point_in_polygon_tool()
    return {"result": tool.contains(request.point, request.vertices)}