"""集合工具集合"""
from typing import Any, List, Set


def set_create(*items: Any) -> Set[Any]:
    return set(items)


def set_add(s: Set[Any], item: Any) -> Set[Any]:
    result = set(s)
    result.add(item)
    return result


def set_remove(s: Set[Any], item: Any) -> Set[Any]:
    result = set(s)
    result.discard(item)
    return result


def set_union(*sets: Set[Any]) -> Set[Any]:
    result = set()
    for s in sets:
        result |= s
    return result


def set_intersect(*sets: Set[Any]) -> Set[Any]:
    if not sets:
        return set()
    result = sets[0]
    for s in sets[1:]:
        result &= s
    return result


def set_diff(s1: Set[Any], s2: Set[Any]) -> Set[Any]:
    return s1 - s2


def set_sym_diff(s1: Set[Any], s2: Set[Any]) -> Set[Any]:
    return s1 ^ s2


def set_is_subset(s1: Set[Any], s2: Set[Any]) -> bool:
    return s1 <= s2


def set_is_superset(s1: Set[Any], s2: Set[Any]) -> bool:
    return s1 >= s2


def set_to_list(s: Set[Any]) -> List[Any]:
    return list(s)


def list_to_set(lst: List[Any]) -> Set[Any]:
    return set(lst)
