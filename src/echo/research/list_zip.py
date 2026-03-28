"""列表合并工具 - 将多个列表合并"""
from typing import Any, List, Optional, Tuple
from dataclasses import dataclass


@dataclass
class ZipResult:
    items: List[Tuple[Any, ...]]
    count: int


def list_zip(*lists: List[Any], fillvalue: Optional[Any] = None) -> ZipResult:
    """
    合并多个列表

    Args:
        *lists: 要合并的列表
        fillvalue: 填充值（用于不等长列表）

    Returns:
        ZipResult: 合并结果

    Example:
        >>> result = list_zip([1, 2], [3, 4])
        >>> result.items
        [(1, 3), (2, 4)]
    """
    from itertools import zip_longest
    if fillvalue is not None:
        items = list(zip_longest(*lists, fillvalue=fillvalue))
    else:
        items = list(zip(*lists))
    return ZipResult(items=items, count=len(items))


def list_concat(*lists: List[Any]) -> List[Any]:
    """
    连接多个列表

    Args:
        *lists: 要连接的列表

    Returns:
        连接后的列表

    Example:
        >>> list_concat([1, 2], [3, 4], [5])
        [1, 2, 3, 4, 5]
    """
    result = []
    for lst in lists:
        result.extend(lst)
    return result


def list_interleave(*lists: List[Any]) -> List[Any]:
    """
    交错合并多个列表

    Args:
        *lists: 要交错的列表

    Returns:
        交错后的列表

    Example:
        >>> list_interleave([1, 2], [3, 4])
        [1, 3, 2, 4]
    """
    result = []
    for items in zip(*lists):
        result.extend(items)
    return result


def list_zip_dict(keys: List[Any], values: List[Any]) -> dict:
    """
    将键和值列表合并为字典

    Args:
        keys: 键列表
        values: 值列表

    Returns:
        字典

    Example:
        >>> list_zip_dict([a, b], [1, 2])
        {a: 1, b: 2}
    """
    return dict(zip(keys, values))

