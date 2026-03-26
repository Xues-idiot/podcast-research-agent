"""文本前缀API"""

from fastapi import APIRouter

from echo.research.prefixer import get_text_prefixer


router = APIRouter(prefix="/api/prefix", tags=["prefix"])


@router.post("/line_numbers")
async def add_line_numbers(text: str, start: int = 1):
    prefixer = get_text_prefixer()
    return {"result": prefixer.add_line_numbers(text, start)}


@router.post("/bullets")
async def add_bullets(text: str, bullet: str = "-"):
    prefixer = get_text_prefixer()
    return {"result": prefixer.add_bullet_points(text, bullet)}


@router.post("/header")
async def add_header(text: str, header: str = "=", width: int = 80):
    prefixer = get_text_prefixer()
    return {"result": prefixer.add_header_line(text, header, width)}