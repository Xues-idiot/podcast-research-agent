"""日期差计算工具"""

from typing import Optional
from datetime import datetime, date


class DateDiffTool:
    _instance: Optional["DateDiffTool"] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def days_between(self, start: date, end: date) -> int:
        """计算两个日期之间的天数"""
        return (end - start).days

    def hours_between(self, start: datetime, end: datetime) -> float:
        """计算两个datetime之间的小时数"""
        delta = end - start
        return delta.total_seconds() / 3600

    def minutes_between(self, start: datetime, end: datetime) -> float:
        """计算两个datetime之间的分钟数"""
        delta = end - start
        return delta.total_seconds() / 60

    def add_days(self, dt: date, days: int) -> date:
        """日期加天数"""
        from datetime import timedelta
        return dt + timedelta(days=days)

    def add_months(self, dt: date, months: int) -> date:
        """日期加月数"""
        month = dt.month - 1 + months
        year = dt.year + month // 12
        month = month % 12 + 1
        day = min(dt.day, [31, 29 if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0) else 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31][month - 1])
        return date(year, month, day)


def get_date_diff_tool() -> DateDiffTool:
    return DateDiffTool()