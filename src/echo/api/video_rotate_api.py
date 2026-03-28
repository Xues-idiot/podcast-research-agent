"""视频旋转API"""

from fastapi import APIRouter
from pydantic import BaseModel

from echo.research.video_rotate import get_video_rotate_tool


router = APIRouter(prefix="/api/video-rotate", tags=["video-rotate"])


class Rotate90Request(BaseModel):
    frames: list[list[list[float]]]
    clockwise: bool = True


class Rotate180Request(BaseModel):
    frames: list[list[list[float]]]


class Rotate270Request(BaseModel):
    frames: list[list[list[float]]]


@router.post("/rotate-90")
async def rotate_90(request: Rotate90Request):
    tool = get_video_rotate_tool()
    return {"result": tool.rotate_90(request.frames, request.clockwise)}


@router.post("/rotate-180")
async def rotate_180(request: Rotate180Request):
    tool = get_video_rotate_tool()
    return {"result": tool.rotate_180(request.frames)}


@router.post("/rotate-270")
async def rotate_270(request: Rotate270Request):
    tool = get_video_rotate_tool()
    return {"result": tool.rotate_270(request.frames)}