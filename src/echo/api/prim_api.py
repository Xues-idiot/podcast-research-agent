"""Prim API"""

from fastapi import APIRouter

from echo.research.prim import get_prim


router = APIRouter(prefix="/api/prim", tags=["prim"])


@router.post("/mst")
async def mst(graph: dict, start: str):
    """最小生成树"""
    tool = get_prim()
    return {"mst": tool.mst(graph, start)}
