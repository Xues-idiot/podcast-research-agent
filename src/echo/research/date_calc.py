"""日期计算工具"""

from datetime import datetime, timedelta
from typing import Optional


class DateCalcTool:
    _instance: Optional["DateCalcTool"] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def add_days(self, date_str: str, days: int) -> str:
        try:
            dt = datetime.strptime(date_str, "%Y-%m-%d")
            new_dt = dt + timedelta(days=days)
            return new_dt.strftime("%Y-%m-%d")
        except:
            return date_str

    def days_between(self, date1: str, date2: str) -> int:
        try:
            d1 = datetime.strptime(date1, "%Y-%m-%d")
            d2 = datetime.strptime(date2, "%Y-%m-%d")
            return abs((d2 - d1).days)
        except:
            return 0

    def is_weekend(self, date_str: str) -> bool:
        try:
            dt = datetime.strptime(date_str, "%Y-%m-%d")
            return dt.weekday() >= 5
        except:
            return False


def get_date_calc_tool() -> DateCalcTool:
    return DateCalcTool()