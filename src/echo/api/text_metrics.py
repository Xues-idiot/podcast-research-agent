"""文本指标API"""

from fastapi import APIRouter

from echo.research.text_metrics import get_text_metrics_calculator


router = APIRouter(prefix="/api/metrics", tags=["metrics"])


@router.post("/calculate")
async def calculate_metrics(text: str):
    calc = get_text_metrics_calculator()
    metrics = calc.calculate(text)
    return {
        "char_count": metrics.char_count,
        "word_count": metrics.word_count,
        "line_count": metrics.line_count,
        "paragraph_count": metrics.paragraph_count,
        "avg_word_length": metrics.avg_word_length,
        "avg_sentence_length": metrics.avg_sentence_length,
        "readability_score": metrics.readability_score,
    }