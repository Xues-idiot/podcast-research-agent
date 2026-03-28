"""日期时间工具"""
from datetime import datetime, timedelta, date
from typing import Optional, Union
from dataclasses import dataclass


@dataclass
class DateTimeResult:
    result: str
    timestamp: Optional[float]


def dt_now(format: str = "%Y-%m-%d %H:%M:%S") -> DateTimeResult:
    """获取当前时间"""
    now = datetime.now()
    return DateTimeResult(result=now.strftime(format), timestamp=now.timestamp())


def dt_today(format: str = "%Y-%m-%d") -> DateTimeResult:
    """获取今天日期"""
    today = date.today()
    return DateTimeResult(result=today.strftime(format), timestamp=None)


def dt_add(dt_str: str, days: int = 0, hours: int = 0, minutes: int = 0, format: str = "%Y-%m-%d %H:%M:%S") -> DateTimeResult:
    """日期加减"""
    dt = datetime.strptime(dt_str, format)
    new_dt = dt + timedelta(days=days, hours=hours, minutes=minutes)
    return DateTimeResult(result=new_dt.strftime(format), timestamp=new_dt.timestamp())


def dt_diff(dt1_str: str, dt2_str: str, format: str = "%Y-%m-%d %H:%M:%S") -> dict:
    """计算日期差"""
    dt1 = datetime.strptime(dt1_str, format)
    dt2 = datetime.strptime(dt2_str, format)
    delta = dt2 - dt1
    return {
        "days": delta.days,
        "seconds": delta.total_seconds(),
        "hours": delta.total_seconds() / 3600,
        "minutes": delta.total_seconds() / 60
    }


def dt_format(dt_str: str, from_format: str, to_format: str) -> DateTimeResult:
    """日期格式转换"""
    dt = datetime.strptime(dt_str, from_format)
    return DateTimeResult(result=dt.strftime(to_format), timestamp=dt.timestamp())


def dt_timestamp(dt_str: str, format: str = "%Y-%m-%d %H:%M:%S") -> dict:
    """转时间戳"""
    dt = datetime.strptime(dt_str, format)
    return {"timestamp": dt.timestamp(), "datetime": dt_str}


def dt_from_timestamp(timestamp: float) -> DateTimeResult:
    """从时间戳转日期"""
    dt = datetime.fromtimestamp(timestamp)
    return DateTimeResult(result=dt.strftime("%Y-%m-%d %H:%M:%S"), timestamp=timestamp)

