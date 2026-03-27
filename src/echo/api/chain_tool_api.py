"""链式调用API"""

from fastapi import APIRouter

from echo.research.chain_tool import get_chain_tool


router = APIRouter(prefix="/api/chain", tags=["chain"])


@router.post("/tap")
async def chain_tap(value: str, func: str):
    """链式tap"""
    tool = get_chain_tool()
    func_obj = eval(func)
    return {"result": tool.tap(value, func_obj)}
