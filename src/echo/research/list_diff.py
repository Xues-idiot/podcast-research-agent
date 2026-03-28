"""列表差集工具 - 计算列表的差集元素"""
from typing import Any, List
from dataclasses import dataclass


@dataclass
class DiffResult:
    """差集结果"""
    difference: List[Any]
    count: int
    from_count: int


def list_diff(*lists: List[Any]) -> DiffResult:
    """
    计算多个列表的差集（第一个列表减去后面所有列表的元素）

    Args:
        *lists: 任意数量的列表，第一个为被减列表

    Returns:
        DiffResult: 包含差集元素、数量和来源数量的结果

    Example:
        >>> result = list_diff([1, 2, 3, 4], [2, 3], [3, 4])
        >>> result.difference
        [1]
    """
    if not lists:
        return DiffResult(difference=[], count=0, from_count=0)

    if len(lists) == 1:
        result = list(lists[0])
        result.sort(key=lambda x: str(x) if not isinstance(x, (int, float)) else x)
        return DiffResult(difference=result, count=len(result), from_count=1)

    # 第一个列表减去后面所有列表的元素
    base = set(lists[0])
    for lst in lists[1:]:
        base -= set(lst)

    result = list(base)
    result.sort(key=lambda x: str(x) if not isinstance(x, (int, float)) else x)

    return DiffResult(
        difference=result,
        count=len(result),
        from_count=len(lists)
    )


def list_symmetric_diff(list1: List[Any], list2: List[Any]) -> DiffResult:
    """
    计算两个列表的对称差集（只出现在其中一个列表中的元素）

    Args:
        list1: 第一个列表
        list2: 第二个列表

    Returns:
        DiffResult: 包含对称差集元素、数量和来源数量的结果

    Example:
        >>> result = list_symmetric_diff([1, 2, 3], [2, 3, 4])
        >>> result.difference
        [1, 4]
    """
    set1 = set(list1)
    set2 = set(list2)

    result = list(set1 ^ set2)
    result.sort(key=lambda x: str(x) if not isinstance(x, (int, float)) else x)

    return DiffResult(
        difference=result,
        count=len(result),
        from_count=2
    )


if __name__ == "__main__":
    # 测试
    r1 = list_diff([1, 2, 3, 4], [2, 3], [3, 4])
    print(f"差集: {r1.difference}, 数量: {r1.count}, 来源: {r1.from_count}")

    r2 = list_diff(['a', 'b', 'c', 'd'], ['b', 'c'])
    print(f"差集: {r2.difference}, 数量: {r2.count}, 来源: {r2.from_count}")

    r3 = list_symmetric_diff([1, 2, 3], [2, 3, 4])
    print(f"对称差集: {r3.difference}, 数量: {r3.count}, 来源: {r3.from_count}")
