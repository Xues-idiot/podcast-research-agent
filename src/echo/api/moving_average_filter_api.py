"""移动平均滤波API"""

from fastapi import APIRouter
from pydantic import BaseModel

from echo.research.moving_average_filter import get_moving_average_filter


router = APIRouter(prefix="/api/moving-avg-filter", tags=["moving-avg-filter"])


class MaFilterRequest(BaseModel):
    data: list
    window: int = 3


@router.post("/filter")
async def filter(request: MaFilterRequest):
    return {"result": get_moving_average_filter().filter(request.data, request.window)}
