"""版本API - 管理研究历史版本"""

from typing import Optional

from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

from echo.research.versions import get_version_manager


router = APIRouter(prefix="/api/versions", tags=["versions"])


class SaveVersionRequest(BaseModel):
    """保存版本请求"""
    research_id: str
    data: dict
    diff_summary: str = ""
    created_by: str = "system"
    is_auto_save: bool = False


@router.post("/")
async def save_version(request: SaveVersionRequest):
    """保存版本

    Args:
        request: 版本信息

    Returns:
        保存的版本
    """
    manager = get_version_manager()
    version = manager.save(
        research_id=request.research_id,
        data=request.data,
        diff_summary=request.diff_summary,
        created_by=request.created_by,
        is_auto_save=request.is_auto_save,
    )
    return version.__dict__


@router.get("/research/{research_id}")
async def get_versions(
    research_id: str,
    limit: int = 20,
    include_auto_save: bool = False,
):
    """获取版本列表

    Args:
        research_id: 研究ID
        limit: 数量限制
        include_auto_save: 是否包含自动保存

    Returns:
        版本列表
    """
    manager = get_version_manager()
    versions = manager.get_versions(
        research_id=research_id,
        limit=limit,
        include_auto_save=include_auto_save,
    )
    return {
        "versions": [v.__dict__ for v in versions],
        "count": len(versions),
    }


@router.get("/{version_id}")
async def get_version(version_id: str):
    """获取版本详情

    Args:
        version_id: 版本ID

    Returns:
        版本详情
    """
    manager = get_version_manager()
    version = manager.get(version_id)
    if not version:
        raise HTTPException(status_code=404, detail="Version not found")
    return version.__dict__


@router.get("/{version_id}/data")
async def get_version_data(version_id: str):
    """获取版本的完整数据

    Args:
        version_id: 版本ID

    Returns:
        研究数据
    """
    manager = get_version_manager()
    version = manager.get(version_id)
    if not version:
        raise HTTPException(status_code=404, detail="Version not found")
    return version.data


@router.post("/{version_id}/rollback")
async def rollback(version_id: str):
    """回滚到指定版本

    Args:
        version_id: 版本ID

    Returns:
        回滚后的数据
    """
    manager = get_version_manager()
    data = manager.rollback(version_id)
    if data is None:
        raise HTTPException(status_code=404, detail="Version not found")
    return {"status": "rolled_back", "data": data}


@router.get("/{version_id1}/compare/{version_id2}")
async def compare_versions(version_id1: str, version_id2: str):
    """比较两个版本

    Args:
        version_id1: 版本1
        version_id2: 版本2

    Returns:
        差异信息
    """
    manager = get_version_manager()
    return manager.compare(version_id1, version_id2)


@router.delete("/research/{research_id}/before/{version_number}")
def delete_versions_before(
    research_id: str,
    version_number: int,
):
    """删除指定版本之前的所有版本

    Args:
        research_id: 研究ID
        version_number: 版本号

    Returns:
        删除数量
    """
    manager = get_version_manager()
    count = manager.delete_before(research_id, version_number)
    return {"deleted": count}


@router.get("/stats/")
async def get_stats():
    """获取版本统计

    Returns:
        版本统计
    """
    manager = get_version_manager()
    return manager.get_stats()
