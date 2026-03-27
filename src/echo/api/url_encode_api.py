"""URL编码API"""

from fastapi import APIRouter

from echo.research.url_encode import get_url_encode


router = APIRouter(prefix="/api/url", tags=["url"])


@router.post("/encode")
async def encode(text: str):
    """URL编码"""
    tool = get_url_encode()
    return {"result": tool.encode(text)}


@router.post("/decode")
async def decode(text: str):
    """URL解码"""
    tool = get_url_encode()
    return {"result": tool.decode(text)}
