"""视频缩放API"""

from fastapi import APIRouter
from pydantic import BaseModel

from echo.research.video_scale import get_video_scale_tool


router = APIRouter(prefix="/api/video-scale", tags=["video-scale"])


class ScaleRequest(BaseModel):
    frames: list[list[list[float]]]
    target_height: int
    target_width: int


@router.post("/scale")
async def scale(request: ScaleRequest):
    tool = get_video_scale_tool()
    return {"result": tool.scale(request.frames, (request.target_height, request.target_width))}