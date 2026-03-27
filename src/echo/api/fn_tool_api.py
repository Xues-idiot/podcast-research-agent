"""函数工具API"""

from fastapi import APIRouter

from echo.research.fn_tool import get_fn_tool


router = APIRouter(prefix="/api/fn", tags=["fn"])


@router.post("/apply")
async def apply_func(func: str, args: list, kwargs: dict = None):
    """应用函数"""
    tool = get_fn_tool()
    func_obj = eval(func)
    return {"result": tool.apply(func_obj, tuple(args), kwargs or {})}


@router.post("/juxt")
async def juxt_funcs(funcs: list, value: str):
    """并行调用"""
    tool = get_fn_tool()
    func_objs = [eval(f) for f in funcs]
    return {"result": tool.juxt(*func_objs)(value)}
