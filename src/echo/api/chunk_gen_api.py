"""分块生成API"""

from fastapi import APIRouter

from echo.research.chunk_gen import get_chunk_gen


router = APIRouter(prefix="/api/chunk-gen", tags=["chunk-gen"])


@router.post("/by-size")
async def chunk_by_size(items: list, size: int):
    """按大小分块"""
    tool = get_chunk_gen()
    return {"chunks": tool.chunk_by_size(items, size)}
