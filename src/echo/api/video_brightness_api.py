"""视频亮度调整API"""

from fastapi import APIRouter
from pydantic import BaseModel

from echo.research.video_brightness import get_video_brightness_tool


router = APIRouter(prefix="/api/video-brightness", tags=["video-brightness"])


class BrightnessRequest(BaseModel):
    frames: list[list[list[float]]]
    factor: float = 1.0


@router.post("/brightness")
async def brightness(request: BrightnessRequest):
    tool = get_video_brightness_tool()
    return {"result": tool.brightness(request.frames, request.factor)}