"""音频混响API"""

from fastapi import APIRouter
from pydantic import BaseModel

from echo.research.audio_reverb import get_audio_reverb_tool


router = APIRouter(prefix="/api/audio-reverb", tags=["audio-reverb"])


class ReverbRequest(BaseModel):
    signal: list[float]
    room_size: float = 0.5
    damping: float = 0.5
    mix: float = 0.3


@router.post("/reverb")
async def reverb(request: ReverbRequest):
    tool = get_audio_reverb_tool()
    return {"result": tool.reverb(request.signal, request.room_size, request.damping, request.mix)}