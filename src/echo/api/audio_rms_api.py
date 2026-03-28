"""音频RMS API"""

from fastapi import APIRouter
from pydantic import BaseModel

from echo.research.audio_rms import get_audio_rms_tool


router = APIRouter(prefix="/api/audio-rms", tags=["audio-rms"])


class RmsRequest(BaseModel):
    signal: list[float]
    window_size: int = 1024


@router.post("/rms")
async def rms(request: RmsRequest):
    tool = get_audio_rms_tool()
    return {"result": tool.rms(request.signal)}


@router.post("/rms-windowed")
async def rms_windowed(request: RmsRequest):
    tool = get_audio_rms_tool()
    return {"result": tool.rms_windowed(request.signal, request.window_size)}