"""视频模糊API"""

from fastapi import APIRouter
from pydantic import BaseModel

from echo.research.video_blur import get_video_blur_tool


router = APIRouter(prefix="/api/video-blur", tags=["video-blur"])


class BlurRequest(BaseModel):
    frames: list[list[list[float]]]
    radius: int = 3


@router.post("/blur")
async def blur(request: BlurRequest):
    tool = get_video_blur_tool()
    return {"result": tool.blur(request.frames, request.radius)}