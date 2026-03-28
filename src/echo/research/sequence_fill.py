"""序列填充工具"""

from typing import List, Any, Optional


class SequenceFillTool:
    _instance: Optional["SequenceFillTool"] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def fill_forward(self, items: List[Any], fill_value: Any = None) -> List[Any]:
        """向前填充None值"""
        result = []
        last_valid = fill_value
        for item in items:
            if item is None:
                result.append(last_valid)
            else:
                result.append(item)
                last_valid = item
        return result

    def fill_backward(self, items: List[Any], fill_value: Any = None) -> List[Any]:
        """向后填充None值"""
        result = [None] * len(items)
        next_valid = fill_value
        for i in range(len(items) - 1, -1, -1):
            if items[i] is not None:
                next_valid = items[i]
            else:
                result[i] = next_valid
        return result

    def fill_linear(self, items: List[Any]) -> List[Any]:
        """线性插值填充"""
        result = []
        start_idx = None
        end_idx = None

        for i, item in enumerate(items):
            if item is not None:
                if start_idx is None:
                    start_idx = i
                end_idx = i

        if start_idx is None:
            return items

        for i in range(len(items)):
            if items[i] is not None:
                result.append(items[i])
            else:
                if i < start_idx:
                    result.append(items[start_idx])
                elif i > end_idx:
                    result.append(items[end_idx])
                else:
                    start_val = items[start_idx]
                    end_val = items[end_idx]
                    if end_idx == start_idx:
                        result.append(start_val)
                    else:
                        ratio = (i - start_idx) / (end_idx - start_idx)
                        filled = start_val + ratio * (end_val - start_val)
                        result.append(filled)
        return result


def get_sequence_fill_tool() -> SequenceFillTool:
    return SequenceFillTool()