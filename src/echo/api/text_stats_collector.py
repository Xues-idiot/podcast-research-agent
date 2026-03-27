"""统计收集API"""

from fastapi import APIRouter

from echo.research.text_stats_collector import get_stats_collector


router = APIRouter(prefix="/api/stats", tags=["stats"])


@router.post("/collect")
async def collect_stats(text: str):
    collector = get_stats_collector()
    stats = collector.collect(text)
    return {
        "total_chars": stats.total_chars,
        "total_words": stats.total_words,
        "total_lines": stats.total_lines,
        "avg_line_length": round(stats.avg_line_length, 2),
        "max_line_length": stats.max_line_length,
        "min_line_length": stats.min_line_length,
    }