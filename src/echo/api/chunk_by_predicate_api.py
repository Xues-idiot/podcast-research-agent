"""谓词分块工具API"""

from fastapi import APIRouter

from echo.research.chunk_by_predicate import get_chunk_by_predicate


router = APIRouter(prefix="/api/chunk-predicate", tags=["chunk-predicate"])


@router.post("/chunk-by")
async def chunk_by_predicate():
    tool = get_chunk_by_predicate()
    return {"success": True}
