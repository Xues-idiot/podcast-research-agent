"""跳表API"""

from fastapi import APIRouter

from echo.research.skip_list import get_skip_list_tool


router = APIRouter(prefix="/api/skip-list", tags=["skip-list"])


@router.post("/random-level")
async def random_level(max_level: int = 16):
    """生成随机层级"""
    tool = get_skip_list_tool()
    return {"level": tool.random_level(max_level)}
