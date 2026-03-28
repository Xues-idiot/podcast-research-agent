"""多边形面积API"""

from fastapi import APIRouter
from pydantic import BaseModel

from echo.research.polygon_area import get_polygon_area_tool


router = APIRouter(prefix="/api/polygon-area", tags=["polygon-area"])


class AreaRequest(BaseModel):
    vertices: list[list[float]]


@router.post("/area")
async def area(request: AreaRequest):
    tool = get_polygon_area_tool()
    return {"result": tool.area(request.vertices)}