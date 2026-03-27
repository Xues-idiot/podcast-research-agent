"""位运算API"""

from fastapi import APIRouter

from echo.research.bits_tool import get_bits_tool


router = APIRouter(prefix="/api/bits", tags=["bits"])


@router.post("/and")
async def bits_and(a: int, b: int):
    """位与"""
    tool = get_bits_tool()
    return {"result": tool.and_(a, b)}


@router.post("/or")
async def bits_or(a: int, b: int):
    """位或"""
    tool = get_bits_tool()
    return {"result": tool.or_(a, b)}


@router.post("/xor")
async def bits_xor(a: int, b: int):
    """位异或"""
    tool = get_bits_tool()
    return {"result": tool.xor(a, b)}


@router.post("/not")
async def bits_not(a: int):
    """位非"""
    tool = get_bits_tool()
    return {"result": tool.not_(a)}


@router.post("/lshift")
async def bits_lshift(a: int, b: int):
    """左移"""
    tool = get_bits_tool()
    return {"result": tool.lshift(a, b)}


@router.post("/rshift")
async def bits_rshift(a: int, b: int):
    """右移"""
    tool = get_bits_tool()
    return {"result": tool.rshift(a, b)}
