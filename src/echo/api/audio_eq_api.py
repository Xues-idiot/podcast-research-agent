"""音频均衡器API"""

from fastapi import APIRouter
from pydantic import BaseModel

from echo.research.audio_eq import get_audio_eq_tool


router = APIRouter(prefix="/api/audio-eq", tags=["audio-eq"])


class EqRequest(BaseModel):
    signal: list[float]
    low: float = 1.0
    mid: float = 1.0
    high: float = 1.0


@router.post("/equalize")
async def equalize(request: EqRequest):
    tool = get_audio_eq_tool()
    return {"result": tool.equalize(request.signal, request.low, request.mid, request.high)}