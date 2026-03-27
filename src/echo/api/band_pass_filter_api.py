"""带通滤波API"""

from fastapi import APIRouter
from pydantic import BaseModel

from echo.research.band_pass_filter import get_band_pass_filter


router = APIRouter(prefix="/api/band-pass", tags=["band-pass"])


class BandPassRequest(BaseModel):
    data: list
    low: float
    high: float


@router.post("/filter")
async def filter(request: BandPassRequest):
    return {"result": get_band_pass_filter().filter(request.data, request.low, request.high)}
