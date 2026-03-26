"""语言检测API"""

from fastapi import APIRouter

from echo.research.language_detector import get_language_detector


router = APIRouter(prefix="/api/language", tags=["language"])


@router.post("/detect")
async def detect_language(text: str):
    detector = get_language_detector()
    result = detector.detect(text)
    return {
        "language": result.language,
        "confidence": round(result.confidence, 3),
        "script": result.script,
    }