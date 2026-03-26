"""情感分析API"""

from fastapi import APIRouter

from echo.research.sentiment import get_sentiment_analyzer


router = APIRouter(prefix="/api/sentiment", tags=["sentiment"])


@router.post("/analyze")
async def analyze_sentiment(text: str):
    analyzer = get_sentiment_analyzer()
    result = analyzer.analyze(text)
    return {
        "label": result.label,
        "score": round(result.score, 3),
        "positive_score": result.positive_score,
        "negative_score": result.negative_score,
        "neutral_score": result.neutral_score,
    }