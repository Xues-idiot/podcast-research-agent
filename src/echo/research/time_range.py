"""时间范围工具"""

from typing import List, Optional
from datetime import datetime, timedelta


class TimeRangeTool:
    _instance: Optional["TimeRangeTool"] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def create_range(self, start: datetime, end: datetime, step_minutes: int = 60) -> List[datetime]:
        """创建时间范围列表"""
        result = []
        current = start
        while current <= end:
            result.append(current)
            current += timedelta(minutes=step_minutes)
        return result

    def is_within_range(self, dt: datetime, start: datetime, end: datetime) -> bool:
        """检查时间是否在范围内"""
        return start <= dt <= end

    def get_overlap(self, start1: datetime, end1: datetime, start2: datetime, end2: datetime) -> Optional[tuple]:
        """获取两个时间范围的重叠部分"""
        overlap_start = max(start1, start2)
        overlap_end = min(end1, end2)
        if overlap_start <= overlap_end:
            return (overlap_start, overlap_end)
        return None


def get_time_range_tool() -> TimeRangeTool:
    return TimeRangeTool()