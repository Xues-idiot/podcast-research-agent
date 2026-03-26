"""URL解析器API"""

from fastapi import APIRouter

from echo.research.url_parser import get_url_parser


router = APIRouter(prefix="/api/url", tags=["url"])


@router.get("/parse")
async def parse_url(url: str):
    parser = get_url_parser()
    result = parser.parse(url)
    return {
        "url": result.url,
        "platform": result.platform,
        "is_valid": result.is_valid,
        "video_id": result.video_id,
    }