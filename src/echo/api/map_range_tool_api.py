"""范围映射API"""

from fastapi import APIRouter
from pydantic import BaseModel

from echo.research.map_range_tool import get_map_range_tool


router = APIRouter(prefix="/api/map-range-tool", tags=["map-range-tool"])


class MapRangeRequest(BaseModel):
    value: float
    in_min: float
    in_max: float
    out_min: float
    out_max: float


@router.post("/map-range")
async def map_range(request: MapRangeRequest):
    return {"result": get_map_range_tool().map_range(
        request.value, request.in_min, request.in_max, request.out_min, request.out_max
    )}
