"""音频立体声扩展API"""

from fastapi import APIRouter
from pydantic import BaseModel

from echo.research.audio_stereo_widen import get_audio_stereo_widen_tool


router = APIRouter(prefix="/api/audio-stereo-widen", tags=["audio-stereo-widen"])


class WidenRequest(BaseModel):
    left: list[float]
    right: list[float]
    amount: float = 0.5


@router.post("/widen")
async def widen(request: WidenRequest):
    tool = get_audio_stereo_widen_tool()
    new_left, new_right = tool.widen(request.left, request.right, request.amount)
    return {"left": new_left, "right": new_right}