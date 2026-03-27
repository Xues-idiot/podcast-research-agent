"""惰性计算API"""

from fastapi import APIRouter

from echo.research.lazy_tool import get_lazy_tool


router = APIRouter(prefix="/api/lazy", tags=["lazy"])


@router.post("/memoize")
async def memoize_test(func: str, value: str):
    """记忆化测试"""
    tool = get_lazy_tool()
    func_obj = eval(func)
    memoized = tool.memoize(func_obj)
    return {"result": memoized(value)}
