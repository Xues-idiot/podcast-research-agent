"""音频淡入淡出API"""

from fastapi import APIRouter
from pydantic import BaseModel

from echo.research.audio_fade import get_audio_fade_tool


router = APIRouter(prefix="/api/audio-fade", tags=["audio-fade"])


class FadeRequest(BaseModel):
    signal: list[float]
    samples: int = 1000


@router.post("/fade-in")
async def fade_in(request: FadeRequest):
    tool = get_audio_fade_tool()
    return {"result": tool.fade_in(request.signal, request.samples)}


@router.post("/fade-out")
async def fade_out(request: FadeRequest):
    tool = get_audio_fade_tool()
    return {"result": tool.fade_out(request.signal, request.samples)}