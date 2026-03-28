"""圆面积API"""

from fastapi import APIRouter
from pydantic import BaseModel

from echo.research.circle_area import get_circle_area_tool


router = APIRouter(prefix="/api/circle-area", tags=["circle-area"])


class AreaRequest(BaseModel):
    radius: float


@router.post("/area")
async def area(request: AreaRequest):
    tool = get_circle_area_tool()
    return {"result": tool.area(request.radius)}