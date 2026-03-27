"""树状数组API"""

from fastapi import APIRouter

from echo.research.fenwick_tree import get_fenwick_tree


router = APIRouter(prefix="/api/fenwick", tags=["fenwick"])


@router.post("/create")
async def create(size: int):
    """创建树状数组"""
    tool = get_fenwick_tree()
    return {"tree": tool.create(size)}


@router.post("/prefix-sum")
async def prefix_sum(tree: list, index: int):
    """前缀和"""
    tool = get_fenwick_tree()
    return {"sum": tool.prefix_sum(tree, index)}
