"""多边形周长API"""

from fastapi import APIRouter
from pydantic import BaseModel

from echo.research.polygon_perimeter import get_polygon_perimeter_tool


router = APIRouter(prefix="/api/polygon-perimeter", tags=["polygon-perimeter"])


class PerimeterRequest(BaseModel):
    vertices: list[list[float]]


@router.post("/perimeter")
async def perimeter(request: PerimeterRequest):
    tool = get_polygon_perimeter_tool()
    return {"result": tool.perimeter(request.vertices)}