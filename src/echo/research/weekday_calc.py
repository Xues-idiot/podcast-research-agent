"""星期计算工具"""

from typing import Optional
from datetime import date


class WeekdayCalcTool:
    _instance: Optional["WeekdayCalcTool"] = None

    WEEKDAY_NAMES = ["周一", "周二", "周三", "周四", "周五", "周六", "周日"]
    WEEKDAY_NAMES_EN = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def get_weekday(self, dt: date) -> int:
        """获取星期几 (0=周一, 6=周日)"""
        return dt.weekday()

    def get_weekday_name(self, dt: date, lang: str = "zh") -> str:
        """获取星期名称"""
        idx = self.get_weekday(dt)
        if lang == "en":
            return self.WEEKDAY_NAMES_EN[idx]
        return self.WEEKDAY_NAMES[idx]

    def is_weekend(self, dt: date) -> bool:
        """判断是否是周末"""
        return dt.weekday() >= 5

    def next_weekday(self, dt: date, target_weekday: int) -> date:
        """获取下一个指定星期几的日期"""
        days_ahead = target_weekday - dt.weekday()
        if days_ahead <= 0:
            days_ahead += 7
        from datetime import timedelta
        return dt + timedelta(days=days_ahead)

    def business_days_between(self, start: date, end: date) -> int:
        """计算两个日期之间的工作日天数"""
        days = 0
        current = start
        from datetime import timedelta
        while current <= end:
            if current.weekday() < 5:
                days += 1
            current += timedelta(days=1)
        return days


def get_weekday_calc_tool() -> WeekdayCalcTool:
    return WeekdayCalcTool()