"""Slug生成API"""

from fastapi import APIRouter
from pydantic import BaseModel
from typing import List

from echo.research.slug_maker import get_slug_maker_tool


router = APIRouter(prefix="/api/slug-maker", tags=["slug-maker"])


class SlugRequest(BaseModel):
    text: str
    max_length: int = 50


@router.post("/make")
async def make(request: SlugRequest):
    tool = get_slug_maker_tool()
    return {"result": tool.make(request.text, request.max_length)}


class WordsToSlugRequest(BaseModel):
    words: List[str]
    separator: str = "-"


@router.post("/from-words")
async def from_words(request: WordsToSlugRequest):
    tool = get_slug_maker_tool()
    return {"result": tool.make_from_words(request.words, request.separator)}