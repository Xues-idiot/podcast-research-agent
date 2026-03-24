"""导航API - 时间戳导航相关路由"""

from dataclasses import dataclass
from typing import Optional

from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

from echo.navigation import TimestampNavigator, TimestampEntry, JumpResult


router = APIRouter(prefix="/api/navigation", tags=["navigation"])


@dataclass
class TimestampResponse:
    """时间戳响应"""
    timestamp: float
    formatted: str
    content: str
    entry_id: str
    type: str
    relevance: float


@dataclass
class JumpResponse:
    """跳转响应"""
    target_timestamp: float
    formatted_time: str
    context_before: str
    context_after: str
    jump_type: str
    nearby: list[TimestampResponse]


@dataclass
class MomentsResponse:
    """关键时刻响应"""
    total_duration: float
    moments: list[TimestampResponse]


# 存储活跃的导航器实例 (生产环境应使用Redis)
_navigators: dict[str, TimestampNavigator] = {}


class RegisterRequest(BaseModel):
    """注册播客请求"""
    podcast_id: str
    entries: list


class JumpRequest(BaseModel):
    """跳转请求"""
    podcast_id: str
    timestamp: float
    window_seconds: float = 30.0


class KeyMomentsRequest(BaseModel):
    """关键时刻请求"""
    podcast_id: str
    num_moments: int = 10


class QAHighlightsRequest(BaseModel):
    """问答高亮请求"""
    podcast_id: str
    qa_pairs: list


@router.post("/register")
async def register_entries(request: RegisterRequest):
    """注册播客的时间戳导航数据

    Args:
        request: 包含 podcast_id 和 entries 的请求

    Returns:
        注册成功的播客ID
    """
    try:
        navigator = TimestampNavigator(request.entries)
        _navigators[request.podcast_id] = navigator
        return {
            "status": "registered",
            "podcast_id": request.podcast_id,
            "entries_count": len(request.entries),
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.post("/jump", response_model=JumpResponse)
async def jump_to_timestamp(request: JumpRequest):
    """跳转到指定时间戳

    Args:
        request: 包含 podcast_id, timestamp 的请求

    Returns:
        JumpResponse: 跳转结果
    """
    navigator = _navigators.get(request.podcast_id)
    if not navigator:
        raise HTTPException(status_code=404, detail="Podcast not found. Please register first.")

    result = navigator.jump_to(request.timestamp, request.window_seconds)

    return JumpResponse(
        target_timestamp=result.target_timestamp,
        formatted_time=navigator.format_timestamp(result.target_timestamp),
        context_before=result.context_before,
        context_after=result.context_after,
        jump_type=result.jump_type,
        nearby=[
            TimestampResponse(
                timestamp=e.timestamp,
                formatted=navigator.format_timestamp(e.timestamp),
                content=e.content,
                entry_id=e.entry_id,
                type=e.type,
                relevance=e.relevance,
            )
            for e in result.nearby_entries
        ],
    )


@router.get("/moments/{podcast_id}", response_model=MomentsResponse)
async def get_key_moments(podcast_id: str, num_moments: int = 10):
    """获取播客的关键时刻列表

    Args:
        podcast_id: 播客ID
        num_moments: 关键时刻数量

    Returns:
        MomentsResponse: 关键时刻列表
    """
    navigator = _navigators.get(podcast_id)
    if not navigator:
        raise HTTPException(status_code=404, detail="Podcast not found")

    moments = navigator.get_key_moments(num_moments)

    total_duration = 0.0
    if navigator.entries:
        total_duration = navigator.entries[-1].end_time

    return MomentsResponse(
        total_duration=total_duration,
        moments=[
            TimestampResponse(
                timestamp=m.timestamp,
                formatted=navigator.format_timestamp(m.timestamp),
                content=m.content,
                entry_id=m.entry_id,
                type=m.type,
                relevance=m.relevance,
            )
            for m in moments
        ],
    )


@router.post("/moments/from-keypoints")
async def get_moments_from_keypoints(request: KeyMomentsRequest):
    """根据关键点生成时间戳时刻

    Args:
        request: 包含 podcast_id 和 keypoints 的请求

    Returns:
        关键点对应的时间戳列表
    """
    navigator = _navigators.get(request.podcast_id)
    if not navigator:
        raise HTTPException(status_code=404, detail="Podcast not found")

    # keypoints 应该在请求体中
    keypoints = request.qa_pairs if hasattr(request, 'qa_pairs') else []

    # 实际上应该用 keypoints，但为了简化复用 KeyMomentsRequest
    # 这里用 extra 方式获取
    keypoints = getattr(request, 'keypoints', [])

    moments = navigator.get_moments_by_keypoints(keypoints)

    return {
        "podcast_id": request.podcast_id,
        "moments": [
            {
                "timestamp": m.timestamp,
                "formatted": navigator.format_timestamp(m.timestamp),
                "content": m.content,
                "type": m.type,
                "relevance": m.relevance,
            }
            for m in moments
        ],
    }


@router.post("/moments/from-qa")
async def get_moments_from_qa(request: QAHighlightsRequest):
    """根据问答对生成时间戳高亮

    Args:
        request: 包含 podcast_id 和 qa_pairs 的请求

    Returns:
        问答对应的时间戳列表
    """
    navigator = _navigators.get(request.podcast_id)
    if not navigator:
        raise HTTPException(status_code=404, detail="Podcast not found")

    moments = navigator.get_moments_by_qa(request.qa_pairs)

    return {
        "podcast_id": request.podcast_id,
        "highlights": [
            {
                "timestamp": m.timestamp,
                "formatted": navigator.format_timestamp(m.timestamp),
                "question": m.content.split("\n")[0] if "\n" in m.content else m.content,
                "answer_preview": m.content.split("\n")[-1] if "\n" in m.content else "",
                "type": m.type,
            }
            for m in moments
        ],
    }


@router.get("/parse/{timestamp_str}")
async def parse_timestamp(timestamp_str: str):
    """解析时间戳字符串

    Args:
        timestamp_str: 时间戳字符串 (MM:SS 或 HH:MM:SS)

    Returns:
        解析后的秒数
    """
    # 创建一个临时导航器来格式化
    navigator = TimestampNavigator([])
    seconds = navigator.parse_timestamp(timestamp_str)
    formatted = navigator.format_timestamp(seconds)

    return {
        "input": timestamp_str,
        "seconds": seconds,
        "formatted": formatted,
    }


@router.delete("/{podcast_id}")
async def unregister_podcast(podcast_id: str):
    """注销播客的导航数据

    Args:
        podcast_id: 播客ID
    """
    if podcast_id in _navigators:
        del _navigators[podcast_id]
        return {"status": "unregistered", "podcast_id": podcast_id}
    raise HTTPException(status_code=404, detail="Podcast not found")
