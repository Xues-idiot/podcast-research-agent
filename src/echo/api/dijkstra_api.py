"""Dijkstra API"""

from fastapi import APIRouter

from echo.research.dijkstra import get_dijkstra


router = APIRouter(prefix="/api/dijkstra", tags=["dijkstra"])


@router.post("/shortest-path")
async def shortest_path(graph: dict, start: str):
    """最短路径"""
    tool = get_dijkstra()
    return {"distances": tool.shortest_path(graph, start)}
