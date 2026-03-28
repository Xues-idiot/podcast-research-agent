"""字符串处理工具 - 字符串操作集合"""
from typing import List, Optional
from dataclasses import dataclass


@dataclass
class StringResult:
    result: str
    length: int


def str_reverse(s: str) -> StringResult:
    return StringResult(result=s[::-1], length=len(s))


def str_upper(s: str) -> StringResult:
    return StringResult(result=s.upper(), length=len(s))


def str_lower(s: str) -> StringResult:
    return StringResult(result=s.lower(), length=len(s))


def str_title(s: str) -> StringResult:
    return StringResult(result=s.title(), length=len(s))


def str_capitalize(s: str) -> StringResult:
    return StringResult(result=s.capitalize(), length=len(s))


def str_strip(s: str, chars: Optional[str] = None) -> StringResult:
    return StringResult(result=s.strip(chars), length=len(s.strip(chars)))


def str_split_lines(s: str) -> List[str]:
    return s.splitlines()


def str_count(s: str, sub: str) -> int:
    return s.count(sub)


def str_replace(s: str, old: str, new: str) -> StringResult:
    return StringResult(result=s.replace(old, new), length=len(s.replace(old, new)))


def str_contains(s: str, sub: str) -> bool:
    return sub in s

