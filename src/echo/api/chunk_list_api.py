"""列表分块API"""

from fastapi import APIRouter

from echo.research.chunk_list_tool import get_chunk_list_tool


router = APIRouter(prefix="/api/chunk-list", tags=["chunk-list"])


@router.post("/chunk")
async def chunk(items: list, size: int):
    return {"result": get_chunk_list_tool().chunk_list(items, size)}