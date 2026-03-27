"""行号API"""

from fastapi import APIRouter

from echo.research.line_numberer import get_line_numberer


router = APIRouter(prefix="/api/linenumber", tags=["linenumber"])


@router.post("/add")
async def add_line_numbers(text: str, start: int = 1, zero_pad: int = 0):
    numberer = get_line_numberer()
    return {"result": numberer.add_line_numbers(text, start, zero_pad=zero_pad)}


@router.post("/remove")
async def remove_line_numbers(text: str):
    numberer = get_line_numberer()
    return {"result": numberer.remove_line_numbers(text)}