"""音频包络API"""

from fastapi import APIRouter
from pydantic import BaseModel

from echo.research.audio_envelope import get_audio_envelope_tool


router = APIRouter(prefix="/api/audio-envelope", tags=["audio-envelope"])


class EnvelopeRequest(BaseModel):
    signal: list[float]
    attack: float = 0.01
    release: float = 0.1
    sample_rate: float = 44100.0


@router.post("/envelope")
async def envelope(request: EnvelopeRequest):
    tool = get_audio_envelope_tool()
    return {"result": tool.attack_release(request.signal, request.attack, request.release, request.sample_rate)}