"""线段树API"""

from fastapi import APIRouter

from echo.research.segment_tree import get_segment_tree


router = APIRouter(prefix="/api/segment-tree", tags=["segment-tree"])


@router.post("/build")
async def build(arr: list):
    """构建线段树"""
    tool = get_segment_tree()
    return {"tree": tool.build(arr)}
