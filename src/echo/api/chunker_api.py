"""分块API"""

from fastapi import APIRouter

from echo.research.chunker_tool import get_chunker_tool


router = APIRouter(prefix="/api/chunker", tags=["chunker"])


@router.post("/chunk")
async def chunk(items: list, size: int):
    return {"result": get_chunker_tool().chunk(items, size)}