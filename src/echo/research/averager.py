"""平均值工具"""

from typing import Optional, List


class AveragerTool:
    """平均值工具"""

    def mean(self, numbers: List[float]) -> float:
        """计算平均值"""
        if not numbers:
            return 0.0
        return sum(numbers) / len(numbers)

    def median(self, numbers: List[float]) -> float:
        """计算中位数"""
        if not numbers:
            return 0.0
        sorted_numbers = sorted(numbers)
        n = len(sorted_numbers)
        if n % 2 == 0:
            return (sorted_numbers[n // 2 - 1] + sorted_numbers[n // 2]) / 2
        return sorted_numbers[n // 2]

    def mode(self, numbers: List[float]) -> float:
        """计算众数"""
        if not numbers:
            return 0.0
        frequency = {}
        for num in numbers:
            frequency[num] = frequency.get(num, 0) + 1
        return max(frequency, key=frequency.get)


_averager_tool: Optional[AveragerTool] = None


def get_averager_tool() -> AveragerTool:
    global _averager_tool
    if _averager_tool is None:
        _averager_tool = AveragerTool()
    return _averager_tool