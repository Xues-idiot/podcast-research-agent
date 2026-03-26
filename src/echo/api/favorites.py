"""收藏API - 管理研究结果收藏夹"""

from typing import Optional

from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

from echo.research.favorites import get_favorites_manager


router = APIRouter(prefix="/api/favorites", tags=["favorites"])


class AddFavoriteRequest(BaseModel):
    """添加收藏请求"""
    research_id: str
    title: str = ""
    source: str = ""
    platform: str = ""
    tags: list[str] = []


class UpdateFavoriteRequest(BaseModel):
    """更新收藏请求"""
    notes: Optional[str] = None
    tags: Optional[list[str]] = None


class CreateCollectionRequest(BaseModel):
    """创建收藏集合请求"""
    name: str
    description: str = ""


@router.get("/")
async def list_favorites(tag: Optional[str] = None, platform: Optional[str] = None):
    """列出收藏

    Args:
        tag: 按标签筛选
        platform: 按平台筛选

    Returns:
        收藏列表
    """
    manager = get_favorites_manager()

    if tag:
        items = manager.list_by_tag(tag)
    elif platform:
        items = manager.list_by_platform(platform)
    else:
        items = manager.list_all()

    return {
        "favorites": [item.__dict__ for item in items],
        "count": len(items),
    }


@router.post("/")
async def add_favorite(request: AddFavoriteRequest):
    """添加收藏

    Args:
        request: 收藏信息

    Returns:
        收藏项
    """
    manager = get_favorites_manager()

    # 检查是否已收藏
    existing = manager.get_by_research_id(request.research_id)
    if existing:
        return existing.__dict__

    item = manager.add(
        research_id=request.research_id,
        title=request.title,
        source=request.source,
        platform=request.platform,
        tags=request.tags,
    )
    return item.__dict__


@router.get("/{favorite_id}")
async def get_favorite(favorite_id: str):
    """获取收藏详情

    Args:
        favorite_id: 收藏ID

    Returns:
        收藏详情
    """
    manager = get_favorites_manager()
    item = manager.get(favorite_id)
    if not item:
        raise HTTPException(status_code=404, detail="Favorite not found")
    return item.__dict__


@router.put("/{favorite_id}")
async def update_favorite(favorite_id: str, request: UpdateFavoriteRequest):
    """更新收藏

    Args:
        favorite_id: 收藏ID
        request: 更新内容

    Returns:
        更新后的收藏
    """
    manager = get_favorites_manager()

    if request.notes is not None:
        if not manager.update_notes(favorite_id, request.notes):
            raise HTTPException(status_code=404, detail="Favorite not found")

    if request.tags is not None:
        if not manager.update_tags(favorite_id, request.tags):
            raise HTTPException(status_code=404, detail="Favorite not found")

    return manager.get(favorite_id).__dict__


@router.delete("/{favorite_id}")
def remove_favorite(favorite_id: str):
    """移除收藏

    Args:
        favorite_id: 收藏ID

    Returns:
        操作结果
    """
    manager = get_favorites_manager()
    if not manager.remove(favorite_id):
        raise HTTPException(status_code=404, detail="Favorite not found")
    return {"status": "removed", "favorite_id": favorite_id}


@router.post("/{favorite_id}/tags/{tag}")
async def add_tag(favorite_id: str, tag: str):
    """添加标签

    Args:
        favorite_id: 收藏ID
        tag: 标签

    Returns:
        操作结果
    """
    manager = get_favorites_manager()
    if not manager.add_tag(favorite_id, tag):
        raise HTTPException(status_code=404, detail="Favorite not found")
    return {"status": "added", "tag": tag}


@router.delete("/{favorite_id}/tags/{tag}")
def remove_tag(favorite_id: str, tag: str):
    """移除标签

    Args:
        favorite_id: 收藏ID
        tag: 标签

    Returns:
        操作结果
    """
    manager = get_favorites_manager()
    if not manager.remove_tag(favorite_id, tag):
        raise HTTPException(status_code=404, detail="Favorite not found")
    return {"status": "removed", "tag": tag}


@router.get("/tags/all")
async def get_all_tags():
    """获取所有标签

    Returns:
        标签列表
    """
    manager = get_favorites_manager()
    return {"tags": manager.get_all_tags()}


# 收藏集合
@router.get("/collections/")
async def list_collections():
    """列出收藏集合

    Returns:
        收藏集合列表
    """
    manager = get_favorites_manager()
    collections = manager.list_collections()
    return {
        "collections": [
            {
                **coll.__dict__,
                "item_count": len(coll.items),
            }
            for coll in collections
        ],
        "count": len(collections),
    }


@router.post("/collections/")
async def create_collection(request: CreateCollectionRequest):
    """创建收藏集合

    Args:
        request: 集合信息

    Returns:
        创建的集合
    """
    manager = get_favorites_manager()
    coll = manager.create_collection(
        name=request.name,
        description=request.description,
    )
    return coll.__dict__


@router.get("/collections/{collection_id}")
async def get_collection(collection_id: str):
    """获取收藏集合详情

    Args:
        collection_id: 集合ID

    Returns:
        集合详情
    """
    manager = get_favorites_manager()
    coll = manager.get_collection(collection_id)
    if not coll:
        raise HTTPException(status_code=404, detail="Collection not found")

    items = manager.get_collection_items(collection_id)
    return {
        **coll.__dict__,
        "items": [item.__dict__ for item in items],
        "item_count": len(items),
    }


@router.delete("/collections/{collection_id}")
def delete_collection(collection_id: str):
    """删除收藏集合

    Args:
        collection_id: 集合ID

    Returns:
        操作结果
    """
    manager = get_favorites_manager()
    if not manager.delete_collection(collection_id):
        raise HTTPException(status_code=404, detail="Collection not found")
    return {"status": "deleted", "collection_id": collection_id}


@router.post("/collections/{collection_id}/items/{favorite_id}")
async def add_to_collection(collection_id: str, favorite_id: str):
    """添加收藏到集合

    Args:
        collection_id: 集合ID
        favorite_id: 收藏ID

    Returns:
        操作结果
    """
    manager = get_favorites_manager()
    if not manager.add_to_collection(collection_id, favorite_id):
        raise HTTPException(status_code=404, detail="Collection or favorite not found")
    return {"status": "added"}


@router.delete("/collections/{collection_id}/items/{favorite_id}")
def remove_from_collection(collection_id: str, favorite_id: str):
    """从集合移除收藏

    Args:
        collection_id: 集合ID
        favorite_id: 收藏ID

    Returns:
        操作结果
    """
    manager = get_favorites_manager()
    if not manager.remove_from_collection(collection_id, favorite_id):
        raise HTTPException(status_code=404, detail="Collection or favorite not found")
    return {"status": "removed"}
