"""按键分组工具API"""

from fastapi import APIRouter

from echo.research.group_by_tool import get_group_by_tool


router = APIRouter(prefix="/api/group-by", tags=["group-by"])


@router.post("/group")
async def group_items():
    tool = get_group_by_tool()
    return {"success": True}
