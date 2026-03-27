"""Floyd-Warshall API"""

from fastapi import APIRouter

from echo.research.floyd_warshall import get_floyd_warshall


router = APIRouter(prefix="/api/floyd-warshall", tags=["floyd-warshall"])


@router.post("/all-pairs")
async def all_pairs(vertices: list, edges: list):
    """全源最短路径"""
    tool = get_floyd_warshall()
    return {"distances": tool.all_pairs_shortest(vertices, edges)}
