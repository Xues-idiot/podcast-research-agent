"""陷波滤波API"""

from fastapi import APIRouter
from pydantic import BaseModel

from echo.research.notch_filter import get_notch_filter


router = APIRouter(prefix="/api/notch", tags=["notch"])


class NotchRequest(BaseModel):
    data: list
    freq: float
    sample_rate: float = 1.0


@router.post("/filter")
async def filter(request: NotchRequest):
    return {"result": get_notch_filter().filter(request.data, request.freq, request.sample_rate)}
