"""列表交集工具 - 计算多个列表的交集元素"""
from typing import Any, List
from dataclasses import dataclass


@dataclass
class IntersectResult:
    """交集结果"""
    intersection: List[Any]
    count: int
    from_count: int


def list_intersect(*lists: List[Any]) -> IntersectResult:
    """
    计算多个列表的交集元素

    Args:
        *lists: 任意数量的列表

    Returns:
        IntersectResult: 包含交集元素、数量和来源数量的结果

    Example:
        >>> result = list_intersect([1, 2, 3], [2, 3, 4], [3, 4, 5])
        >>> result.intersection
        [3]
    """
    if not lists:
        return IntersectResult(intersection=[], count=0, from_count=0)

    # 过滤空列表
    non_empty_lists = [lst for lst in lists if lst]
    if not non_empty_lists:
        return IntersectResult(intersection=[], count=0, from_count=len(lists))

    # 计算交集
    intersection = set(non_empty_lists[0])
    for lst in non_empty_lists[1:]:
        intersection &= set(lst)

    result_list = list(intersection)
    result_list.sort(key=lambda x: str(x) if not isinstance(x, (int, float)) else x)

    return IntersectResult(
        intersection=result_list,
        count=len(result_list),
        from_count=len(non_empty_lists)
    )


def list_intersect_by_key(*lists: List[dict], key: str) -> List[dict]:
    """
    根据键计算字典列表的交集

    Args:
        *lists: 字典列表
        key: 用于比较的键

    Returns:
        包含交集元素的字典列表

    Example:
        >>> list1 = [{'id': 1, 'name': 'a'}, {'id': 2, 'name': 'b'}]
        >>> list2 = [{'id': 2, 'name': 'b'}, {'id': 3, 'name': 'c'}]
        >>> list_intersect_by_key(list1, list2, key='id')
        [{'id': 2, 'name': 'b'}]
    """
    if not lists or not key:
        return []

    non_empty_lists = [lst for lst in lists if lst]
    if not non_empty_lists:
        return []

    # 提取所有键值
    key_sets = []
    for lst in non_empty_lists:
        key_set = set()
        for item in lst:
            if isinstance(item, dict) and key in item:
                key_set.add(item[key])
        key_sets.append(key_set)

    # 计算键值交集
    common_keys = set(key_sets[0])
    for ks in key_sets[1:]:
        common_keys &= ks

    # 构建结果
    result = []
    for lst in non_empty_lists:
        for item in lst:
            if isinstance(item, dict) and item.get(key) in common_keys:
                if item not in result:
                    result.append(item)

    return result


if __name__ == "__main__":
    # 测试
    r1 = list_intersect([1, 2, 3], [2, 3, 4], [3, 4, 5])
    print(f"交集: {r1.intersection}, 数量: {r1.count}, 来源: {r1.from_count}")

    r2 = list_intersect(['a', 'b', 'c'], ['b', 'c', 'd'])
    print(f"交集: {r2.intersection}, 数量: {r2.count}, 来源: {r2.from_count}")

    r3 = list_intersect([1, 2], [3, 4])
    print(f"交集: {r3.intersection}, 数量: {r3.count}, 来源: {r3.from_count}")
