"""视频稳定API"""

from fastapi import APIRouter
from pydantic import BaseModel

from echo.research.video_stabilize import get_video_stabilize_tool


router = APIRouter(prefix="/api/video-stabilize", tags=["video-stabilize"])


class StabilizeRequest(BaseModel):
    frames: list[list[list[float]]]
    strength: float = 0.5


@router.post("/stabilize")
async def stabilize(request: StabilizeRequest):
    tool = get_video_stabilize_tool()
    return {"result": tool.stabilize(request.frames, request.strength)}