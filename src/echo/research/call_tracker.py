"""调用跟踪工具"""

from typing import Optional, Callable, List


class CallTracker:
    """调用跟踪工具"""

    def __init__(self):
        self._calls: List = []

    def track(self, func: Callable) -> Callable:
        """跟踪函数调用"""
        def wrapper(*args, **kwargs):
            self._calls.append((args, kwargs))
            return func(*args, **kwargs)
        return wrapper

    def get_calls(self) -> List:
        """获取调用记录"""
        return self._calls

    def clear(self) -> None:
        """清除记录"""
        self._calls.clear()


_call_tracker: Optional[CallTracker] = None


def get_call_tracker() -> CallTracker:
    global _call_tracker
    if _call_tracker is None:
        _call_tracker = CallTracker()
    return _call_tracker