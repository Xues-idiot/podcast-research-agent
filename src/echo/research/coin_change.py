"""硬币找零工具"""

from typing import List, Optional


class CoinChange:
    _instance: Optional["CoinChange"] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def min_coins(self, coins: List[int], amount: int) -> int:
        dp = [float("inf")] * (amount + 1)
        dp[0] = 0
        for coin in coins:
            for i in range(coin, amount + 1):
                dp[i] = min(dp[i], dp[i - coin] + 1)
        return dp[amount] if dp[amount] != float("inf") else -1


def get_coin_change() -> CoinChange:
    return CoinChange()
