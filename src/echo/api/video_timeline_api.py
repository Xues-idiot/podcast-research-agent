"""视频时间线API"""

from fastapi import APIRouter
from pydantic import BaseModel

from echo.research.video_timeline import get_video_timeline_tool


router = APIRouter(prefix="/api/video-timeline", tags=["video-timeline"])


class TrimRequest(BaseModel):
    frames: list[list[list[float]]]
    start: int
    end: int


class SpliceRequest(BaseModel):
    clips: list[list[list[list[float]]]]
    transitions: list[int]


@router.post("/trim")
async def trim(request: TrimRequest):
    tool = get_video_timeline_tool()
    return {"result": tool.trim(request.frames, request.start, request.end)}


@router.post("/splice")
async def splice(request: SpliceRequest):
    tool = get_video_timeline_tool()
    return {"result": tool.splice(request.clips, request.transitions)}