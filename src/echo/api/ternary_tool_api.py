"""三元表达式API"""

from fastapi import APIRouter

from echo.research.ternary_tool import get_ternary_tool


router = APIRouter(prefix="/api/ternary", tags=["ternary"])


@router.post("/if-then-else")
async def if_then_else(condition: bool, then_val, else_val):
    return {"result": get_ternary_tool().if_then_else(condition, then_val, else_val)}