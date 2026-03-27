"""堆API"""

from fastapi import APIRouter

from echo.research.heap_tool import get_heap_tool


router = APIRouter(prefix="/api/heap", tags=["heap"])


@router.post("/heapify")
async def heapify(items: list):
    """堆化"""
    tool = get_heap_tool()
    return {"heap": tool.heapify(items)}
