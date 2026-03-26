"""文本填充API"""

from fastapi import APIRouter

from echo.research.padding import get_text_padder


router = APIRouter(prefix="/api/pad", tags=["pad"])


@router.post("/left")
async def pad_left(text: str, width: int, char: str = " "):
    padder = get_text_padder()
    return {"result": padder.pad_left(text, width, char)}


@router.post("/right")
async def pad_right(text: str, width: int, char: str = " "):
    padder = get_text_padder()
    return {"result": padder.pad_right(text, width, char)}


@router.post("/center")
async def pad_center(text: str, width: int, char: str = " "):
    padder = get_text_padder()
    return {"result": padder.pad_center(text, width, char)}