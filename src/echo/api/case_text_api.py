"""大小写转换API"""

from fastapi import APIRouter

from echo.research.case_text import get_case_text


router = APIRouter(prefix="/api/case", tags=["case"])


@router.post("/upper")
async def upper(text: str):
    """转大写"""
    tool = get_case_text()
    return {"result": tool.upper(text)}


@router.post("/lower")
async def lower(text: str):
    """转小写"""
    tool = get_case_text()
    return {"result": tool.lower(text)}


@router.post("/swap")
async def swap(text: str):
    """大小写互换"""
    tool = get_case_text()
    return {"result": tool.swap(text)}


@router.post("/camel")
async def camel(text: str):
    """驼峰命名"""
    tool = get_case_text()
    return {"result": tool.camel(text)}


@router.post("/snake")
async def snake(text: str):
    """蛇形命名"""
    tool = get_case_text()
    return {"result": tool.snake(text)}
