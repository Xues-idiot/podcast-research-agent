"""音频自动哇音效果API"""

from fastapi import APIRouter
from pydantic import BaseModel

from echo.research.audio_autowah import get_audio_autowah_tool


router = APIRouter(prefix="/api/audio-autowah", tags=["audio-autowah"])


class AutowahRequest(BaseModel):
    signal: list[float]
    cutoff: float = 0.5
    resonance: float = 2.0
    mix: float = 0.5


@router.post("/autowah")
async def autowah(request: AutowahRequest):
    tool = get_audio_autowah_tool()
    return {"result": tool.autowah(request.signal, request.cutoff, request.resonance, request.mix)}