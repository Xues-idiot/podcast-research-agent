"""分块API"""

from fastapi import APIRouter

from echo.research.chunk_tool import get_chunk_tool


router = APIRouter(prefix="/api/chunk", tags=["chunk"])


@router.post("/chunk")
async def chunk(items: list, size: int):
    return {"result": get_chunk_tool().chunk(items, size)}