"""列表排序工具 - 对列表进行排序"""
from typing import Any, List, Callable, Optional
from dataclasses import dataclass


@dataclass
class SortResult:
    items: List[Any]
    count: int
    reverse: bool


def list_sort(
    lst: List[Any],
    reverse: bool = False,
    key: Optional[Callable[[Any], Any]] = None
) -> SortResult:
    """
    对列表进行排序

    Args:
        lst: 源列表
        reverse: 是否降序
        key: 排序键函数

    Returns:
        SortResult: 排序结果

    Example:
        >>> result = list_sort([3, 1, 4, 1, 5])
        >>> result.items
        [1, 1, 3, 4, 5]
    """
    result = sorted(lst, reverse=reverse, key=key)
    return SortResult(items=result, count=len(result), reverse=reverse)


def list_reverse(lst: List[Any]) -> List[Any]:
    """反转列表"""
    return list(reversed(lst))


def list_shuffle(lst: List[Any]) -> List[Any]:
    """随机打乱列表"""
    import random
    result = list(lst)
    random.shuffle(result)
    return result


def list_sort_by_length(lst: List[Any], reverse: bool = False) -> SortResult:
    """按元素长度排序"""
    return list_sort(lst, reverse=reverse, key=len)

