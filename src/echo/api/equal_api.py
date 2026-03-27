"""相等检查API"""

from fastapi import APIRouter

from echo.research.equal_tool import get_equal_tool


router = APIRouter(prefix="/api/equal", tags=["equal"])


@router.post("/equal")
async def equal(a, b):
    return {"result": get_equal_tool().equal(a, b)}