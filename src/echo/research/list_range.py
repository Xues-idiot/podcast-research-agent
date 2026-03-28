"""列表范围工具 - 生成数值范围列表"""
from typing import Any, List, Union
from dataclasses import dataclass


@dataclass
class RangeResult:
    items: List[Any]
    count: int


def list_range(
    start: Union[int, float],
    stop: Union[int, float],
    step: Union[int, float] = 1
) -> RangeResult:
    """
    生成数值范围列表

    Args:
        start: 起始值（包含）
        stop: 结束值（不包含）
        step: 步长

    Returns:
        RangeResult: 范围结果

    Example:
        >>> result = list_range(0, 5)
        >>> result.items
        [0, 1, 2, 3, 4]
    """
    if step == 0:
        raise ValueError("step cannot be 0")

    items = []
    current = start
    if step > 0:
        while current < stop:
            items.append(current)
            current += step
    else:
        while current > stop:
            items.append(current)
            current += step

    return RangeResult(items=items, count=len(items))


def list_range_inclusive(
    start: Union[int, float],
    stop: Union[int, float],
    step: Union[int, float] = 1
) -> RangeResult:
    """
    生成包含结束值的数值范围列表

    Args:
        start: 起始值（包含）
        stop: 结束值（包含）
        step: 步长

    Returns:
        RangeResult: 范围结果
    """
    return list_range(start, stop + (step if step > 0 else -step), step)


def list_times(n: int, func: Any = None) -> List[Any]:
    """
    生成重复n次的列表

    Args:
        n: 重复次数
        func: 可选的值生成函数

    Returns:
        重复列表

    Example:
        >>> list_times(3)
        [None, None, None]
        >>> list_times(3, lambda i: i * 2)
        [0, 2, 4]
    """
    if func is None:
        return [None] * n
    return [func(i) for i in range(n)]


def list_cycle(lst: List[Any], n: int) -> List[Any]:
    """
    将列表循环n次

    Args:
        lst: 源列表
        n: 循环次数

    Returns:
        循环后的列表

    Example:
        >>> list_cycle([1, 2], 3)
        [1, 2, 1, 2, 1, 2]
    """
    if not lst:
        return []
    return (lst * n)[:n * len(lst)]

