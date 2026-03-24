"""来源聚合API路由"""

from typing import Optional

from fastapi import APIRouter, HTTPException

from echo.sources import (
    SourceType,
    detect_source_type,
    get_registry,
    register_all_sources,
)

router = APIRouter(prefix="/api/sources", tags=["sources"])


@router.on_event("startup")
async def startup():
    """启动时注册所有来源"""
    register_all_sources()


@router.get("/detect")
async def detect_url_source(url: str) -> dict:
    """检测URL的来源类型

    Args:
        url: 待检测的URL

    Returns:
        来源类型信息
    """
    source_type = detect_source_type(url)
    registry = get_registry()
    source = registry.get(source_type)

    return {
        "url": url,
        "source_type": source_type.value,
        "source_name": source_type.name if hasattr(source_type, "name") else str(source_type),
        "is_supported": source is not None,
        "detected_at": source_type.value != "unknown",
    }


@router.get("/sources")
async def list_sources() -> dict:
    """列出所有已注册的来源

    Returns:
        来源列表
    """
    registry = get_registry()
    sources = registry.list_sources()

    return {
        "sources": [
            {
                "type": s.value,
                "name": s.name if hasattr(s, "name") else str(s),
            }
            for s in sources
        ],
        "total": len(sources),
    }


@router.get("/channel")
async def get_channel(url: str) -> dict:
    """获取播客频道信息

    Args:
        url: 频道URL

    Returns:
        频道信息
    """
    registry = get_registry()
    source_type, source = registry.detect_and_get(url)

    if source is None:
        raise HTTPException(
            status_code=400,
            detail=f"Unsupported source type: {source_type.value}"
        )

    try:
        channel = await source.get_channel(url)
        return {
            "source": channel.source.value,
            "source_id": channel.source_id,
            "title": channel.title,
            "description": channel.description,
            "feed_url": channel.feed_url,
            "thumbnail_url": channel.thumbnail_url,
            "episode_count": len(channel.episodes),
            "episodes": [
                {
                    "source_id": e.source_id,
                    "title": e.title,
                    "description": e.description[:200] + "..." if len(e.description) > 200 else e.description,
                    "duration": e.duration,
                    "published_at": e.published_at,
                    "thumbnail_url": e.thumbnail_url,
                }
                for e in channel.episodes[:20]  # 限制返回20个
            ],
            "metadata": channel.metadata,
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/episode")
async def get_episode(url: str) -> dict:
    """获取播客单集信息

    Args:
        url: 单集URL

    Returns:
        单集信息
    """
    registry = get_registry()
    source_type, source = registry.detect_and_get(url)

    if source is None:
        raise HTTPException(
            status_code=400,
            detail=f"Unsupported source type: {source_type.value}"
        )

    try:
        episode = await source.get_episode(url)
        return {
            "source": episode.source.value,
            "source_id": episode.source_id,
            "title": episode.title,
            "description": episode.description,
            "audio_url": episode.audio_url,
            "thumbnail_url": episode.thumbnail_url,
            "duration": episode.duration,
            "published_at": episode.published_at,
            "metadata": episode.metadata,
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/audio-url")
async def get_audio_url(url: str) -> dict:
    """获取音频直链

    Args:
        url: 单集URL

    Returns:
        音频URL信息
    """
    registry = get_registry()
    source_type, source = registry.detect_and_get(url)

    if source is None:
        raise HTTPException(
            status_code=400,
            detail=f"Unsupported source type: {source_type.value}"
        )

    try:
        episode = await source.get_episode(url)
        audio_url = await source.get_audio_url(episode)
        return {
            "audio_url": audio_url,
            "source": episode.source.value,
            "source_id": episode.source_id,
            "title": episode.title,
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
