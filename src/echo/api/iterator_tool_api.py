"""迭代器工具API"""

from fastapi import APIRouter
from pydantic import BaseModel

from echo.research.iterator_tool import get_iterator_tool


router = APIRouter(prefix="/api/iterator-tool", tags=["iterator-tool"])


class ChunkRequest(BaseModel):
    items: list
    size: int


@router.post("/chunk")
async def chunk(request: ChunkRequest):
    return {"result": list(get_iterator_tool().chunk_iter(request.items, request.size))}
