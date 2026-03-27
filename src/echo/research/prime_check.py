"""质数检查器"""

from typing import Optional


class PrimeCheck:
    _instance: Optional["PrimeCheck"] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def is_prime(self, n: int) -> bool:
        if n < 2:
            return False
        if n == 2:
            return True
        if n % 2 == 0:
            return False
        for i in range(3, int(n ** 0.5) + 1, 2):
            if n % i == 0:
                return False
        return True


def get_prime_check() -> PrimeCheck:
    return PrimeCheck()
