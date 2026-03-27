"""蹦床工具API"""

from fastapi import APIRouter

from echo.research.trampoline_tool import get_trampoline_tool


router = APIRouter(prefix="/api/trampoline", tags=["trampoline"])


@router.post("/bounce")
async def bounce_func(func: str, value: str):
    """蹦床调用"""
    tool = get_trampoline_tool()
    func_obj = eval(func)
    bounced = tool.bounce(func_obj)
    return {"result": bounced(value)}
