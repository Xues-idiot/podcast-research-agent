"""音频声像API"""

from fastapi import APIRouter
from pydantic import BaseModel

from echo.research.audio_pan import get_audio_pan_tool


router = APIRouter(prefix="/api/audio-pan", tags=["audio-pan"])


class PanRequest(BaseModel):
    signal: list[float]
    pan: float


@router.post("/pan")
async def pan(request: PanRequest):
    tool = get_audio_pan_tool()
    left, right = tool.pan(request.signal, request.pan)
    return {"left": left, "right": right}