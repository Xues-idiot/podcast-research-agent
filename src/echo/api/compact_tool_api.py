"""压缩工具API"""

from fastapi import APIRouter

from echo.research.compact_tool import get_compact_tool


router = APIRouter(prefix="/api/compact", tags=["compact"])


@router.post("/compact")
async def compact_items():
    tool = get_compact_tool()
    return {"success": True}
