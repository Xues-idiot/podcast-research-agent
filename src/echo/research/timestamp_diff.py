"""时间戳差计算工具"""

from typing import Optional
from datetime import datetime


class TimestampDiffTool:
    _instance: Optional["TimestampDiffTool"] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def seconds_between(self, ts1: int, ts2: int) -> int:
        """秒数差"""
        return abs(ts1 - ts2)

    def minutes_between(self, ts1: int, ts2: int) -> float:
        """分钟数差"""
        return abs(ts1 - ts2) / 60

    def hours_between(self, ts1: int, ts2: int) -> float:
        """小时数差"""
        return abs(ts1 - ts2) / 3600

    def days_between(self, ts1: int, ts2: int) -> float:
        """天数差"""
        return abs(ts1 - ts2) / 86400

    def is_within_seconds(self, ts1: int, ts2: int, threshold: int) -> bool:
        """判断两个时间戳是否在指定秒数内"""
        return abs(ts1 - ts2) <= threshold

    def age_string(self, timestamp: int) -> str:
        """将时间戳转为相对时间字符串"""
        now = int(datetime.now().timestamp())
        diff = now - timestamp
        if diff < 60:
            return f"{diff}秒前"
        elif diff < 3600:
            return f"{diff // 60}分钟前"
        elif diff < 86400:
            return f"{diff // 3600}小时前"
        else:
            return f"{diff // 86400}天前"


_ts_diff_instance: Optional[TimestampDiffTool] = None


def get_timestamp_diff_tool() -> TimestampDiffTool:
    global _ts_diff_instance
    if _ts_diff_instance is None:
        _ts_diff_instance = TimestampDiffTool()
    return _ts_diff_instance