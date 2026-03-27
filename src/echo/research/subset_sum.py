"""子集和问题工具"""

from typing import List, Optional


class SubsetSum:
    _instance: Optional["SubsetSum"] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def can_partition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2 != 0:
            return False
        target = total // 2
        dp = [False] * (target + 1)
        dp[0] = True
        for num in nums:
            for i in range(target, num - 1, -1):
                dp[i] = dp[i] or dp[i - num]
        return dp[target]


def get_subset_sum() -> SubsetSum:
    return SubsetSum()
