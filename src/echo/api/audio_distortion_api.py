"""音频失真效果API"""

from fastapi import APIRouter
from pydantic import BaseModel

from echo.research.audio_distortion import get_audio_distortion_tool


router = APIRouter(prefix="/api/audio-distortion", tags=["audio-distortion"])


class DistortionRequest(BaseModel):
    signal: list[float]
    drive: float = 0.5
    mix: float = 0.5


@router.post("/distort")
async def distort(request: DistortionRequest):
    tool = get_audio_distortion_tool()
    return {"result": tool.distort(request.signal, request.drive, request.mix)}