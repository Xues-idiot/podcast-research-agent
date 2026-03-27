"""加权工具"""

from typing import Optional, Any


class WeightTool:
    """加权工具"""

    def weight_sum(self, values: list, weights: list) -> float:
        """加权求和"""
        return sum(v * w for v, w in zip(values, weights))

    def normalize_weights(self, weights: list) -> list:
        """归一化权重"""
        total = sum(weights)
        return [w / total for w in weights] if total else weights


_tool: Optional[WeightTool] = None


def get_weight_tool() -> WeightTool:
    global _tool
    if _tool is None:
        _tool = WeightTool()
    return _tool