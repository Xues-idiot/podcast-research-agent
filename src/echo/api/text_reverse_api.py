"""文本反转API"""

from fastapi import APIRouter
from pydantic import BaseModel

from echo.research.text_reverse import get_text_reverse_tool


router = APIRouter(prefix="/api/text-reverse", tags=["text-reverse"])


class ReverseRequest(BaseModel):
    text: str


@router.post("/string")
async def reverse_string(request: ReverseRequest):
    tool = get_text_reverse_tool()
    return {"result": tool.reverse_string(request.text)}


@router.post("/words")
async def reverse_words(request: ReverseRequest):
    tool = get_text_reverse_tool()
    return {"result": tool.reverse_words(request.text)}


@router.post("/lines")
async def reverse_lines(request: ReverseRequest):
    tool = get_text_reverse_tool()
    return {"result": tool.reverse_lines(request.text)}