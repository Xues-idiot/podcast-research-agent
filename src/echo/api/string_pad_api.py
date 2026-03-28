"""字符串填充API"""

from fastapi import APIRouter
from pydantic import BaseModel

from echo.research.string_pad import get_string_pad_tool


router = APIRouter(prefix="/api/string-pad", tags=["string-pad"])


class PadRequest(BaseModel):
    text: str
    width: int
    char: str = " "


@router.post("/left")
async def pad_left(request: PadRequest):
    tool = get_string_pad_tool()
    return {"result": tool.pad_left(request.text, request.width, request.char)}


@router.post("/right")
async def pad_right(request: PadRequest):
    tool = get_string_pad_tool()
    return {"result": tool.pad_right(request.text, request.width, request.char)}


@router.post("/center")
async def center(request: PadRequest):
    tool = get_string_pad_tool()
    return {"result": tool.center(request.text, request.width, request.char)}