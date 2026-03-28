"""MIME类型检测API"""

from fastapi import APIRouter
from pydantic import BaseModel

from echo.research.mime_type_detect import get_mime_type_detect_tool


router = APIRouter(prefix="/api/mime-type-detect", tags=["mime-type-detect"])


class FileRequest(BaseModel):
    filename: str


@router.post("/from-extension")
async def from_extension(request: FileRequest):
    tool = get_mime_type_detect_tool()
    return {"result": tool.from_extension(request.filename)}


@router.post("/extension-from-mime")
async def extension_from_mime(request: FileRequest):
    tool = get_mime_type_detect_tool()
    return {"result": tool.extension_from_mime(request.filename)}


@router.post("/is-text")
async def is_text(request: FileRequest):
    tool = get_mime_type_detect_tool()
    return {"result": tool.is_text(request.filename)}


@router.post("/is-image")
async def is_image(request: FileRequest):
    tool = get_mime_type_detect_tool()
    return {"result": tool.is_image(request.filename)}


@router.post("/is-audio")
async def is_audio(request: FileRequest):
    tool = get_mime_type_detect_tool()
    return {"result": tool.is_audio(request.filename)}


@router.post("/is-video")
async def is_video(request: FileRequest):
    tool = get_mime_type_detect_tool()
    return {"result": tool.is_video(request.filename)}