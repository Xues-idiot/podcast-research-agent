"""列表统计工具 - 对列表进行统计分析"""
from typing import Any, List, Optional
from dataclasses import dataclass
import statistics


@dataclass
class StatsResult:
    count: int
    sum: float
    mean: Optional[float]
    median: Optional[float]
    min: Optional[Any]
    max: Optional[Any]


def list_stats(lst: List[Any]) -> StatsResult:
    """
    计算列表的统计信息

    Args:
        lst: 源列表（应为数值类型）

    Returns:
        StatsResult: 统计结果
    """
    if not lst:
        return StatsResult(count=0, sum=0, mean=None, median=None, min=None, max=None)

    numeric_vals = [x for x in lst if isinstance(x, (int, float))]
    if not numeric_vals:
        return StatsResult(count=len(lst), sum=0, mean=None, median=None, min=None, max=None)

    try:
        mean_val = statistics.mean(numeric_vals)
        median_val = statistics.median(numeric_vals)
    except:
        mean_val = None
        median_val = None

    return StatsResult(
        count=len(lst),
        sum=sum(numeric_vals),
        mean=mean_val,
        median=median_val,
        min=min(numeric_vals),
        max=max(numeric_vals)
    )


def list_sum(lst: List[Any]) -> float:
    """计算数值列表的和"""
    return sum(x for x in lst if isinstance(x, (int, float)))


def list_mean(lst: List[Any]) -> Optional[float]:
    """计算平均值"""
    numeric = [x for x in lst if isinstance(x, (int, float))]
    return statistics.mean(numeric) if numeric else None


def list_max(lst: List[Any]) -> Optional[Any]:
    """返回最大值"""
    return max(lst) if lst else None


def list_min(lst: List[Any]) -> Optional[Any]:
    """返回最小值"""
    return min(lst) if lst else None

