"""音频频谱分析API"""

from fastapi import APIRouter
from pydantic import BaseModel

from echo.research.audio_spectrum import get_audio_spectrum_tool


router = APIRouter(prefix="/api/audio-spectrum", tags=["audio-spectrum"])


class SpectrumRequest(BaseModel):
    signal: list[float]


@router.post("/spectrum")
async def spectrum(request: SpectrumRequest):
    tool = get_audio_spectrum_tool()
    return {"result": tool.spectrum(request.signal)}