"""文本合并API"""

from fastapi import APIRouter

from echo.research.merger import get_text_merger


router = APIRouter(prefix="/api/merge", tags=["merge"])


@router.post("/consecutive")
async def merge_consecutive(texts: list[str], separator: str = " "):
    merger = get_text_merger()
    result = merger.merge_consecutive(texts, separator)
    return {"result": result}


@router.post("/with_overlap")
async def merge_with_overlap(texts: list[str], overlap_chars: int = 100):
    merger = get_text_merger()
    result = merger.merge_with_overlap(texts, overlap_chars)
    return {"result": result}


@router.post("/by_theme")
async def merge_by_theme(texts: list[str], similarity_threshold: float = 0.5):
    merger = get_text_merger()
    result = merger.merge_by_theme(texts, similarity_threshold)
    return {"merged_count": len(result), "texts": result}