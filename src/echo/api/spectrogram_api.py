"""频谱分析API"""

from fastapi import APIRouter
from pydantic import BaseModel

from echo.research.spectrogram import get_spectrogram


router = APIRouter(prefix="/api/spectrogram", tags=["spectrogram"])


class SpectrogramRequest(BaseModel):
    signal: list
    window_size: int = 256


@router.post("/compute")
async def compute(request: SpectrogramRequest):
    return {"result": get_spectrogram().compute(request.signal, request.window_size)}
