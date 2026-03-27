"""打乱工具API"""

from fastapi import APIRouter

from echo.research.shuffle_tool import get_shuffle_tool


router = APIRouter(prefix="/api/shuffle", tags=["shuffle"])


@router.post("/shuffle")
async def shuffle_items():
    tool = get_shuffle_tool()
    return {"success": True}
