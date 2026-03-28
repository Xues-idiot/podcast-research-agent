"""时区转换工具"""

from datetime import datetime
from typing import Optional, Dict


class TimezoneConvertTool:
    _instance: Optional["TimezoneConvertTool"] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def convert(self, time_str: str, from_tz: str, to_tz: str) -> str:
        offsets: Dict[str, int] = {
            "UTC": 0, "EST": -5, "CST": 8, "JST": 9,
            "PST": -8, "GMT": 0, "CET": 1, "AEST": 10
        }
        from_offset = offsets.get(from_tz.upper(), 0)
        to_offset = offsets.get(to_tz.upper(), 0)
        try:
            dt = datetime.strptime(time_str, "%Y-%m-%d %H:%M:%S")
            utc_dt = dt.replace(hour=dt.hour - from_offset)
            target_dt = utc_dt.replace(hour=utc_dt.hour + to_offset)
            return target_dt.strftime("%Y-%m-%d %H:%M:%S")
        except:
            return time_str


def get_timezone_convert_tool() -> TimezoneConvertTool:
    return TimezoneConvertTool()