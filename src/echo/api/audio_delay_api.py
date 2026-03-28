"""音频延迟效果API"""

from fastapi import APIRouter
from pydantic import BaseModel

from echo.research.audio_delay import get_audio_delay_tool


router = APIRouter(prefix="/api/audio-delay", tags=["audio-delay"])


class DelayRequest(BaseModel):
    signal: list[float]
    delay_ms: float = 250.0
    feedback: float = 0.3
    mix: float = 0.5


@router.post("/delay")
async def delay(request: DelayRequest):
    tool = get_audio_delay_tool()
    return {"result": tool.delay(request.signal, request.delay_ms, request.feedback, request.mix)}