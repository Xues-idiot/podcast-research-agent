"""列表采样工具 - 从列表中随机抽取样本"""
from typing import Any, List, Optional
import random


def list_sample(
    lst: List[Any],
    n: int = 1,
    replace: bool = False
) -> List[Any]:
    """
    从列表中随机抽取样本

    Args:
        lst: 源列表
        n: 抽取数量
        replace: 是否放回抽样

    Returns:
        样本列表

    Example:
        >>> result = list_sample([1, 2, 3, 4, 5], n=2)
        >>> len(result)
        2
    """
    if n < 1:
        return []
    if replace:
        return random.choices(lst, k=n)
    else:
        if n > len(lst):
            n = len(lst)
        return random.sample(lst, k=n)


def list_shuffle_sample(lst: List[Any], fraction: float = 0.1) -> List[Any]:
    """
    按比例随机打乱并返回样本

    Args:
        lst: 源列表
        fraction: 采样比例 (0-1)

    Returns:
        样本列表
    """
    result = list(lst)
    random.shuffle(result)
    n = max(1, int(len(result) * fraction))
    return result[:n]


def list_random_item(lst: List[Any]) -> Any:
    """随机返回一个元素"""
    if not lst:
        return None
    return random.choice(lst)


def list_random_pair(lst: List[Any]) -> List[Any]:
    """随机返回两个不重复的元素"""
    if len(lst) < 2:
        return lst
    return random.sample(lst, k=2)

