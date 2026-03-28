"""音频合唱效果API"""

from fastapi import APIRouter
from pydantic import BaseModel

from echo.research.audio_chorus import get_audio_chorus_tool


router = APIRouter(prefix="/api/audio-chorus", tags=["audio-chorus"])


class ChorusRequest(BaseModel):
    signal: list[float]
    depth: float = 0.003
    rate: float = 1.5
    mix: float = 0.5


@router.post("/chorus")
async def chorus(request: ChorusRequest):
    tool = get_audio_chorus_tool()
    return {"result": tool.chorus(request.signal, request.depth, request.rate, request.mix)}