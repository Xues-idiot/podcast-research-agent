"""速率限制工具"""

import time
from collections import defaultdict
from typing import Optional


class RateLimiter:
    """速率限制器"""

    def __init__(self):
        self._requests = defaultdict(list)

    def is_allowed(self, key: str, max_requests: int, window_seconds: int) -> bool:
        """检查是否允许请求"""
        now = time.time()
        window_start = now - window_seconds

        self._requests[key] = [t for t in self._requests[key] if t > window_start]

        if len(self._requests[key]) < max_requests:
            self._requests[key].append(now)
            return True
        return False

    def reset(self, key: str):
        """重置限制"""
        if key in self._requests:
            del self._requests[key]


_limiter: Optional[RateLimiter] = None


def get_rate_limiter() -> RateLimiter:
    global _limiter
    if _limiter is None:
        _limiter = RateLimiter()
    return _limiter