"""视频裁剪API"""

from fastapi import APIRouter
from pydantic import BaseModel

from echo.research.video_crop import get_video_crop_tool


router = APIRouter(prefix="/api/video-crop", tags=["video-crop"])


class CropRequest(BaseModel):
    frames: list[list[list[float]]]
    x: int
    y: int
    width: int
    height: int


@router.post("/crop")
async def crop(request: CropRequest):
    tool = get_video_crop_tool()
    return {"result": tool.crop(request.frames, request.x, request.y, request.width, request.height)}