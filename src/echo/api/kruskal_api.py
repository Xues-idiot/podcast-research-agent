"""Kruskal API"""

from fastapi import APIRouter

from echo.research.kruskal import get_kruskal


router = APIRouter(prefix="/api/kruskal", tags=["kruskal"])


@router.post("/mst")
async def mst(vertices: list, edges: list):
    """最小生成树"""
    tool = get_kruskal()
    return {"mst": tool.mst(vertices, edges)}
