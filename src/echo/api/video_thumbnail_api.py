"""视频缩略图提取API"""

from fastapi import APIRouter
from pydantic import BaseModel

from echo.research.video_thumbnail import get_video_thumbnail_tool


router = APIRouter(prefix="/api/video-thumbnail", tags=["video-thumbnail"])


class ExtractRequest(BaseModel):
    frames: list[list[list[float]]]
    indices: list[int]


@router.post("/extract")
async def extract(request: ExtractRequest):
    tool = get_video_thumbnail_tool()
    return {"result": tool.extract(request.frames, request.indices)}