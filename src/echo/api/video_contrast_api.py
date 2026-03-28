"""视频对比度调整API"""

from fastapi import APIRouter
from pydantic import BaseModel

from echo.research.video_contrast import get_video_contrast_tool


router = APIRouter(prefix="/api/video-contrast", tags=["video-contrast"])


class ContrastRequest(BaseModel):
    frames: list[list[list[float]]]
    factor: float = 1.0


@router.post("/contrast")
async def contrast(request: ContrastRequest):
    tool = get_video_contrast_tool()
    return {"result": tool.contrast(request.frames, request.factor)}