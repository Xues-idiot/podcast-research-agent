"""反转API"""

from fastapi import APIRouter

from echo.research.reverse_list import get_reverse_list


router = APIRouter(prefix="/api/reverse", tags=["reverse"])


@router.post("/list")
async def reverse_list(items: list):
    """反转列表"""
    tool = get_reverse_list()
    return {"items": tool.reverse(items)}
