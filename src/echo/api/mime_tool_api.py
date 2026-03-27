"""MIME类型API"""

from fastapi import APIRouter

from echo.research.mime_tool import get_mime_tool


router = APIRouter(prefix="/api/mime", tags=["mime"])


@router.post("/type")
async def get_type(filename: str):
    """获取MIME类型"""
    tool = get_mime_tool()
    return {"type": tool.get_type(filename)}
