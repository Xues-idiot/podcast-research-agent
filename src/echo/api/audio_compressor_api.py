"""音频压缩器API"""

from fastapi import APIRouter
from pydantic import BaseModel

from echo.research.audio_compressor import get_audio_compressor_tool


router = APIRouter(prefix="/api/audio-compressor", tags=["audio-compressor"])


class CompressRequest(BaseModel):
    signal: list[float]
    threshold: float = 0.5
    ratio: float = 4.0
    makeup_gain: float = 1.0


@router.post("/compress")
async def compress(request: CompressRequest):
    tool = get_audio_compressor_tool()
    return {"result": tool.compress(request.signal, request.threshold, request.ratio, request.makeup_gain)}