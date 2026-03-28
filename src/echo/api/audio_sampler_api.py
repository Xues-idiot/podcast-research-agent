"""音频采样API"""

from fastapi import APIRouter
from pydantic import BaseModel

from echo.research.audio_sampler import get_audio_sampler_tool


router = APIRouter(prefix="/api/audio-sampler", tags=["audio-sampler"])


class SampleRequest(BaseModel):
    signal: list[float]
    rate: float = 1.0


@router.post("/sample")
async def sample(request: SampleRequest):
    tool = get_audio_sampler_tool()
    return {"result": tool.sample(request.signal, request.rate)}