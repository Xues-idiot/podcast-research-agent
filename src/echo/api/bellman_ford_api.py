"""Bellman-Ford API"""

from fastapi import APIRouter

from echo.research.bellman_ford import get_bellman_ford


router = APIRouter(prefix="/api/bellman-ford", tags=["bellman-ford"])


@router.post("/shortest-path")
async def shortest_path(vertices: list, edges: list, start: str):
    """最短路径"""
    tool = get_bellman_ford()
    return {"distances": tool.shortest_path(vertices, edges, start)}
