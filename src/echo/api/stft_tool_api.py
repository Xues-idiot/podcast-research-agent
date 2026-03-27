"""STFT API"""

from fastapi import APIRouter
from pydantic import BaseModel

from echo.research.stft_tool import get_stft_tool


router = APIRouter(prefix="/api/stft", tags=["stft"])


class StftRequest(BaseModel):
    signal: list
    window_size: int = 1024
    hop_size: int = 512


@router.post("/transform")
async def transform(request: StftRequest):
    return {"result": get_stft_tool().stft(request.signal, request.window_size, request.hop_size)}
