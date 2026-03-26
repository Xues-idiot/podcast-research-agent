"""文本统计API"""

from fastapi import APIRouter

from echo.research.word_counter import get_text_stats_calculator


router = APIRouter(prefix="/api/text", tags=["text"])


@router.post("/stats")
async def get_stats(text: str):
    calc = get_text_stats_calculator()
    stats = calc.calculate(text)
    return {
        "char_count": stats.char_count,
        "word_count": stats.word_count,
        "chinese_char_count": stats.chinese_char_count,
        "english_word_count": stats.english_word_count,
        "line_count": stats.line_count,
        "paragraph_count": stats.paragraph_count,
        "avg_line_length": round(stats.avg_line_length, 2),
        "reading_time_seconds": stats.reading_time_seconds,
        "reading_time_minutes": round(stats.reading_time_seconds / 60, 1),
    }