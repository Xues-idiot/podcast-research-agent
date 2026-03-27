"""文本连接API"""

from fastapi import APIRouter

from echo.research.text_joiner import get_text_joiner


router = APIRouter(prefix="/api/join", tags=["join"])


@router.post("/lines")
async def join_lines(lines: list[str], separator: str = "\n"):
    return {"result": get_text_joiner().join_lines(lines, separator)}


@router.post("/with_space")
async def join_with_space(parts: list[str]):
    return {"result": get_text_joiner().join_with_space(parts)}


@router.post("/paragraphs")
async def join_paragraphs(paragraphs: list[str]):
    return {"result": get_text_joiner().join_paragraphs(paragraphs)}