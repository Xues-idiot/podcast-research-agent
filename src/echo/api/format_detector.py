"""内容格式检测API"""

from fastapi import APIRouter

from echo.research.format_detector import get_format_detector


router = APIRouter(prefix="/api/format", tags=["format"])


@router.post("/detect")
async def detect_format(content: str):
    detector = get_format_detector()
    result = detector.detect(content)
    return {
        "format_type": result.format_type,
        "confidence": result.confidence,
        "language": result.language,
        "is_timestamped": result.is_timestamped,
        "has_speaker_labels": result.has_speaker_labels,
    }