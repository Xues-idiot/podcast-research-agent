"""音频时间拉伸API"""

from fastapi import APIRouter
from pydantic import BaseModel

from echo.research.audio_time_stretch import get_audio_time_stretch_tool


router = APIRouter(prefix="/api/audio-time-stretch", tags=["audio-time-stretch"])


class TimeStretchRequest(BaseModel):
    signal: list[float]
    factor: float = 1.0


@router.post("/time-stretch")
async def time_stretch(request: TimeStretchRequest):
    tool = get_audio_time_stretch_tool()
    return {"result": tool.time_stretch(request.signal, request.factor)}