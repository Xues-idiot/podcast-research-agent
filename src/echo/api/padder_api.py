"""填充API"""

from fastapi import APIRouter

from echo.research.padder_tool import get_padder_tool


router = APIRouter(prefix="/api/padder", tags=["padder"])


@router.post("/pad-left")
async def pad_left(text: str, width: int, char: str = " "):
    return {"result": get_padder_tool().pad_left(text, width, char)}


@router.post("/pad-right")
async def pad_right(text: str, width: int, char: str = " "):
    return {"result": get_padder_tool().pad_right(text, width, char)}