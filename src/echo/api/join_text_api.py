"""连接文本API"""

from fastapi import APIRouter

from echo.research.join_text import get_join_text


router = APIRouter(prefix="/api/join", tags=["join"])


@router.post("/join")
async def join_items(items: list, delimiter: str = " "):
    """连接"""
    tool = get_join_text()
    return {"result": tool.join(items, delimiter)}
