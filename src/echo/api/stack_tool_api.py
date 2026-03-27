"""栈API"""

from fastapi import APIRouter

from echo.research.stack_tool import get_stack_tool


router = APIRouter(prefix="/api/stack", tags=["stack"])


@router.post("/peek")
async def peek(stack: list):
    """查看栈顶"""
    tool = get_stack_tool()
    return {"item": tool.peek(stack)}


@router.post("/size")
async def size(stack: list):
    """获取大小"""
    tool = get_stack_tool()
    return {"size": tool.size(stack)}
