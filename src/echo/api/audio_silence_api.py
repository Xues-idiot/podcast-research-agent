"""音频静音检测API"""

from fastapi import APIRouter
from pydantic import BaseModel

from echo.research.audio_silence import get_audio_silence_tool


router = APIRouter(prefix="/api/audio-silence", tags=["audio-silence"])


class SilenceRequest(BaseModel):
    signal: list[float]
    threshold: float = 0.01


@router.post("/detect-silence")
async def detect_silence(request: SilenceRequest):
    tool = get_audio_silence_tool()
    return {"result": tool.detect_silence(request.signal, request.threshold)}