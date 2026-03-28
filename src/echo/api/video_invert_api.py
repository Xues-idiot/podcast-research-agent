"""视频反色API"""

from fastapi import APIRouter
from pydantic import BaseModel

from echo.research.video_invert import get_video_invert_tool


router = APIRouter(prefix="/api/video-invert", tags=["video-invert"])


class InvertRequest(BaseModel):
    frames: list[list[list[float]]]


@router.post("/invert")
async def invert(request: InvertRequest):
    tool = get_video_invert_tool()
    return {"result": tool.invert(request.frames)}