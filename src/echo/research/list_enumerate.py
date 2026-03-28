"""列表枚举工具 - 为列表元素添加索引"""
from typing import Any, List, Tuple, Optional
from dataclasses import dataclass


@dataclass
class EnumerateResult:
    """枚举结果"""
    items: List[Tuple[int, Any]]
    count: int


def list_enumerate(
    lst: List[Any],
    start: int = 0,
    step: int = 1
) -> EnumerateResult:
    """
    为列表元素添加索引

    Args:
        lst: 源列表
        start: 起始索引
        step: 索引步长

    Returns:
        EnumerateResult: 包含枚举结果的信息

    Example:
        >>> result = list_enumerate(['a', 'b', 'c'], start=1)
        >>> result.items
        [(1, 'a'), (2, 'b'), (3, 'c')]
    """
    if step == 0:
        raise ValueError("step cannot be 0")

    items = []
    idx = start
    for item in lst:
        items.append((idx, item))
        idx += step

    return EnumerateResult(items=items, count=len(items))


def list_enumerate_dict(
    lst: List[Any],
    index_key: str = "index",
    value_key: str = "value",
    start: int = 0,
    step: int = 1
) -> List[dict]:
    """
    为列表元素添加索引，返回字典列表

    Args:
        lst: 源列表
        index_key: 索引键名
        value_key: 值键名
        start: 起始索引
        step: 索引步长

    Returns:
        字典列表

    Example:
        >>> result = list_enumerate_dict(['a', 'b', 'c'])
        >>> result
        [{'index': 0, 'value': 'a'}, {'index': 1, 'value': 'b'}, {'index': 2, 'value': 'c'}]
    """
    if step == 0:
        raise ValueError("step cannot be 0")

    idx = start
    result = []
    for item in lst:
        result.append({index_key: idx, value_key: item})
        idx += step

    return result


def list_with_index(lst: List[Any], index: int, default: Any = None) -> Any:
    """
    获取列表中指定索引的元素

    Args:
        lst: 源列表
        index: 索引
        default: 默认值

    Returns:
        元素值或默认值

    Example:
        >>> list_with_index(['a', 'b', 'c'], 1)
        'b'
        >>> list_with_index(['a', 'b', 'c'], 10, 'default')
        'default'
    """
    if index < 0:
        index = len(lst) + index
    if 0 <= index < len(lst):
        return lst[index]
    return default


if __name__ == "__main__":
    # 测试
    r1 = list_enumerate(['a', 'b', 'c'], start=1)
    print(f"枚举: {r1.items}, 数量: {r1.count}")

    r2 = list_enumerate_dict(['x', 'y', 'z'], index_key='i', value_key='v')
    print(f"字典枚举: {r2}")

    r3 = list_with_index([1, 2, 3], 1)
    print(f"索引1: {r3}")

    r4 = list_with_index([1, 2, 3], -1)
    print(f"倒数第一: {r4}")
