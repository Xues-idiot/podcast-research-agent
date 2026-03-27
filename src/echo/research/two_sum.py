"""两数之和工具"""

from typing import List, Optional, Tuple


class TwoSum:
    _instance: Optional["TwoSum"] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def solve(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for i, num in enumerate(nums):
            complement = target - num
            if complement in seen:
                return [seen[complement], i]
            seen[num] = i
        return []


def get_two_sum() -> TwoSum:
    return TwoSum()
