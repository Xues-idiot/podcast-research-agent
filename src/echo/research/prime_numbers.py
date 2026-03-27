"""质数工具"""

from typing import Optional


class PrimeTool:
    """质数工具"""

    def is_prime(self, n: int) -> bool:
        """判断质数"""
        if n < 2:
            return False
        if n == 2:
            return True
        if n % 2 == 0:
            return False
        for i in range(3, int(n**0.5) + 1, 2):
            if n % i == 0:
                return False
        return True

    def primes_up_to(self, n: int) -> list[int]:
        """获取n以内的所有质数"""
        sieve = [True] * (n + 1)
        sieve[0] = sieve[1] = False
        for i in range(2, int(n**0.5) + 1):
            if sieve[i]:
                for j in range(i*i, n + 1, i):
                    sieve[j] = False
        return [i for i in range(n + 1) if sieve[i]]


_tool: Optional[PrimeTool] = None


def get_prime_tool() -> PrimeTool:
    global _tool
    if _tool is None:
        _tool = PrimeTool()
    return _tool