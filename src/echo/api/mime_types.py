"""MIME类型API"""

from fastapi import APIRouter

from echo.research.mime_types import get_mime_types_tool


router = APIRouter(prefix="/api/mime", tags=["mime"])


@router.get("/type")
async def get_mime_type(filename: str):
    return {"mime_type": get_mime_types_tool().get_mime_type(filename)}


@router.get("/extension")
async def get_extension(mime_type: str):
    return {"extension": get_mime_types_tool().get_extension(mime_type)}