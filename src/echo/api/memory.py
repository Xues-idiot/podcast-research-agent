"""记忆API - 用户记忆管理路由"""

from typing import Optional
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

from echo.memory import MemoryStore, MemoryUpdater


router = APIRouter(prefix="/api/memory", tags=["memory"])


# 存储实例
_memory_store = MemoryStore()
_memory_updater = MemoryUpdater(_memory_store)


class UpdateRequest(BaseModel):
    """更新记忆请求"""
    user_id: str = "default"
    work_context: Optional[str] = None
    personal_context: Optional[str] = None
    top_of_mind: Optional[str] = None


class AddFactRequest(BaseModel):
    """添加事实请求"""
    user_id: str = "default"
    content: str
    category: str = "context"  # preference, knowledge, context, behavior, goal
    confidence: float = 0.5
    source: str = ""


class LearnPreferenceRequest(BaseModel):
    """学习偏好请求"""
    user_id: str = "default"
    preference_type: str  # podcast, export, topic
    data: dict


@router.get("/{user_id}")
async def get_memory(user_id: str = "default"):
    """获取用户记忆

    Args:
        user_id: 用户ID

    Returns:
        用户记忆
    """
    memory = _memory_store.get_memory(user_id)
    return memory.to_dict()


@router.post("/update")
async def update_memory(request: UpdateRequest):
    """更新用户记忆

    Args:
        request: 更新请求

    Returns:
        更新后的记忆
    """
    kwargs = {}
    if request.work_context is not None:
        kwargs["work_context"] = request.work_context
    if request.personal_context is not None:
        kwargs["personal_context"] = request.personal_context
    if request.top_of_mind is not None:
        kwargs["top_of_mind"] = request.top_of_mind

    memory = _memory_store.update_memory(request.user_id, **kwargs)
    return memory.to_dict()


@router.post("/facts")
async def add_fact(request: AddFactRequest):
    """添加记忆事实

    Args:
        request: 添加事实请求

    Returns:
        添加的事实
    """
    fact = _memory_store.add_fact(
        user_id=request.user_id,
        content=request.content,
        category=request.category,
        confidence=request.confidence,
        source=request.source
    )
    return fact.to_dict()


@router.get("/{user_id}/facts")
async def get_facts(
    user_id: str = "default",
    category: Optional[str] = None,
    min_confidence: float = 0.0
):
    """获取记忆事实

    Args:
        user_id: 用户ID
        category: 过滤分类
        min_confidence: 最低置信度

    Returns:
        事实列表
    """
    facts = _memory_store.get_facts(
        user_id=user_id,
        category=category,
        min_confidence=min_confidence
    )
    return {
        "facts": [f.to_dict() for f in facts],
        "count": len(facts)
    }


@router.post("/learn")
async def learn_preference(request: LearnPreferenceRequest):
    """学习用户偏好

    Args:
        request: 学习偏好请求

    Returns:
        操作结果
    """
    if request.preference_type == "podcast":
        _memory_updater.learn_podcast_preference(request.user_id, request.data)
    elif request.preference_type == "export":
        format_type = request.data.get("format", "")
        if format_type:
            _memory_updater.learn_export_preference(request.user_id, format_type)
    elif request.preference_type == "topic":
        topic = request.data.get("topic", "")
        if topic:
            _memory_updater.learn_research_topic(request.user_id, topic)
    else:
        raise HTTPException(status_code=400, detail=f"Unknown preference type: {request.preference_type}")

    return {"status": "learned"}


@router.get("/{user_id}/context")
async def get_context(user_id: str = "default"):
    """获取个性化上下文

    Args:
        user_id: 用户ID

    Returns:
        格式化的上下文文本
    """
    context = _memory_updater.get_personalized_context(user_id)
    return {"context": context}


@router.delete("/{user_id}")
async def clear_memory(user_id: str = "default"):
    """清除用户记忆

    Args:
        user_id: 用户ID
    """
    _memory_store.clear_memory(user_id)
    return {"status": "cleared"}


@router.delete("/{user_id}/all")
async def delete_memory(user_id: str = "default"):
    """删除用户记忆

    Args:
        user_id: 用户ID
    """
    _memory_store.delete_memory(user_id)
    return {"status": "deleted"}
