"""搜索API - 全文搜索和高级筛选"""

from typing import Optional

from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

from echo.research.search import get_search_engine


router = APIRouter(prefix="/api/search", tags=["search"])


class SearchRequest(BaseModel):
    """搜索请求"""
    query: str
    platform: Optional[str] = None
    tag: Optional[str] = None
    date_from: Optional[str] = None
    date_to: Optional[str] = None
    limit: int = 20


class IndexRequest(BaseModel):
    """索引请求"""
    research_id: str
    title: str = ""
    source: str = ""
    platform: str = ""
    summary: str = ""
    keypoints: list[str] = []
    tags: list[str] = []


@router.get("/")
async def search(
    q: str,
    platform: Optional[str] = None,
    tag: Optional[str] = None,
    date_from: Optional[str] = None,
    date_to: Optional[str] = None,
    limit: int = 20,
):
    """搜索研究结果

    Args:
        q: 搜索词
        platform: 平台筛选
        tag: 标签筛选
        date_from: 开始日期
        date_to: 结束日期
        limit: 结果数量

    Returns:
        搜索结果列表
    """
    engine = get_search_engine()
    results = engine.search(
        query=q,
        platform=platform,
        tag=tag,
        date_from=date_from,
        date_to=date_to,
        limit=limit,
    )

    return {
        "results": [
            {
                "research_id": r.research_id,
                "title": r.title,
                "source": r.source,
                "platform": r.platform,
                "snippet": r.snippet,
                "score": r.score,
                "highlights": r.highlights,
            }
            for r in results
        ],
        "count": len(results),
        "query": q,
    }


@router.post("/index")
async def index_research(request: IndexRequest):
    """索引研究结果

    Args:
        request: 索引信息

    Returns:
        索引结果
    """
    engine = get_search_engine()
    engine.index(
        research_id=request.research_id,
        title=request.title,
        source=request.source,
        platform=request.platform,
        summary=request.summary,
        keypoints=request.keypoints,
        tags=request.tags,
    )
    return {"status": "indexed", "research_id": request.research_id}


@router.delete("/{research_id}")
def remove_index(research_id: str):
    """移除索引

    Args:
        research_id: 研究ID

    Returns:
        操作结果
    """
    engine = get_search_engine()
    engine.remove(research_id)
    return {"status": "removed", "research_id": research_id}


@router.get("/suggest/")
async def suggest(prefix: str, limit: int = 5):
    """获取搜索建议

    Args:
        prefix: 前缀
        limit: 数量限制

    Returns:
        建议列表
    """
    engine = get_search_engine()
    suggestions = engine.suggest(prefix=prefix, limit=limit)
    return {"suggestions": suggestions}


@router.get("/recent/")
async def get_recent(limit: int = 10):
    """获取最近的索引项

    Args:
        limit: 数量限制

    Returns:
        最近索引列表
    """
    engine = get_search_engine()
    items = engine.get_recent(limit=limit)
    return {
        "recent": [item.to_dict() for item in items],
        "count": len(items),
    }


@router.get("/filters/")
async def get_filters():
    """获取筛选选项

    Returns:
        平台和标签列表
    """
    engine = get_search_engine()
    return {
        "platforms": engine.get_platforms(),
        "tags": engine.get_tags(),
    }


@router.get("/stats/")
async def get_stats():
    """获取索引统计

    Returns:
        索引统计
    """
    engine = get_search_engine()
    return engine.get_stats()


@router.post("/rebuild")
async def rebuild_index(researches: list[dict]):
    """重建索引

    Args:
        researches: 研究结果列表

    Returns:
        重建结果
    """
    engine = get_search_engine()
    engine.rebuild_index(researches)
    return {"status": "rebuilt", "count": len(researches)}
