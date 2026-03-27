"""拓扑排序API"""

from fastapi import APIRouter

from echo.research.topo_sort import get_topo_sort


router = APIRouter(prefix="/api/topo-sort", tags=["topo-sort"])


@router.post("/sort")
async def sort(graph: dict):
    """拓扑排序"""
    tool = get_topo_sort()
    return {"order": tool.sort(graph)}
