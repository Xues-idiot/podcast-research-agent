"""背包问题工具"""

from typing import Any, List, Optional, Tuple


class Knapsack:
    _instance: Optional["Knapsack"] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def solve_0_1(self, weights: List[int], values: List[int], capacity: int) -> int:
        n = len(weights)
        dp = [[0] * (capacity + 1) for _ in range(n + 1)]
        for i in range(1, n + 1):
            for w in range(capacity + 1):
                if weights[i-1] <= w:
                    dp[i][w] = max(dp[i-1][w], dp[i-1][w-weights[i-1]] + values[i-1])
                else:
                    dp[i][w] = dp[i-1][w]
        return dp[n][capacity]

    def solve_unbounded(self, weights: List[int], values: List[int], capacity: int) -> int:
        dp = [0] * (capacity + 1)
        for w in range(capacity + 1):
            for i in range(len(weights)):
                if weights[i] <= w:
                    dp[w] = max(dp[w], dp[w - weights[i]] + values[i])
        return dp[capacity]


def get_knapsack() -> Knapsack:
    return Knapsack()
