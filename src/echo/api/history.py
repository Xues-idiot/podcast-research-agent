"""研究历史API - 管理研究历史记录"""

from typing import Optional

from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

from echo.research.history import get_research_history


router = APIRouter(prefix="/api/history", tags=["history"])


class AddHistoryRequest(BaseModel):
    """添加历史请求"""
    url: str
    title: str = ""
    podcast_id: str = ""
    platform: str = ""
    duration: int = 0


class UpdateNotesRequest(BaseModel):
    """更新笔记请求"""
    notes: str


class AddTagRequest(BaseModel):
    """添加标签请求"""
    tag: str


@router.get("/")
async def list_history(
    platform: Optional[str] = None,
    tag: Optional[str] = None,
    favorite: bool = None,
    search: Optional[str] = None,
    limit: int = 50,
):
    """列出研究历史

    Args:
        platform: 按平台筛选
        tag: 按标签筛选
        favorite: 按收藏筛选
        search: 搜索关键词
        limit: 返回数量

    Returns:
        历史条目列表
    """
    history = get_research_history()
    entries = history.list(
        platform=platform,
        tag=tag,
        favorite=favorite,
        search=search,
        limit=limit,
    )
    return {
        "entries": [e.to_dict() for e in entries],
        "count": len(entries),
    }


@router.post("/")
async def add_history(request: AddHistoryRequest):
    """添加研究历史记录

    Args:
        request: 包含研究信息的请求

    Returns:
        创建的历史条目
    """
    history = get_research_history()
    entry = history.add(
        url=request.url,
        title=request.title,
        podcast_id=request.podcast_id,
        platform=request.platform,
        duration=request.duration,
    )
    return entry.to_dict()


@router.get("/stats")
async def get_history_stats():
    """获取研究历史统计"""
    history = get_research_history()
    return history.get_stats()


@router.get("/{entry_id}")
async def get_history_entry(entry_id: str):
    """获取特定历史条目"""
    history = get_research_history()
    entry = history.get(entry_id)
    if not entry:
        raise HTTPException(status_code=404, detail="History entry not found")
    return entry.to_dict()


@router.post("/{entry_id}/tag")
async def add_tag(entry_id: str, request: AddTagRequest):
    """添加标签"""
    history = get_research_history()
    if not history.add_tag(entry_id, request.tag):
        raise HTTPException(status_code=404, detail="History entry not found")
    return {"status": "added", "tag": request.tag}


@router.delete("/{entry_id}/tag/{tag}")
def remove_tag(entry_id: str, tag: str):
    """移除标签"""
    history = get_research_history()
    if not history.remove_tag(entry_id, tag):
        raise HTTPException(status_code=404, detail="History entry not found")
    return {"status": "removed", "tag": tag}


@router.post("/{entry_id}/favorite")
async def toggle_favorite(entry_id: str):
    """切换收藏状态"""
    history = get_research_history()
    if not history.toggle_favorite(entry_id):
        raise HTTPException(status_code=404, detail="History entry not found")
    entry = history.get(entry_id)
    return {"status": "toggled", "favorite": entry.favorite}


@router.put("/{entry_id}/notes")
def update_notes(entry_id: str, request: UpdateNotesRequest):
    """更新笔记"""
    history = get_research_history()
    if not history.update_notes(entry_id, request.notes):
        raise HTTPException(status_code=404, detail="History entry not found")
    return {"status": "updated", "notes": request.notes}


@router.delete("/{entry_id}")
def delete_history(entry_id: str):
    """删除历史条目"""
    history = get_research_history()
    if not history.delete(entry_id):
        raise HTTPException(status_code=404, detail="History entry not found")
    return {"status": "deleted", "entry_id": entry_id}


@router.delete("/")
def clear_history():
    """清空所有历史"""
    history = get_research_history()
    history.clear()
    return {"status": "cleared"}
