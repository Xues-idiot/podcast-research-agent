"""采样工具API"""

from fastapi import APIRouter

from echo.research.sample_tool import get_sample_tool


router = APIRouter(prefix="/api/sample", tags=["sample"])


@router.post("/sample")
async def sample_items():
    tool = get_sample_tool()
    return {"success": True}
