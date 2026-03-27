"""文本填充API"""

from fastapi import APIRouter

from echo.research.pad_text import get_pad_text


router = APIRouter(prefix="/api/pad", tags=["pad"])


@router.post("/left")
async def pad_left(text: str, width: int, char: str = " "):
    """左填充"""
    tool = get_pad_text()
    return {"result": tool.pad_left(text, width, char)}


@router.post("/right")
async def pad_right(text: str, width: int, char: str = " "):
    """右填充"""
    tool = get_pad_text()
    return {"result": tool.pad_right(text, width, char)}


@router.post("/center")
async def pad_center(text: str, width: int, char: str = " "):
    """居中填充"""
    tool = get_pad_text()
    return {"result": tool.pad_center(text, width, char)}
