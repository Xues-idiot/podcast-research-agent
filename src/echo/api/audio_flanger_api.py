"""音频镶边效果API"""

from fastapi import APIRouter
from pydantic import BaseModel

from echo.research.audio_flanger import get_audio_flanger_tool


router = APIRouter(prefix="/api/audio-flanger", tags=["audio-flanger"])


class FlangerRequest(BaseModel):
    signal: list[float]
    depth: float = 0.005
    rate: float = 0.5
    mix: float = 0.5


@router.post("/flanger")
async def flanger(request: FlangerRequest):
    tool = get_audio_flanger_tool()
    return {"result": tool.flanger(request.signal, request.depth, request.rate, request.mix)}