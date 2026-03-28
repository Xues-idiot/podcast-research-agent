"""字符串包裹API"""

from fastapi import APIRouter
from pydantic import BaseModel

from echo.research.string_wrap import get_string_wrap_tool


router = APIRouter(prefix="/api/string-wrap", tags=["string-wrap"])


class WrapRequest(BaseModel):
    text: str
    width: int = 80


@router.post("/wrap")
async def wrap(request: WrapRequest):
    tool = get_string_wrap_tool()
    return {"result": tool.wrap(request.text, request.width)}


@router.post("/wrap-words")
async def wrap_words(request: WrapRequest):
    tool = get_string_wrap_tool()
    return {"result": tool.wrap_words(request.text, request.width)}


@router.post("/indent")
async def indent(request: WrapRequest):
    tool = get_string_wrap_tool()
    return {"result": tool.indent(request.text)}