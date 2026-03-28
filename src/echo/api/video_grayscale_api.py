"""视频灰度API"""

from fastapi import APIRouter
from pydantic import BaseModel

from echo.research.video_grayscale import get_video_grayscale_tool


router = APIRouter(prefix="/api/video-grayscale", tags=["video-grayscale"])


class GrayscaleRequest(BaseModel):
    frames: list[list[list[float]]]


@router.post("/grayscale")
async def grayscale(request: GrayscaleRequest):
    tool = get_video_grayscale_tool()
    return {"result": tool.grayscale(request.frames)}