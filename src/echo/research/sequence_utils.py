"""序列工具 - 序列生成和操作"""
import secrets
import string
from typing import List, Any, Iterator


def generate_arithmetic_sequence(start: float, step: float, length: int) -> List[float]:
    """
    生成等差数列

    Args:
        start: 起始值
        step: 步长
        length: 数量

    Returns:
        等差数列
    """
    return [start + i * step for i in range(length)]


def generate_geometric_sequence(start: float, ratio: float, length: int) -> List[float]:
    """
    生成等比数列

    Args:
        start: 起始值
        ratio: 公比
        length: 数量

    Returns:
        等比数列
    """
    return [start * (ratio ** i) for i in range(length)]


def generate_fibonacci_sequence(length: int) -> List[int]:
    """
    生成斐波那契数列

    Args:
        length: 数量

    Returns:
        斐波那契数列
    """
    if length <= 0:
        return []
    if length == 1:
        return [0]
    seq = [0, 1]
    for i in range(2, length):
        seq.append(seq[-1] + seq[-2])
    return seq


def generate_prime_sequence(length: int) -> List[int]:
    """
    生成素数序列

    Args:
        length: 数量

    Returns:
        素数列表
    """
    primes = []
    n = 2
    while len(primes) < length:
        is_prime = True
        for p in primes:
            if p * p > n:
                break
            if n % p == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(n)
        n += 1
    return primes


def sequence_slice(seq: List[Any], start: int = 0, end: int = None, step: int = 1) -> List[Any]:
    """
    序列切片

    Args:
        seq: 源序列
        start: 起始索引
        end: 结束索引
        step: 步长

    Returns:
        切片后的序列
    """
    return list(seq[start:end:step])


def sequence_index(seq: List[Any], value: Any, start: int = 0) -> int:
    """
    序列中查找值的索引

    Args:
        seq: 源序列
        value: 要查找的值
        start: 起始位置

    Returns:
        索引值，未找到返回-1
    """
    try:
        return seq.index(value, start)
    except ValueError:
        return -1


def sequence_count(seq: List[Any], value: Any) -> int:
    """
    统计值在序列中出现的次数

    Args:
        seq: 源序列
        value: 要统计的值

    Returns:
        出现次数
    """
    return seq.count(value)


def sequence_reverse(seq: List[Any]) -> List[Any]:
    """
    反转序列

    Args:
        seq: 源序列

    Returns:
        反转后的序列
    """
    return list(reversed(seq))


def sequence_find_all(seq: List[Any], value: Any) -> List[int]:
    """
    查找值在序列中的所有位置

    Args:
        seq: 源序列
        value: 要查找的值

    Returns:
        所有位置的列表
    """
    return [i for i, x in enumerate(seq) if x == value]


if __name__ == "__main__":
    print(f"等差数列: {generate_arithmetic_sequence(1, 2, 10)}")
    print(f"等比数列: {generate_geometric_sequence(1, 2, 10)}")
    print(f"斐波那契: {generate_fibonacci_sequence(15)}")
    print(f"素数序列: {generate_prime_sequence(20)}")