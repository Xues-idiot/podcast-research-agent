"""去重工具API"""

from fastapi import APIRouter

from echo.research.distinct_tool import get_distinct_tool


router = APIRouter(prefix="/api/distinct", tags=["distinct"])


@router.post("/distinct")
async def distinct_items():
    tool = get_distinct_tool()
    return {"success": True}
