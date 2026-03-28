"""音频归一化API"""

from fastapi import APIRouter
from pydantic import BaseModel

from echo.research.audio_normalize import get_audio_normalize_tool


router = APIRouter(prefix="/api/audio-normalize", tags=["audio-normalize"])


class NormalizeRequest(BaseModel):
    signal: list[float]
    target: float = 1.0


@router.post("/normalize")
async def normalize(request: NormalizeRequest):
    tool = get_audio_normalize_tool()
    return {"result": tool.normalize(request.signal, request.target)}