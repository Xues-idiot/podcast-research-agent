"""截断API"""

from fastapi import APIRouter

from echo.research.truncate import get_truncate_tool


router = APIRouter(prefix="/api/truncate", tags=["truncate"])


@router.post("/truncate")
async def truncate(text: str, length: int, suffix: str = "..."):
    """截断"""
    tool = get_truncate_tool()
    return {"result": tool.truncate(text, length, suffix)}
