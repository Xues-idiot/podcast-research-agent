"""音频峰值检测API"""

from fastapi import APIRouter
from pydantic import BaseModel

from echo.research.audio_peak import get_audio_peak_tool


router = APIRouter(prefix="/api/audio-peak", tags=["audio-peak"])


class PeakRequest(BaseModel):
    signal: list[float]
    threshold: float = 0.8


@router.post("/peak")
async def peak(request: PeakRequest):
    tool = get_audio_peak_tool()
    return {"result": tool.peak(request.signal)}


@router.post("/peaks")
async def peaks(request: PeakRequest):
    tool = get_audio_peak_tool()
    return {"result": tool.peaks(request.signal, request.threshold)}