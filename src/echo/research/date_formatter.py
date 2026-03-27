"""日期格式化工具"""

from datetime import datetime
from typing import Optional


class DateFormatter:
    """日期格式化工具"""

    def format_datetime(self, dt: datetime, format_str: str = "%Y-%m-%d %H:%M:%S") -> str:
        """格式化日期时间"""
        return dt.strftime(format_str)

    def parse_datetime(self, date_str: str, format_str: str = "%Y-%m-%d %H:%M:%S") -> datetime:
        """解析日期时间"""
        return datetime.strptime(date_str, format_str)

    def now(self, format_str: str = "%Y-%m-%d %H:%M:%S") -> str:
        """当前时间"""
        return datetime.now().strftime(format_str)

    def to_iso(self, dt: datetime) -> str:
        """转ISO格式"""
        return dt.isoformat()


_formatter: Optional[DateFormatter] = None


def get_date_formatter() -> DateFormatter:
    global _formatter
    if _formatter is None:
        _formatter = DateFormatter()
    return _formatter