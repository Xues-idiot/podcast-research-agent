"""音频颤音效果API"""

from fastapi import APIRouter
from pydantic import BaseModel

from echo.research.audio_tremolo import get_audio_tremolo_tool


router = APIRouter(prefix="/api/audio-tremolo", tags=["audio-tremolo"])


class TremoloRequest(BaseModel):
    signal: list[float]
    rate: float = 5.0
    depth: float = 0.5


@router.post("/tremolo")
async def tremolo(request: TremoloRequest):
    tool = get_audio_tremolo_tool()
    return {"result": tool.tremolo(request.signal, request.rate, request.depth)}