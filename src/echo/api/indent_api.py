"""缩进API"""

from fastapi import APIRouter

from echo.research.indent import get_indent_tool


router = APIRouter(prefix="/api/indent", tags=["indent"])


@router.post("/indent")
async def indent(text: str, spaces: int = 4):
    """缩进"""
    tool = get_indent_tool()
    return {"result": tool.indent(text, spaces)}


@router.post("/unindent")
async def unindent(text: str, spaces: int = 4):
    """取消缩进"""
    tool = get_indent_tool()
    return {"result": tool.unindent(text, spaces)}
