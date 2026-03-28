"""列表并集工具 - 计算多个列表的并集元素"""
from typing import Any, List
from dataclasses import dataclass


@dataclass
class UnionResult:
    """并集结果"""
    union: List[Any]
    count: int
    from_count: int


def list_union(*lists: List[Any]) -> UnionResult:
    """
    计算多个列表的并集元素（去重）

    Args:
        *lists: 任意数量的列表

    Returns:
        UnionResult: 包含并集元素、数量和来源数量的结果

    Example:
        >>> result = list_union([1, 2, 3], [2, 3, 4], [3, 4, 5])
        >>> result.union
        [1, 2, 3, 4, 5]
    """
    if not lists:
        return UnionResult(union=[], count=0, from_count=0)

    # 合并所有元素
    all_elements = []
    for lst in lists:
        all_elements.extend(lst)

    # 去重并排序
    unique = list(set(all_elements))
    unique.sort(key=lambda x: str(x) if not isinstance(x, (int, float)) else x)

    return UnionResult(
        union=unique,
        count=len(unique),
        from_count=len(lists)
    )


def list_union_by_key(*lists: List[dict], key: str) -> List[dict]:
    """
    根据键计算字典列表的并集（去重）

    Args:
        *lists: 字典列表
        key: 用于比较的键

    Returns:
        包含并集元素的字典列表

    Example:
        >>> list1 = [{'id': 1, 'name': 'a'}, {'id': 2, 'name': 'b'}]
        >>> list2 = [{'id': 2, 'name': 'b'}, {'id': 3, 'name': 'c'}]
        >>> list_union_by_key(list1, list2, key='id')
        [{'id': 1, 'name': 'a'}, {'id': 2, 'name': 'b'}, {'id': 3, 'name': 'c'}]
    """
    if not lists or not key:
        return []

    seen_keys = set()
    result = []

    for lst in lists:
        for item in lst:
            if isinstance(item, dict) and key in item:
                item_key = item[key]
                if item_key not in seen_keys:
                    seen_keys.add(item_key)
                    result.append(item)

    return result


if __name__ == "__main__":
    # 测试
    r1 = list_union([1, 2, 3], [2, 3, 4], [3, 4, 5])
    print(f"并集: {r1.union}, 数量: {r1.count}, 来源: {r1.from_count}")

    r2 = list_union(['a', 'b', 'c'], ['b', 'c', 'd'])
    print(f"并集: {r2.union}, 数量: {r2.count}, 来源: {r2.from_count}")

    r3 = list_union([1, 2], [3, 4])
    print(f"并集: {r3.union}, 数量: {r3.count}, 来源: {r3.from_count}")
