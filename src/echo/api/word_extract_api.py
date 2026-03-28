"""单词提取API"""

from fastapi import APIRouter
from pydantic import BaseModel

from echo.research.word_extract import get_word_extract_tool


router = APIRouter(prefix="/api/word-extract", tags=["word-extract"])


class ExtractRequest(BaseModel):
    text: str


@router.post("/extract")
async def extract(request: ExtractRequest):
    tool = get_word_extract_tool()
    return {"words": tool.extract_words(request.text)}


@router.post("/unique")
async def unique(request: ExtractRequest):
    tool = get_word_extract_tool()
    return {"words": tool.extract_unique_words(request.text)}


@router.post("/count")
async def count(request: ExtractRequest):
    tool = get_word_extract_tool()
    return {"count": tool.word_count(request.text)}