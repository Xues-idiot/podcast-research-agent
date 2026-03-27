"""编码转换API"""

from fastapi import APIRouter

from echo.research.encoding_tool import get_encoding_tool


router = APIRouter(prefix="/api/encoding", tags=["encoding"])


@router.post("/encode")
async def encode(text: str, encoding: str = "utf-8"):
    """编码"""
    tool = get_encoding_tool()
    return {"result": tool.encode(text, encoding)}


@router.post("/decode")
async def decode(data: str, encoding: str = "utf-8"):
    """解码"""
    tool = get_encoding_tool()
    import base64
    return {"result": tool.decode(base64.b64decode(data), encoding)}
