"""列表去重工具 - 去除列表中的重复元素"""
from typing import Any, List, Callable
from dataclasses import dataclass


@dataclass
class UniqueResult:
    items: List[Any]
    count: int
    removed_count: int


def list_unique(lst: List[Any], preserve_order: bool = True) -> UniqueResult:
    if preserve_order:
        seen = set()
        result = []
        for item in lst:
            if item not in seen:
                seen.add(item)
                result.append(item)
        removed = len(lst) - len(result)
    else:
        result = list(set(lst))
        result.sort()
        removed = len(lst) - len(result)
    return UniqueResult(items=result, count=len(result), removed_count=removed)


def list_duplicates(lst: List[Any]) -> List[Any]:
    seen = set()
    duplicates = set()
    for item in lst:
        if item in seen:
            duplicates.add(item)
        else:
            seen.add(item)
    return list(duplicates)


def list_is_unique(lst: List[Any]) -> bool:
    return len(lst) == len(set(lst))

