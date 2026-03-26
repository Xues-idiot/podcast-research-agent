"""分享API - 管理研究结果分享链接"""

from typing import Optional

from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

from echo.research.share import (
    get_share_manager,
)


router = APIRouter(prefix="/api/share", tags=["share"])


class CreateShareRequest(BaseModel):
    """创建分享请求"""
    research_id: str
    password: str = ""
    expires_in_hours: int = 168  # 默认7天
    max_views: int = 0


class AccessShareRequest(BaseModel):
    """访问分享内容请求"""
    password: str = ""


@router.get("/{share_id}")
async def get_share_info(share_id: str):
    """获取分享链接信息（不包含研究内容）

    Args:
        share_id: 分享ID

    Returns:
        分享链接信息
    """
    manager = get_share_manager()
    share = manager.get(share_id)
    if not share:
        raise HTTPException(status_code=404, detail="Share not found")

    if not share.can_access():
        raise HTTPException(status_code=410, detail="Share link expired or max views reached")

    return share.to_dict()


@router.post("/{share_id}/access")
async def access_share(share_id: str, request: AccessShareRequest):
    """验证并访问分享内容

    Args:
        share_id: 分享ID
        request: 访问请求

    Returns:
        研究结果ID（实际内容需单独获取）
    """
    manager = get_share_manager()
    share = manager.get(share_id)
    if not share:
        raise HTTPException(status_code=404, detail="Share not found")

    if not share.can_access():
        raise HTTPException(status_code=410, detail="Share link expired or max views reached")

    # 验证密码
    if not manager.verify_password(share, request.password):
        raise HTTPException(status_code=401, detail="Invalid password")

    # 记录访问
    manager.record_view(share_id)

    return {
        "research_id": share.research_id,
        "access_granted": True,
    }


@router.post("/")
async def create_share(request: CreateShareRequest):
    """创建分享链接

    Args:
        request: 创建参数

    Returns:
        分享链接信息
    """
    manager = get_share_manager()

    # 检查是否已存在分享链接
    existing = manager.get_by_research_id(request.research_id)
    if existing:
        return existing.to_dict()

    share = manager.create(
        research_id=request.research_id,
        password=request.password,
        expires_in_hours=request.expires_in_hours,
        max_views=request.max_views,
    )
    return share.to_dict()


@router.delete("/{share_id}")
def revoke_share(share_id: str):
    """撤销分享链接

    Args:
        share_id: 分享ID

    Returns:
        操作结果
    """
    manager = get_share_manager()
    if not manager.revoke(share_id):
        raise HTTPException(status_code=404, detail="Share not found")
    return {"status": "revoked", "share_id": share_id}


@router.get("/research/{research_id}")
async def get_research_shares(research_id: str):
    """获取研究结果的所有分享链接

    Args:
        research_id: 研究结果ID

    Returns:
        分享链接列表
    """
    manager = get_share_manager()
    shares = manager.list_by_research(research_id)
    return {
        "shares": [s.to_dict() for s in shares],
        "count": len(shares),
    }


@router.post("/cleanup")
async def cleanup_expired():
    """清理过期链接

    Returns:
        清理结果
    """
    manager = get_share_manager()
    count = manager.cleanup_expired()
    return {"cleaned": count}
