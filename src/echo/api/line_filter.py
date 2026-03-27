"""行过滤API"""

from fastapi import APIRouter

from echo.research.line_filter import get_line_filter


router = APIRouter(prefix="/api/filter", tags=["filter"])


@router.post("/lines")
async def filter_lines(
    lines: list[str],
    filter_empty: bool = True,
    min_length: int = 1,
    max_length: int = 10000
):
    f = get_line_filter()
    result = lines
    if filter_empty:
        result = f.filter_empty_lines(result)
    result = f.filter_by_length(result, min_length, max_length)
    return {"lines": result, "count": len(result)}


@router.post("/deduplicate")
async def deduplicate_lines(lines: list[str], preserve_order: bool = True):
    f = get_line_filter()
    result = f.filter_duplicates(lines, preserve_order)
    return {"lines": result, "original_count": len(lines), "deduplicated_count": len(result)}