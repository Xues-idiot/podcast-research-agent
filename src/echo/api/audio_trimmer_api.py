"""音频裁剪API"""

from fastapi import APIRouter
from pydantic import BaseModel

from echo.research.audio_trimmer import get_audio_trimmer_tool


router = APIRouter(prefix="/api/audio-trimmer", tags=["audio-trimmer"])


class TrimRequest(BaseModel):
    signal: list[float]
    start: int = 0
    end: int = -1


@router.post("/trim")
async def trim(request: TrimRequest):
    tool = get_audio_trimmer_tool()
    return {"result": tool.trim(request.signal, request.start, request.end)}