"""HTML编码API"""

from fastapi import APIRouter

from echo.research.html_encode import get_html_encode


router = APIRouter(prefix="/api/html", tags=["html"])


@router.post("/encode")
async def encode(text: str):
    """HTML编码"""
    tool = get_html_encode()
    return {"result": tool.encode(text)}


@router.post("/decode")
async def decode(text: str):
    """HTML解码"""
    tool = get_html_encode()
    return {"result": tool.decode(text)}
