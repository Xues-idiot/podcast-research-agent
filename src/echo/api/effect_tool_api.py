"""副作用API"""

from fastapi import APIRouter

from echo.research.effect_tool import get_effect_tool


router = APIRouter(prefix="/api/effect", tags=["effect"])


@router.post("/trace")
async def trace_value(label: str, value: str):
    """追踪值"""
    tool = get_effect_tool()
    return {"result": tool.trace(label, value)}
