"""列表变换工具 - 对列表进行各种变换"""
from typing import Any, List, Callable
from dataclasses import dataclass


@dataclass
class TransformResult:
    items: List[Any]
    count: int


def list_transform(lst: List[Any], transform: Callable[[Any], Any]) -> TransformResult:
    result = [transform(item) for item in lst]
    return TransformResult(items=result, count=len(result))


def list_accumulate(lst: List[Any], func: Callable[[Any, Any], Any] = lambda a, b: a + b, initial: Any = None) -> List[Any]:
    if not lst:
        return []
    if initial is None:
        result = [lst[0]]
        for item in lst[1:]:
            result.append(func(result[-1], item))
    else:
        result = [initial]
        for item in lst:
            result.append(func(result[-1], item))
    return result


def list_distinct(lst: List[Any]) -> List[Any]:
    seen = set()
    result = []
    for item in lst:
        if item not in seen:
            seen.add(item)
            result.append(item)
    return result


def list_compact(lst: List[Any]) -> List[Any]:
    return [item for item in lst if item]


def list_flatten_deep(lst: List[Any], depth: int = -1) -> List[Any]:
    result = []
    def _flatten(items, current_depth):
        for item in items:
            if isinstance(item, (list, tuple)) and (depth < 0 or current_depth < depth):
                _flatten(item, current_depth + 1)
            else:
                result.append(item)
    _flatten(lst, 0)
    return result

