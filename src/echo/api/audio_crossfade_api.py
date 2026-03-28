"""音频交叉淡入淡出API"""

from fastapi import APIRouter
from pydantic import BaseModel

from echo.research.audio_crossfade import get_audio_crossfade_tool


router = APIRouter(prefix="/api/audio-crossfade", tags=["audio-crossfade"])


class CrossfadeRequest(BaseModel):
    a: list[float]
    b: list[float]
    fade_points: int = 1000


@router.post("/crossfade")
async def crossfade(request: CrossfadeRequest):
    tool = get_audio_crossfade_tool()
    return {"result": tool.crossfade(request.a, request.b, request.fade_points)}