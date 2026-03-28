"""音频位深压缩API"""

from fastapi import APIRouter
from pydantic import BaseModel

from echo.research.audio_bitcrush import get_audio_bitcrush_tool


router = APIRouter(prefix="/api/audio-bitcrush", tags=["audio-bitcrush"])


class BitcrushRequest(BaseModel):
    signal: list[float]
    bits: int = 8
    mix: float = 0.5


@router.post("/bitcrush")
async def bitcrush(request: BitcrushRequest):
    tool = get_audio_bitcrush_tool()
    return {"result": tool.bitcrush(request.signal, request.bits, request.mix)}