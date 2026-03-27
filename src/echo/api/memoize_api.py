"""记忆化API"""

from fastapi import APIRouter

from echo.research.memoize_tool import get_memoize_tool


router = APIRouter(prefix="/api/memoize", tags=["memoize"])


@router.post("/memoize")
async def memoize(func, *args, **kwargs):
    return {"result": get_memoize_tool().memoize(func, *args, **kwargs)}


@router.post("/clear")
async def clear():
    get_memoize_tool().clear()
    return {"success": True}