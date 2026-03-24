"""知识库API - 管理播客Entry"""

from typing import Optional

from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

from echo.knowledge import Entry, EntryStore, TextSplitter


router = APIRouter(prefix="/api/knowledge", tags=["knowledge"])


class EntryResponse(BaseModel):
    """Entry响应"""
    id: str
    podcast_id: str
    raw: str
    compiled: str
    start_time: float
    end_time: float
    duration: float
    metadata: dict


class SearchRequest(BaseModel):
    """搜索请求"""
    query: str
    podcast_id: str
    top_k: int = 5


class SearchResponse(BaseModel):
    """搜索响应"""
    results: list[EntryResponse]
    query: str


class CreateEntriesRequest(BaseModel):
    """创建Entry请求"""
    podcast_id: str
    transcript_segments: list[dict]  # [{"start": 0, "end": 10, "text": "..."}]


# 全局存储和分割器实例
_entry_store = EntryStore()
_text_splitter = TextSplitter(chunk_size=500, chunk_overlap=50)


@router.post("/entries", response_model=dict)
async def create_entries(request: CreateEntriesRequest):
    """从转录创建Entry

    Args:
        request: 包含 podcast_id 和 transcript_segments

    Returns:
        创建的Entry数量
    """
    entries = _text_splitter.split_transcript(
        podcast_id=request.podcast_id,
        transcript_segments=request.transcript_segments,
    )

    count = _entry_store.add_entries(request.podcast_id, entries)

    return {
        "podcast_id": request.podcast_id,
        "count": count,
        "message": f"成功创建 {count} 个Entry"
    }


@router.get("/entries/{podcast_id}", response_model=list[EntryResponse])
async def get_entries(podcast_id: str):
    """获取播客的所有Entry"""
    entries = _entry_store.get_entries(podcast_id)

    return [
        EntryResponse(
            id=e.id,
            podcast_id=e.podcast_id,
            raw=e.raw,
            compiled=e.compiled,
            start_time=e.start_time,
            end_time=e.end_time,
            duration=e.duration,
            metadata=e.metadata,
        )
        for e in entries
    ]


@router.get("/entries/{podcast_id}/time-range")
async def get_entries_by_time(
    podcast_id: str,
    start: float,
    end: float
) -> list[EntryResponse]:
    """获取指定时间范围内的Entry"""
    entries = _entry_store.get_entries_by_time_range(podcast_id, start, end)

    return [
        EntryResponse(
            id=e.id,
            podcast_id=e.podcast_id,
            raw=e.raw,
            compiled=e.compiled,
            start_time=e.start_time,
            end_time=e.end_time,
            duration=e.duration,
            metadata=e.metadata,
        )
        for e in entries
    ]


@router.delete("/entries/{podcast_id}", response_model=dict)
async def delete_entries(podcast_id: str):
    """删除播客的所有Entry"""
    count = _entry_store.delete_entries(podcast_id)

    return {
        "podcast_id": podcast_id,
        "count": count,
        "message": f"成功删除 {count} 个Entry"
    }


@router.post("/search", response_model=SearchResponse)
async def search_entries(request: SearchRequest):
    """搜索Entry

    TODO: 集成向量检索
    """
    entries = _entry_store.search(
        podcast_id=request.podcast_id,
        query=request.query,
        top_k=request.top_k,
    )

    return SearchResponse(
        query=request.query,
        results=[
            EntryResponse(
                id=e.id,
                podcast_id=e.podcast_id,
                raw=e.raw,
                compiled=e.compiled,
                start_time=e.start_time,
                end_time=e.end_time,
                duration=e.duration,
                metadata=e.metadata,
            )
            for e in entries
        ]
    )


@router.get("/podcasts")
async def list_podcasts():
    """列出所有已存储的播客"""
    podcast_ids = _entry_store.list_podcasts()
    return {
        "podcasts": podcast_ids,
        "count": len(podcast_ids)
    }


@router.get("/health")
async def health_check():
    """健康检查"""
    return {"status": "healthy", "module": "knowledge"}
