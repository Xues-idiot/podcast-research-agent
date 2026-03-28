"""音频限制器API"""

from fastapi import APIRouter
from pydantic import BaseModel

from echo.research.audio_limiter import get_audio_limiter_tool


router = APIRouter(prefix="/api/audio-limiter", tags=["audio-limiter"])


class LimitRequest(BaseModel):
    signal: list[float]
    threshold: float = 0.9


@router.post("/limit")
async def limit(request: LimitRequest):
    tool = get_audio_limiter_tool()
    return {"result": tool.limit(request.signal, request.threshold)}