"""视频叠加API"""

from fastapi import APIRouter
from pydantic import BaseModel

from echo.research.video_overlay import get_video_overlay_tool


router = APIRouter(prefix="/api/video-overlay", tags=["video-overlay"])


class OverlayRequest(BaseModel):
    base: list[list[list[float]]]
    overlay: list[list[list[float]]]
    x: int = 0
    y: int = 0
    alpha: float = 0.5


@router.post("/overlay")
async def overlay(request: OverlayRequest):
    tool = get_video_overlay_tool()
    return {"result": tool.overlay(request.base, request.overlay, request.x, request.y, request.alpha)}