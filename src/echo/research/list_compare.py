"""列表比较工具 - 比较两个列表"""
from typing import Any, List, Tuple
from dataclasses import dataclass


@dataclass
class CompareResult:
    equal: bool
    same_length: bool
    length_diff: int
    common: List[Any]
    only_in_first: List[Any]
    only_in_second: List[Any]


def list_compare(list1: List[Any], list2: List[Any]) -> CompareResult:
    """
    比较两个列表

    Args:
        list1: 第一个列表
        list2: 第二个列表

    Returns:
        CompareResult: 比较结果

    Example:
        >>> result = list_compare([1, 2, 3], [2, 3, 4])
        >>> result.equal
        False
        >>> result.common
        [2, 3]
    """
    set1 = set(list1)
    set2 = set(list2)

    common = list(set1 & set2)
    only_in_first = list(set1 - set2)
    only_in_second = list(set2 - set1)

    return CompareResult(
        equal=list1 == list2,
        same_length=len(list1) == len(list2),
        length_diff=len(list1) - len(list2),
        common=common,
        only_in_first=only_in_first,
        only_in_second=only_in_second
    )


def list_is_subsequence(sub: List[Any], main: List[Any]) -> bool:
    """
    检查sub是否为main的子序列

    Args:
        sub: 候选子序列
        main: 主列表

    Returns:
        是否为子序列

    Example:
        >>> list_is_subsequence([1, 3, 5], [1, 2, 3, 4, 5])
        True
    """
    idx = 0
    for item in main:
        if idx < len(sub) and item == sub[idx]:
            idx += 1
    return idx == len(sub)


def list_starts_with(lst: List[Any], prefix: List[Any]) -> bool:
    """检查列表是否以指定前缀开始"""
    if len(prefix) > len(lst):
        return False
    return lst[:len(prefix)] == prefix


def list_ends_with(lst: List[Any], suffix: List[Any]) -> bool:
    """检查列表是否以指定后缀结束"""
    if len(suffix) > len(lst):
        return False
    return lst[-len(suffix):] == suffix


def list_is_prefixed(lst: List[Any], prefix: List[Any]) -> bool:
    """同list_starts_with"""
    return list_starts_with(lst, prefix)


def list_is_suffixed(lst: List[Any], suffix: List[Any]) -> bool:
    """同list_ends_with"""
    return list_ends_with(lst, suffix)

