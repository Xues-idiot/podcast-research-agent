"""位运算工具 - 位级操作和处理"""
from typing import List


def bitwise_and(a: int, b: int) -> int:
    """
    位与运算

    Args:
        a: 操作数A
        b: 操作数B

    Returns:
        位与结果
    """
    return a & b


def bitwise_or(a: int, b: int) -> int:
    """
    位或运算

    Args:
        a: 操作数A
        b: 操作数B

    Returns:
        位或结果
    """
    return a | b


def bitwise_xor(a: int, b: int) -> int:
    """
    位异或运算

    Args:
        a: 操作数A
        b: 操作数B

    Returns:
        位异或结果
    """
    return a ^ b


def bitwise_not(a: int) -> int:
    """
    位非运算

    Args:
        a: 操作数

    Returns:
        位非结果
    """
    return ~a


def left_shift(a: int, bits: int) -> int:
    """
    左移运算

    Args:
        a: 操作数
        bits: 移位位数

    Returns:
        左移结果
    """
    return a << bits


def right_shift(a: int, bits: int) -> int:
    """
    右移运算

    Args:
        a: 操作数
        bits: 移位位数

    Returns:
        右移结果
    """
    return a >> bits


def count_set_bits(a: int) -> int:
    """
    统计整数中1的个数

    Args:
        a: 整数

    Returns:
        1的个数
    """
    return bin(a).count('1')


def get_bit(a: int, pos: int) -> int:
    """
    获取指定位的值

    Args:
        a: 整数
        pos: 位位置

    Returns:
        位的值(0或1)
    """
    return (a >> pos) & 1


def set_bit(a: int, pos: int) -> int:
    """
    设置指定位为1

    Args:
        a: 整数
        pos: 位位置

    Returns:
        修改后的整数
    """
    return a | (1 << pos)


def clear_bit(a: int, pos: int) -> int:
    """
    清除指定位(置0)

    Args:
        a: 整数
        pos: 位位置

    Returns:
        修改后的整数
    """
    return a & ~(1 << pos)


def toggle_bit(a: int, pos: int) -> int:
    """
    翻转指定位

    Args:
        a: 整数
        pos: 位位置

    Returns:
        修改后的整数
    """
    return a ^ (1 << pos)


def is_power_of_two(a: int) -> bool:
    """
    判断是否为2的幂

    Args:
        a: 整数

    Returns:
        是否为2的幂
    """
    return a > 0 and (a & (a - 1)) == 0


def bit_length(a: int) -> int:
    """
    获取整数需要的位数

    Args:
        a: 整数

    Returns:
        需要的位数
    """
    return a.bit_length()


if __name__ == "__main__":
    print(f"5 & 3 = {bitwise_and(5, 3)}")
    print(f"5 | 3 = {bitwise_or(5, 3)}")
    print(f"5 ^ 3 = {bitwise_xor(5, 3)}")
    print(f"~5 = {bitwise_not(5)}")
    print(f"5 << 1 = {left_shift(5, 1)}")
    print(f"5 >> 1 = {right_shift(5, 1)}")
    print(f"5中1的个数: {count_set_bits(5)}")