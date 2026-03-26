"""速率限制API - 管理API速率限制"""

from typing import Optional

from fastapi import APIRouter, HTTPException, Request
from pydantic import BaseModel

from echo.research.rate_limit import get_rate_limiter, RateLimitRule, RateLimitScope


router = APIRouter(prefix="/api/rate-limit", tags=["rate-limit"])


class UpdateRuleRequest(BaseModel):
    """更新规则请求"""
    max_requests: Optional[int] = None
    window_seconds: Optional[int] = None
    burst: Optional[int] = None


@router.get("/status")
async def get_status(rule_name: str = "global", user_id: Optional[str] = None):
    """获取速率限制状态

    Args:
        rule_name: 规则名称
        user_id: 用户ID

    Returns:
        限制状态
    """
    limiter = get_rate_limiter()
    status = limiter.get_status(
        key=user_id or "anonymous",
        rule_name=rule_name,
        user_id=user_id,
    )
    return {
        "rule": rule_name,
        "allowed": status.allowed,
        "remaining": status.remaining,
        "reset_at": status.reset_at,
    }


@router.post("/enabled")
async def set_enabled(enabled: bool):
    """设置是否启用限制

    Args:
        enabled: 是否启用

    Returns:
        操作结果
    """
    limiter = get_rate_limiter()
    limiter.set_enabled(enabled)
    return {"enabled": enabled}


@router.get("/rules")
async def list_rules():
    """列出所有规则

    Returns:
        规则列表
    """
    limiter = get_rate_limiter()
    return {
        "rules": {
            name: {
                "scope": rule.scope.value,
                "max_requests": rule.max_requests,
                "window_seconds": rule.window_seconds,
                "burst": rule.burst,
            }
            for name, rule in limiter._rules.items()
        }
    }


@router.put("/rules/{rule_name}")
def update_rule(rule_name: str, request: UpdateRuleRequest):
    """更新规则

    Args:
        rule_name: 规则名称
        request: 更新内容

    Returns:
        更新后的规则
    """
    limiter = get_rate_limiter()

    if rule_name not in limiter._rules:
        raise HTTPException(status_code=404, detail=f"Rule not found: {rule_name}")

    rule = limiter._rules[rule_name]

    if request.max_requests is not None:
        rule.max_requests = request.max_requests
    if request.window_seconds is not None:
        rule.window_seconds = request.window_seconds
    if request.burst is not None:
        rule.burst = request.burst

    limiter._rules[rule_name] = rule

    return {
        "rule": rule_name,
        "scope": rule.scope.value,
        "max_requests": rule.max_requests,
        "window_seconds": rule.window_seconds,
        "burst": rule.burst,
    }


@router.post("/reset")
async def reset_limit(key: Optional[str] = None, rule_name: Optional[str] = None):
    """重置限制

    Args:
        key: 标识键
        rule_name: 规则名称

    Returns:
        操作结果
    """
    limiter = get_rate_limiter()
    limiter.reset(key=key, rule_name=rule_name)
    return {"status": "reset"}


@router.post("/cleanup")
async def cleanup_expired():
    """清理过期记录

    Returns:
        清理结果
    """
    limiter = get_rate_limiter()
    count = limiter.cleanup()
    return {"cleaned": count}
