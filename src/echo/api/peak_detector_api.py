"""峰值检测API"""

from fastapi import APIRouter
from pydantic import BaseModel

from echo.research.peak_detector import get_peak_detector


router = APIRouter(prefix="/api/peak", tags=["peak"])


class PeakRequest(BaseModel):
    signal: list
    threshold: float = 0.0


@router.post("/find")
async def find(request: PeakRequest):
    return {"result": get_peak_detector().find_peaks(request.signal, request.threshold)}
