"""线段交点API"""

from fastapi import APIRouter
from pydantic import BaseModel

from echo.research.line_intersection import get_line_intersection_tool


router = APIRouter(prefix="/api/line-intersection", tags=["line-intersection"])


class IntersectionRequest(BaseModel):
    p1: list[float]
    p2: list[float]
    p3: list[float]
    p4: list[float]


@router.post("/intersection")
async def intersection(request: IntersectionRequest):
    tool = get_line_intersection_tool()
    return {"result": list(tool.intersection(request.p1, request.p2, request.p3, request.p4))}