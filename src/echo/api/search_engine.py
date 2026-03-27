"""全文搜索API"""

from fastapi import APIRouter

from echo.research.search_engine import get_full_text_search


router = APIRouter(prefix="/api/search", tags=["search"])


@router.post("/text")
async def search_text(text: str, query: str, case_sensitive: bool = False):
    searcher = get_full_text_search()
    results = searcher.search(text, query, case_sensitive)
    return {
        "count": len(results),
        "results": [
            {
                "line": r.line,
                "line_number": r.line_number,
                "match_start": r.match_start,
                "match_end": r.match_end
            }
            for r in results
        ]
    }


@router.post("/regex")
async def search_regex(text: str, pattern: str):
    searcher = get_full_text_search()
    results = searcher.search_regex(text, pattern)
    return {
        "count": len(results),
        "results": [
            {
                "line": r.line,
                "line_number": r.line_number,
                "match_start": r.match_start,
                "match_end": r.match_end
            }
            for r in results
        ]
    }