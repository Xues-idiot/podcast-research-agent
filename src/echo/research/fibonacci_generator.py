"""斐波那契生成器"""

from typing import List, Optional


class FibonacciGenerator:
    _instance: Optional["FibonacciGenerator"] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def fibonacci(self, n: int) -> Optional[int]:
        if n < 0:
            return None
        if n == 0:
            return 0
        if n == 1:
            return 1
        a, b = 0, 1
        for _ in range(2, n + 1):
            a, b = b, a + b
        return b

    def fibonacci_sequence(self, length: int) -> List[int]:
        if length <= 0:
            return []
        sequence = [0, 1] if length > 1 else [0]
        while len(sequence) < length:
            sequence.append(sequence[-1] + sequence[-2])
        return sequence[:length]


def get_fibonacci_generator() -> FibonacciGenerator:
    return FibonacciGenerator()
