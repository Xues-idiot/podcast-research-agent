"""时间工具集合"""
from datetime import datetime, timedelta
from typing import Optional


def time_now() -> str:
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")


def time_today() -> str:
    return datetime.now().strftime("%Y-%m-%d")


def time_timestamp() -> float:
    return datetime.now().timestamp()


def time_from_timestamp(ts: float) -> str:
    return datetime.fromtimestamp(ts).strftime("%Y-%m-%d %H:%M:%S")


def time_add(dt_str: str, days: int = 0, hours: int = 0, minutes: int = 0) -> str:
    dt = datetime.strptime(dt_str, "%Y-%m-%d %H:%M:%S")
    dt += timedelta(days=days, hours=hours, minutes=minutes)
    return dt.strftime("%Y-%m-%d %H:%M:%S")


def time_diff(dt1_str: str, dt2_str: str) -> dict:
    dt1 = datetime.strptime(dt1_str, "%Y-%m-%d %H:%M:%S")
    dt2 = datetime.strptime(dt2_str, "%Y-%m-%d %H:%M:%S")
    delta = dt2 - dt1
    return {
        "days": delta.days,
        "hours": delta.total_seconds() / 3600,
        "minutes": delta.total_seconds() / 60,
        "seconds": delta.total_seconds()
    }


def time_format(dt_str: str, fmt: str) -> str:
    dt = datetime.strptime(dt_str, "%Y-%m-%d %H:%M:%S")
    return dt.strftime(fmt)


def time_parse(dt_str: str, fmt: str) -> str:
    return datetime.strptime(dt_str, fmt).isoformat()
