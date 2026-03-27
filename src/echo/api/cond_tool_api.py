"""条件表达式API"""

from fastapi import APIRouter

from echo.research.cond_tool import get_cond_tool


router = APIRouter(prefix="/api/cond", tags=["cond"])


@router.post("/if")
async def cond_if(condition: bool, then_val: str, else_val: str):
    """三元表达式"""
    tool = get_cond_tool()
    return {"result": tool.if_(condition, then_val, else_val)}
