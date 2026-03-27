"""中值滤波API"""

from fastapi import APIRouter
from pydantic import BaseModel

from echo.research.median_filter import get_median_filter


router = APIRouter(prefix="/api/median-filter", tags=["median-filter"])


class MedianRequest(BaseModel):
    data: list
    window: int = 3


@router.post("/filter")
async def filter(request: MedianRequest):
    return {"result": get_median_filter().filter(request.data, request.window)}
