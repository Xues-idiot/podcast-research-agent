"""列表扁平化工具 - 将嵌套列表展开"""
from typing import Any, List, Union
from dataclasses import dataclass


@dataclass
class FlattenResult:
    """扁平化结果"""
    items: List[Any]
    count: int
    depth: int


def list_flatten(
    lst: List[Any],
    depth: int = -1
) -> FlattenResult:
    """
    将嵌套列表展开

    Args:
        lst: 源列表（可能包含嵌套列表）
        depth: 展开深度，-1表示全部展开

    Returns:
        FlattenResult: 包含扁平化结果的信息

    Example:
        >>> result = list_flatten([1, [2, [3, 4]], 5])
        >>> result.items
        [1, 2, 3, 4, 5]
    """
    if depth == 0:
        return FlattenResult(items=list(lst), count=len(lst), depth=0)

    result = []
    current_depth = 0

    def _flatten(items, current_depth):
        for item in items:
            if isinstance(item, (list, tuple)) and current_depth < depth or depth < 0:
                _flatten(item, current_depth + 1)
            else:
                result.append(item)

    _flatten(lst, current_depth)

    return FlattenResult(
        items=result,
        count=len(result),
        depth=current_depth
    )


def list_flatten_once(lst: List[Any]) -> List[Any]:
    """
    将嵌套列表展开一层

    Args:
        lst: 源列表

    Returns:
        扁平化一层后的列表

    Example:
        >>> list_flatten_once([1, [2, [3, 4]], 5])
        [1, 2, [3, 4], 5]
    """
    result = []
    for item in lst:
        if isinstance(item, (list, tuple)):
            result.extend(item)
        else:
            result.append(item)
    return result


def list_chunk_by_size(
    lst: List[Any],
    chunk_size: int
) -> List[List[Any]]:
    """
    将列表分成指定大小的块

    Args:
        lst: 源列表
        chunk_size: 每块的大小

    Returns:
        分块后的列表

    Example:
        >>> list_chunk_by_size([1, 2, 3, 4, 5, 6, 7], 3)
        [[1, 2, 3], [4, 5, 6], [7]]
    """
    if chunk_size <= 0:
        raise ValueError("chunk_size must be greater than 0")

    result = []
    for i in range(0, len(lst), chunk_size):
        result.append(lst[i:i + chunk_size])
    return result


def list_window(
    lst: List[Any],
    window_size: int,
    step: int = 1
) -> List[List[Any]]:
    """
    创建滑动窗口

    Args:
        lst: 源列表
        window_size: 窗口大小
        step: 滑动步长

    Returns:
        窗口列表

    Example:
        >>> list_window([1, 2, 3, 4, 5], window_size=3)
        [[1, 2, 3], [2, 3, 4], [3, 4, 5]]
    """
    if window_size <= 0:
        raise ValueError("window_size must be greater than 0")
    if step <= 0:
        raise ValueError("step must be greater than 0")

    result = []
    for i in range(0, len(lst) - window_size + 1, step):
        result.append(lst[i:i + window_size])
    return result


if __name__ == "__main__":
    # 测试
    r1 = list_flatten([1, [2, [3, 4]], 5])
    print(f"扁平化: {r1.items}, 数量: {r1.count}, 深度: {r1.depth}")

    r2 = list_flatten_once([1, [2, [3, 4]], 5])
    print(f"扁平化一层: {r2}")

    r3 = list_chunk_by_size([1, 2, 3, 4, 5, 6, 7], 3)
    print(f"分块: {r3}")

    r4 = list_window([1, 2, 3, 4, 5], window_size=3)
    print(f"滑动窗口: {r4}")
