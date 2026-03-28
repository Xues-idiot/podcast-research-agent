"""音频 vibrato 效果API"""

from fastapi import APIRouter
from pydantic import BaseModel

from echo.research.audio_vibrato import get_audio_vibrato_tool


router = APIRouter(prefix="/api/audio-vibrato", tags=["audio-vibrato"])


class VibratoRequest(BaseModel):
    signal: list[float]
    rate: float = 6.0
    depth: float = 0.01
    mix: float = 0.5


@router.post("/vibrato")
async def vibrato(request: VibratoRequest):
    tool = get_audio_vibrato_tool()
    return {"result": tool.vibrato(request.signal, request.rate, request.depth, request.mix)}