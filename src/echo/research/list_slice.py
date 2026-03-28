"""列表切片工具 - 获取列表的切片"""
from typing import Any, List, Optional
from dataclasses import dataclass


@dataclass
class SliceResult:
    """切片结果"""
    items: List[Any]
    count: int
    start: int
    end: int
    step: int


def list_slice(
    lst: List[Any],
    start: Optional[int] = None,
    end: Optional[int] = None,
    step: int = 1
) -> SliceResult:
    """
    获取列表的切片

    Args:
        lst: 源列表
        start: 起始索引（包含）
        end: 结束索引（不包含）
        step: 步长

    Returns:
        SliceResult: 包含切片结果的信息

    Example:
        >>> result = list_slice([0, 1, 2, 3, 4, 5], start=1, end=4)
        >>> result.items
        [1, 2, 3]
    """
    if step == 0:
        raise ValueError("step cannot be 0")

    # 处理负索引
    start_idx = start if start is not None else (0 if step > 0 else len(lst) - 1)
    end_idx = end if end is not None else (len(lst) if step > 0 else len(lst) - 1)

    # 边界处理
    if start_idx < 0:
        start_idx = max(0, start_idx + len(lst))
    if start_idx > len(lst):
        start_idx = len(lst)

    if end_idx < 0:
        end_idx = max(0, end_idx + len(lst))
    if end_idx > len(lst):
        end_idx = len(lst)

    result = lst[start_idx:end_idx:step]

    return SliceResult(
        items=result,
        count=len(result),
        start=start_idx,
        end=end_idx,
        step=step
    )


def list_first_n(lst: List[Any], n: int = 5) -> SliceResult:
    """获取前n个元素"""
    return list_slice(lst, start=0, end=n)


def list_last_n(lst: List[Any], n: int = 5) -> SliceResult:
    """获取后n个元素"""
    return list_slice(lst, start=-n, end=None)


def list_at_index(lst: List[Any], index: int, default: Any = None) -> Any:
    """获取指定索引的元素，支持负索引"""
    try:
        return lst[index]
    except IndexError:
        return default


if __name__ == "__main__":
    # 测试
    r1 = list_slice([0, 1, 2, 3, 4, 5], start=1, end=4)
    print(f"切片[1:4]: {r1.items}, 数量: {r1.count}")

    r2 = list_slice([0, 1, 2, 3, 4, 5], step=2)
    print(f"切片[::2]: {r2.items}, 数量: {r2.count}")

    r3 = list_first_n([1, 2, 3, 4, 5, 6, 7], n=3)
    print(f"前3个: {r3.items}, 数量: {r3.count}")

    r4 = list_last_n([1, 2, 3, 4, 5, 6, 7], n=2)
    print(f"后2个: {r4.items}, 数量: {r4.count}")
