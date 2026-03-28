"""列表分区工具 - 将列表按条件分区"""
from typing import Any, List, Callable, Tuple
from dataclasses import dataclass


@dataclass
class PartitionResult:
    matches: List[Any]
    non_matches: List[Any]
    match_count: int
    non_match_count: int


def list_partition(
    lst: List[Any],
    predicate: Callable[[Any], bool]
) -> PartitionResult:
    """
    将列表按条件分为两部分

    Args:
        lst: 源列表
        predicate: 条件函数

    Returns:
        PartitionResult: 分区结果

    Example:
        >>> result = list_partition([1, 2, 3, 4, 5], lambda x: x % 2 == 0)
        >>> result.matches
        [2, 4]
        >>> result.non_matches
        [1, 3, 5]
    """
    matches = []
    non_matches = []

    for item in lst:
        if predicate(item):
            matches.append(item)
        else:
            non_matches.append(item)

    return PartitionResult(
        matches=matches,
        non_matches=non_matches,
        match_count=len(matches),
        non_match_count=len(non_matches)
    )


def list_group_by(
    lst: List[Any],
    key: Callable[[Any], Any]
) -> dict:
    """
    按键函数对列表元素分组

    Args:
        lst: 源列表
        key: 键函数

    Returns:
        分组字典

    Example:
        >>> result = list_group_by([1, 2, 3, 4, 5], lambda x: x % 2)
        >>> result
        {0: [2, 4], 1: [1, 3, 5]}
    """
    groups = {}
    for item in lst:
        k = key(item)
        if k not in groups:
            groups[k] = []
        groups[k].append(item)
    return groups


def list_chunk_by_count(lst: List[Any], chunk_count: int) -> List[List[Any]]:
    """
    将列表分成指定数量的块

    Args:
        lst: 源列表
        chunk_count: 块数量

    Returns:
        分块列表

    Example:
        >>> list_chunk_by_count([1, 2, 3, 4, 5, 6, 7], 3)
        [[1, 2, 3], [4, 5, 6], [7]]
    """
    if chunk_count <= 0:
        raise ValueError("chunk_count must be greater than 0")

    chunk_size = len(lst) / chunk_count
    result = []
    for i in range(chunk_count):
        start = int(i * chunk_size)
        end = int((i + 1) * chunk_size)
        result.append(lst[start:end])
    return result


def list_split_at(lst: List[Any], index: int) -> Tuple[List[Any], List[Any]]:
    """
    在指定索引处分割列表

    Args:
        lst: 源列表
        index: 分割索引

    Returns:
        (前部分, 后部分)

    Example:
        >>> list_split_at([1, 2, 3, 4, 5], 2)
        ([1, 2], [3, 4, 5])
    """
    if index < 0:
        index = len(lst) + index
    return lst[:index], lst[index:]

