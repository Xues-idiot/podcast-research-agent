"""格式化工具集合"""
from typing import Any, List
import json


def format_json(obj: Any, indent: int = 2) -> str:
    return json.dumps(obj, indent=indent, ensure_ascii=False)


def format_number(num: float, decimals: int = 2) -> str:
    return f"{num:.{decimals}f}"


def format_currency(amount: float, symbol: str = "¥") -> str:
    return f"{symbol}{amount:,.2f}"


def format_percent(value: float, decimals: int = 1) -> str:
    return f"{value:.{decimals}f}%"


def format_file_size(bytes: int) -> str:
    for unit in ['B', 'KB', 'MB', 'GB', 'TB']:
        if bytes < 1024:
            return f"{bytes:.1f} {unit}"
        bytes /= 1024
    return f"{bytes:.1f} PB"


def format_duration(seconds: int) -> str:
    hours = seconds // 3600
    minutes = (seconds % 3600) // 60
    secs = seconds % 60
    if hours > 0:
        return f"{hours}h {minutes}m"
    if minutes > 0:
        return f"{minutes}m {secs}s"
    return f"{secs}s"


def format_phone(phone: str) -> str:
    if len(phone) == 11:
        return f"{phone[:3]}-{phone[3:7]}-{phone[7:]}"
    return phone


def format_list(items: List, separator: str = ", ", last_separator: str = " 和 ") -> str:
    if not items:
        return ""
    if len(items) == 1:
        return str(items[0])
    return separator.join(str(x) for x in items[:-1]) + last_separator + str(items[-1])
