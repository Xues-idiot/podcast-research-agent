"""视频复古色调API"""

from fastapi import APIRouter
from pydantic import BaseModel

from echo.research.video_sepia import get_video_sepia_tool


router = APIRouter(prefix="/api/video-sepia", tags=["video-sepia"])


class SepiaRequest(BaseModel):
    frames: list[list[list[float]]]


@router.post("/sepia")
async def sepia(request: SepiaRequest):
    tool = get_video_sepia_tool()
    return {"result": tool.sepia(request.frames)}