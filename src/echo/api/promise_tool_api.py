"""Promise工具API"""

from fastapi import APIRouter

from echo.research.promise_tool import get_promise_tool


router = APIRouter(prefix="/api/promise", tags=["promise"])


@router.post("/resolve")
async def resolve(value: str):
    """解析值"""
    tool = get_promise_tool()
    return {"result": tool.resolve(value)}


@router.post("/reject")
async def reject(error: str):
    """拒绝错误"""
    tool = get_promise_tool()
    return {"error": tool.reject(Exception(error))}
