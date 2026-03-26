"""剪贴板导入API"""

from fastapi import APIRouter
from pydantic import BaseModel

from echo.research.clipboard import get_clipboard_importer


router = APIRouter(prefix="/api/clipboard", tags=["clipboard"])


class ParseTextRequest(BaseModel):
    """解析文本请求"""
    text: str


@router.post("/parse")
async def parse_clipboard(request: ParseTextRequest):
    """解析剪贴板文本中的URL

    Args:
        request: 包含文本的请求

    Returns:
        解析出的URL列表
    """
    importer = get_clipboard_importer()
    urls = importer.parse(request.text)

    return {
        "urls": [
            {
                "url": u.url,
                "platform": u.platform,
                "is_valid": u.is_valid,
            }
            for u in urls
        ],
        "count": len(urls),
    }


@router.get("/validate/{url}")
async def validate_url(url: str):
    """验证URL是否有效

    Args:
        url: URL

    Returns:
        验证结果
    """
    importer = get_clipboard_importer()
    is_valid = importer.is_valid_podcast_url(url)
    platform = importer.get_platform_from_url(url)

    return {
        "url": url,
        "is_valid": is_valid,
        "platform": platform,
    }


@router.get("/platform/{url}")
async def get_platform(url: str):
    """获取URL对应的平台

    Args:
        url: URL

    Returns:
        平台信息
    """
    importer = get_clipboard_importer()
    platform = importer.get_platform_from_url(url)

    return {
        "url": url,
        "platform": platform,
        "is_supported": platform != "unknown",
    }
