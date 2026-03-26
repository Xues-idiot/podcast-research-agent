"""书签API - 管理书签"""

from typing import Optional

from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

from echo.research.bookmarks import get_bookmark_manager


router = APIRouter(prefix="/api/bookmarks", tags=["bookmarks"])


class AddBookmarkRequest(BaseModel):
    """添加书签请求"""
    research_id: str
    timestamp: float
    content: str = ""
    entry_id: str = ""
    note: str = ""
    color: str = "#3498DB"


class UpdateBookmarkRequest(BaseModel):
    """更新书签请求"""
    note: Optional[str] = None
    color: Optional[str] = None


@router.get("/")
async def list_bookmarks(research_id: Optional[str] = None, limit: int = 100):
    """列出书签

    Args:
        research_id: 研究ID筛选
        limit: 数量限制

    Returns:
        书签列表
    """
    manager = get_bookmark_manager()

    if research_id:
        bookmarks = manager.list_by_research(research_id)
    else:
        bookmarks = manager.list_all(limit=limit)

    return {
        "bookmarks": [bm.to_dict() for bm in bookmarks],
        "count": len(bookmarks),
    }


@router.post("/")
async def add_bookmark(request: AddBookmarkRequest):
    """添加书签

    Args:
        request: 书签信息

    Returns:
        添加的书签
    """
    manager = get_bookmark_manager()
    bookmark = manager.add(
        research_id=request.research_id,
        timestamp=request.timestamp,
        content=request.content,
        entry_id=request.entry_id,
        note=request.note,
        color=request.color,
    )
    return bookmark.to_dict()


@router.get("/{bookmark_id}")
async def get_bookmark(bookmark_id: str):
    """获取书签详情

    Args:
        bookmark_id: 书签ID

    Returns:
        书签详情
    """
    manager = get_bookmark_manager()
    bookmark = manager.get(bookmark_id)
    if not bookmark:
        raise HTTPException(status_code=404, detail="Bookmark not found")
    return bookmark.to_dict()


@router.put("/{bookmark_id}")
async def update_bookmark(bookmark_id: str, request: UpdateBookmarkRequest):
    """更新书签

    Args:
        bookmark_id: 书签ID
        request: 更新内容

    Returns:
        更新后的书签
    """
    manager = get_bookmark_manager()

    if request.note is not None:
        if not manager.update_note(bookmark_id, request.note):
            raise HTTPException(status_code=404, detail="Bookmark not found")

    if request.color is not None:
        if not manager.update_color(bookmark_id, request.color):
            raise HTTPException(status_code=404, detail="Bookmark not found")

    return manager.get(bookmark_id).to_dict()


@router.delete("/{bookmark_id}")
def remove_bookmark(bookmark_id: str):
    """删除书签

    Args:
        bookmark_id: 书签ID

    Returns:
        操作结果
    """
    manager = get_bookmark_manager()
    if not manager.remove(bookmark_id):
        raise HTTPException(status_code=404, detail="Bookmark not found")
    return {"status": "removed", "bookmark_id": bookmark_id}


@router.get("/search/")
async def search_bookmarks(q: str):
    """搜索书签

    Args:
        q: 搜索词

    Returns:
        搜索结果
    """
    manager = get_bookmark_manager()
    results = manager.search(q)
    return {
        "bookmarks": [bm.to_dict() for bm in results],
        "count": len(results),
        "query": q,
    }


@router.get("/stats/")
async def get_stats():
    """获取书签统计

    Returns:
        书签统计
    """
    manager = get_bookmark_manager()
    return manager.get_stats()
