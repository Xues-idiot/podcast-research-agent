"""斐波那契生成器"""

from typing import List, Optional


class FibonacciGen:
    _instance: Optional["FibonacciGen"] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def fibonacci(self, n: int) -> int:
        if n <= 0:
            return 0
        if n == 1:
            return 1
        a, b = 0, 1
        for _ in range(2, n + 1):
            a, b = b, a + b
        return b

    def fibonacci_sequence(self, count: int) -> List[int]:
        return [self.fibonacci(i) for i in range(count)]


def get_fibonacci_gen() -> FibonacciGen:
    return FibonacciGen()
