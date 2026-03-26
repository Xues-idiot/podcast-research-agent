"""API速率限制器 - 防止API滥用"""

import time
from collections import defaultdict
from dataclasses import dataclass
from datetime import datetime, timedelta
from enum import Enum
from typing import Optional


class RateLimitScope(Enum):
    """速率限制范围"""
    GLOBAL = "global"
    USER = "user"
    IP = "ip"
    ENDPOINT = "endpoint"


@dataclass
class RateLimitRule:
    """速率限制规则"""
    scope: RateLimitScope = RateLimitScope.GLOBAL
    max_requests: int = 100  # 时间窗口内最大请求数
    window_seconds: int = 60  # 时间窗口（秒）
    burst: int = 10  # 突发允许的额外请求


@dataclass
class RateLimitStatus:
    """速率限制状态"""
    allowed: bool  # 是否允许请求
    remaining: int  # 剩余请求数
    reset_at: float  # 重置时间戳
    retry_after: float = 0  # 多少秒后重试


class RateLimiter:
    """速率限制器"""

    # 默认限制规则
    DEFAULT_RULES = {
        "global": RateLimitRule(scope=RateLimitScope.GLOBAL, max_requests=500, window_seconds=60),
        "chat": RateLimitRule(scope=RateLimitScope.USER, max_requests=30, window_seconds=60),
        "research": RateLimitRule(scope=RateLimitScope.USER, max_requests=10, window_seconds=60),
        "export": RateLimitRule(scope=RateLimitScope.USER, max_requests=20, window_seconds=60),
        "search": RateLimitRule(scope=RateLimitScope.USER, max_requests=60, window_seconds=60),
    }

    def __init__(self):
        """初始化速率限制器"""
        self._requests: dict = defaultdict(list)  # key -> [timestamps]
        self._rules = self.DEFAULT_RULES.copy()
        self._enabled = True

    def set_enabled(self, enabled: bool):
        """设置是否启用"""
        self._enabled = enabled

    def set_rule(self, name: str, rule: RateLimitRule):
        """设置限制规则"""
        self._rules[name] = rule

    def check(
        self,
        key: str,
        rule_name: str = "global",
        user_id: Optional[str] = None,
        ip: Optional[str] = None,
    ) -> RateLimitStatus:
        """检查请求是否允许

        Args:
            key: 标识键（如API key、user id）
            rule_name: 规则名称
            user_id: 用户ID
            ip: IP地址

        Returns:
            限制状态
        """
        if not self._enabled:
            return RateLimitStatus(allowed=True, remaining=999, reset_at=0)

        rule = self._rules.get(rule_name, self.DEFAULT_RULES["global"])

        # 构建存储键
        if rule.scope == RateLimitScope.GLOBAL:
            storage_key = f"global:{rule_name}"
        elif rule.scope == RateLimitScope.USER:
            storage_key = f"user:{user_id}:{rule_name}" if user_id else key
        elif rule.scope == RateLimitScope.IP:
            storage_key = f"ip:{ip}:{rule_name}" if ip else key
        else:
            storage_key = f"{key}:{rule_name}"

        now = time.time()
        window_start = now - rule.window_seconds

        # 获取当前窗口内的请求
        requests = self._requests[storage_key]
        recent_requests = [t for t in requests if t > window_start]

        # 计算剩余请求数
        remaining = rule.max_requests - len(recent_requests)
        reset_at = now + rule.window_seconds

        if remaining <= 0:
            # 计算重试时间
            oldest = min(recent_requests) if recent_requests else now
            retry_after = oldest + rule.window_seconds - now

            return RateLimitStatus(
                allowed=False,
                remaining=0,
                reset_at=reset_at,
                retry_after=retry_after,
            )

        # 允许请求
        recent_requests.append(now)
        self._requests[storage_key] = recent_requests

        return RateLimitStatus(
            allowed=True,
            remaining=remaining - 1,
            reset_at=reset_at,
        )

    def consume(
        self,
        key: str,
        rule_name: str = "global",
        user_id: Optional[str] = None,
        ip: Optional[str] = None,
        cost: int = 1,
    ) -> RateLimitStatus:
        """消费请求配额

        Args:
            key: 标识键
            rule_name: 规则名称
            user_id: 用户ID
            ip: IP地址
            cost: 消耗配额

        Returns:
            限制状态
        """
        if not self._enabled:
            return RateLimitStatus(allowed=True, remaining=999, reset_at=0)

        rule = self._rules.get(rule_name, self.DEFAULT_RULES["global"])

        # 构建存储键
        if rule.scope == RateLimitScope.GLOBAL:
            storage_key = f"global:{rule_name}"
        elif rule.scope == RateLimitScope.USER:
            storage_key = f"user:{user_id}:{rule_name}" if user_id else key
        elif rule.scope == RateLimitScope.IP:
            storage_key = f"ip:{ip}:{rule_name}" if ip else key
        else:
            storage_key = f"{key}:{rule_name}"

        now = time.time()
        window_start = now - rule.window_seconds

        # 获取当前窗口内的请求
        requests = self._requests[storage_key]
        recent_requests = [t for t in requests if t > window_start]

        # 计算剩余请求数
        remaining = rule.max_requests - len(recent_requests)

        if remaining < cost:
            # 计算重试时间
            oldest = min(recent_requests) if recent_requests else now
            retry_after = oldest + rule.window_seconds - now

            return RateLimitStatus(
                allowed=False,
                remaining=0,
                reset_at=now + rule.window_seconds,
                retry_after=retry_after,
            )

        # 消耗配额
        for _ in range(cost):
            recent_requests.append(now)
        self._requests[storage_key] = recent_requests

        return RateLimitStatus(
            allowed=True,
            remaining=remaining - cost,
            reset_at=now + rule.window_seconds,
        )

    def get_status(
        self,
        key: str,
        rule_name: str = "global",
        user_id: Optional[str] = None,
    ) -> RateLimitStatus:
        """获取限制状态（不消耗配额）"""
        rule = self._rules.get(rule_name, self.DEFAULT_RULES["global"])

        if rule.scope == RateLimitScope.USER:
            storage_key = f"user:{user_id}:{rule_name}" if user_id else key
        else:
            storage_key = f"global:{rule_name}"

        now = time.time()
        window_start = now - rule.window_seconds

        requests = self._requests[storage_key]
        recent_requests = [t for t in requests if t > window_start]

        remaining = rule.max_requests - len(recent_requests)

        return RateLimitStatus(
            allowed=remaining > 0,
            remaining=max(0, remaining),
            reset_at=now + rule.window_seconds,
        )

    def reset(self, key: str = None, rule_name: str = None):
        """重置限制"""
        if key and rule_name:
            storage_key = f"{key}:{rule_name}"
            if storage_key in self._requests:
                del self._requests[storage_key]
        elif key:
            # 重置该key的所有规则
            keys_to_delete = [k for k in self._requests.keys() if k.startswith(key)]
            for k in keys_to_delete:
                del self._requests[k]
        else:
            # 重置所有
            self._requests.clear()

    def cleanup(self):
        """清理过期记录"""
        now = time.time()
        max_window = max(rule.window_seconds for rule in self._rules.values())

        keys_to_delete = []
        for key, requests in self._requests.items():
            window_start = now - max_window
            recent = [t for t in requests if t > window_start]
            if recent:
                self._requests[key] = recent
            else:
                keys_to_delete.append(key)

        for key in keys_to_delete:
            del self._requests[key]

        return len(keys_to_delete)


# 全局实例
_rate_limiter: Optional[RateLimiter] = None


def get_rate_limiter() -> RateLimiter:
    """获取全局速率限制器"""
    global _rate_limiter
    if _rate_limiter is None:
        _rate_limiter = RateLimiter()
    return _rate_limiter
