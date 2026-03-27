"""图API"""

from fastapi import APIRouter

from echo.research.graph_tool import get_graph_tool


router = APIRouter(prefix="/api/graph", tags=["graph"])


@router.post("/bfs")
async def bfs(graph: dict, start: str):
    """广度优先搜索"""
    tool = get_graph_tool()
    return {"path": tool.bfs(graph, start)}


@router.post("/dfs")
async def dfs(graph: dict, start: str):
    """深度优先搜索"""
    tool = get_graph_tool()
    return {"path": tool.dfs(graph, start)}
