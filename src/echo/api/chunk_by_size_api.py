"""按大小分块API"""

from fastapi import APIRouter

from echo.research.chunk_by_size_tool import get_chunk_by_size_tool


router = APIRouter(prefix="/api/chunk-by-size", tags=["chunk-by-size"])


@router.post("/chunk")
async def chunk_by_size(items: list, size: int):
    return {"result": get_chunk_by_size_tool().chunk_by_size(items, size)}