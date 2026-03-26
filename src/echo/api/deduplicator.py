"""内容去重API"""

from fastapi import APIRouter

from echo.research.deduplicator import get_deduplicator


router = APIRouter(prefix="/api/dedup", tags=["dedup"])


@router.post("/lines")
async def deduplicate_lines(lines: list[str], threshold: float = 0.85):
    dedup = get_deduplicator()
    result = dedup.deduplicate_lines(lines, threshold)
    return {
        "original_count": len(lines),
        "deduplicated_count": len(result),
        "removed_count": len(lines) - len(result),
        "lines": result
    }


@router.post("/chunks")
async def deduplicate_chunks(chunks: list[str], threshold: float = 0.8):
    dedup = get_deduplicator()
    result = dedup.deduplicate_chunks(chunks, threshold)
    return {
        "original_count": len(chunks),
        "deduplicated_count": len(result),
        "removed_count": len(chunks) - len(result),
        "chunks": result
    }