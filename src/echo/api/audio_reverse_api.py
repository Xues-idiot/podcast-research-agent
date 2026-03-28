"""音频反转API"""

from fastapi import APIRouter
from pydantic import BaseModel

from echo.research.audio_reverse import get_audio_reverse_tool


router = APIRouter(prefix="/api/audio-reverse", tags=["audio-reverse"])


class ReverseRequest(BaseModel):
    signal: list[float]


@router.post("/reverse")
async def reverse(request: ReverseRequest):
    tool = get_audio_reverse_tool()
    return {"result": tool.reverse(request.signal)}