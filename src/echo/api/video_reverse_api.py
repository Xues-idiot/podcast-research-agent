"""视频反转API"""

from fastapi import APIRouter
from pydantic import BaseModel

from echo.research.video_reverse import get_video_reverse_tool


router = APIRouter(prefix="/api/video-reverse", tags=["video-reverse"])


class ReverseRequest(BaseModel):
    frames: list[list[list[float]]]


@router.post("/reverse")
async def reverse(request: ReverseRequest):
    tool = get_video_reverse_tool()
    return {"result": tool.reverse(request.frames)}