"""长度API"""

from fastapi import APIRouter

from echo.research.length_list import get_length_list


router = APIRouter(prefix="/api/length", tags=["length"])


@router.post("/count")
async def length_count(items: list):
    """获取长度"""
    tool = get_length_list()
    return {"length": tool.length(items)}


@router.post("/is-empty")
async def is_empty(items: list):
    """检查是否为空"""
    tool = get_length_list()
    return {"is_empty": tool.is_empty(items)}


@router.post("/is-not-empty")
async def is_not_empty(items: list):
    """检查是否非空"""
    tool = get_length_list()
    return {"is_not_empty": tool.is_not_empty(items)}
