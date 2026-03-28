"""视频翻转API"""

from fastapi import APIRouter
from pydantic import BaseModel

from echo.research.video_flip import get_video_flip_tool


router = APIRouter(prefix="/api/video-flip", tags=["video-flip"])


class FlipRequest(BaseModel):
    frames: list[list[list[float]]]


@router.post("/flip-horizontal")
async def flip_horizontal(request: FlipRequest):
    tool = get_video_flip_tool()
    return {"result": tool.flip_horizontal(request.frames)}


@router.post("/flip-vertical")
async def flip_vertical(request: FlipRequest):
    tool = get_video_flip_tool()
    return {"result": tool.flip_vertical(request.frames)}