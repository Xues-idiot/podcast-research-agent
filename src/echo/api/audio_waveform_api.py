"""音频波形API"""

from fastapi import APIRouter
from pydantic import BaseModel

from echo.research.audio_waveform import get_audio_waveform_tool


router = APIRouter(prefix="/api/audio-waveform", tags=["audio-waveform"])


class WaveformRequest(BaseModel):
    signal: list[float]
    bins: int = 100


@router.post("/waveform")
async def waveform(request: WaveformRequest):
    tool = get_audio_waveform_tool()
    return {"result": tool.waveform(request.signal, request.bins)}