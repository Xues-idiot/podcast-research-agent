"""时间转换工具"""

from typing import Optional


class TimeConverter:
    """时间转换工具"""

    def seconds_to_readable(self, seconds: int) -> str:
        """秒转可读时间"""
        if seconds < 60:
            return f"{seconds}秒"
        elif seconds < 3600:
            minutes = seconds // 60
            secs = seconds % 60
            return f"{minutes}分{secs}秒"
        elif seconds < 86400:
            hours = seconds // 3600
            mins = (seconds % 3600) // 60
            return f"{hours}小时{mins}分"
        else:
            days = seconds // 86400
            hours = (seconds % 86400) // 3600
            return f"{days}天{hours}小时"

    def minutes_to_readable(self, minutes: int) -> str:
        """分钟转可读时间"""
        return self.seconds_to_readable(minutes * 60)


_converter: Optional[TimeConverter] = None


def get_time_converter() -> TimeConverter:
    global _converter
    if _converter is None:
        _converter = TimeConverter()
    return _converter