"""布尔工具API"""

from fastapi import APIRouter

from echo.research.bool_tool import get_bool_tool


router = APIRouter(prefix="/api/bool", tags=["bool"])


@router.post("/and")
async def bool_and(a: bool, b: bool):
    """逻辑与"""
    tool = get_bool_tool()
    return {"result": tool.and_(a, b)}


@router.post("/or")
async def bool_or(a: bool, b: bool):
    """逻辑或"""
    tool = get_bool_tool()
    return {"result": tool.or_(a, b)}


@router.post("/not")
async def bool_not(a: bool):
    """逻辑非"""
    tool = get_bool_tool()
    return {"result": tool.not_(a)}


@router.post("/xor")
async def bool_xor(a: bool, b: bool):
    """逻辑异或"""
    tool = get_bool_tool()
    return {"result": tool.xor(a, b)}
