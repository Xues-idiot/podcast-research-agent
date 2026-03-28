"""音频循环API"""

from fastapi import APIRouter
from pydantic import BaseModel

from echo.research.audio_looper import get_audio_looper_tool


router = APIRouter(prefix="/api/audio-looper", tags=["audio-looper"])


class LoopRequest(BaseModel):
    signal: list[float]
    start: int = 0
    end: int = -1
    count: int = 1


@router.post("/loop")
async def loop(request: LoopRequest):
    tool = get_audio_looper_tool()
    return {"result": tool.loop(request.signal, request.start, request.end, request.count)}