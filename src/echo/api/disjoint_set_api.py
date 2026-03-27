"""并查集API"""

from fastapi import APIRouter

from echo.research.disjoint_set import get_disjoint_set


router = APIRouter(prefix="/api/disjoint-set", tags=["disjoint-set"])


@router.post("/create")
async def create(items: list):
    """创建并查集"""
    tool = get_disjoint_set()
    return {"parent": tool.create(items)}


@router.post("/find")
async def find(parent: dict, x: str):
    """查找根"""
    tool = get_disjoint_set()
    return {"root": tool.find(parent, x)}
