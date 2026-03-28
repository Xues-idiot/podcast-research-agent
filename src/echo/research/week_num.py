"""周数计算工具"""

from datetime import datetime
from typing import Optional


class WeekNumTool:
    _instance: Optional["WeekNumTool"] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def get_week_number(self, date_str: str) -> int:
        try:
            dt = datetime.strptime(date_str, "%Y-%m-%d")
            return dt.isocalendar()[1]
        except:
            return 0

    def get_day_of_week(self, date_str: str) -> str:
        days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
        try:
            dt = datetime.strptime(date_str, "%Y-%m-%d")
            return days[dt.weekday()]
        except:
            return ""


def get_week_num_tool() -> WeekNumTool:
    return WeekNumTool()