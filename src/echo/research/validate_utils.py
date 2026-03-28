"""验证工具 - 数据验证和检查"""
import re
from typing import Any, List, Optional


def is_valid_email(email: str) -> bool:
    """
    验证邮箱格式

    Args:
        email: 邮箱地址

    Returns:
        是否有效
    """
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return bool(re.match(pattern, email))


def is_valid_url(url: str) -> bool:
    """
    验证URL格式

    Args:
        url: URL地址

    Returns:
        是否有效
    """
    pattern = r'^https?://[^\s/$.?#].[^\s]*$'
    return bool(re.match(pattern, url))


def is_valid_phone(phone: str, country: str = "CN") -> bool:
    """
    验证电话号码格式

    Args:
        phone: 电话号码
        country: 国家代码

    Returns:
        是否有效
    """
    if country == "CN":
        pattern = r'^1[3-9]\d{9}$'
    elif country == "US":
        pattern = r'^\d{10}$'
    else:
        return True
    return bool(re.match(pattern, phone))


def is_valid_ip(ip: str, version: int = 4) -> bool:
    """
    验证IP地址格式

    Args:
        ip: IP地址
        version: IP版本(4或6)

    Returns:
        是否有效
    """
    if version == 4:
        pattern = r'^(\d{1,3}\.){3}\d{1,3}$'
        if not re.match(pattern, ip):
            return False
        parts = ip.split('.')
        return all(0 <= int(p) <= 255 for p in parts)
    else:
        pattern = r'^([0-9a-fA-F]{1,4}:){7}[0-9a-fA-F]{1,4}$'
        return bool(re.match(pattern, ip))


def is_valid_cidr(cidr: str) -> bool:
    """
    验证CIDR格式

    Args:
        cidr: CIDR表示法

    Returns:
        是否有效
    """
    pattern = r'^(\d{1,3}\.){3}\d{1,3}/\d{1,2}$'
    if not re.match(pattern, cidr):
        return False
    ip, mask = cidr.split('/')
    parts = ip.split('.')
    if not all(0 <= int(p) <= 255 for p in parts):
        return False
    mask_int = int(mask)
    return 0 <= mask_int <= 32


def is_valid_hex_color(color: str) -> bool:
    """
    验证十六进制颜色

    Args:
        color: 颜色值

    Returns:
        是否有效
    """
    pattern = r'^#?([0-9A-Fa-f]{3}|[0-9A-Fa-f]{6})$'
    return bool(re.match(pattern, color))


def is_valid_credit_card(card: str) -> bool:
    """
    验证信用卡号(Luhn算法)

    Args:
        card: 卡号

    Returns:
        是否有效
    """
    digits = [int(c) for c in card if c.isdigit()]
    if len(digits) < 13 or len(digits) > 19:
        return False
    checksum = 0
    for i, d in enumerate(reversed(digits)):
        if i % 2 == 1:
            d *= 2
            if d > 9:
                d -= 9
        checksum += d
    return checksum % 10 == 0


def is_valid_uuid(uuid: str) -> bool:
    """
    验证UUID格式

    Args:
        uuid: UUID字符串

    Returns:
        是否有效
    """
    pattern = r'^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$'
    return bool(re.match(pattern, uuid.lower()))


def is_valid_json(text: str) -> bool:
    """
    验证JSON格式

    Args:
        text: JSON文本

    Returns:
        是否有效
    """
    import json
    try:
        json.loads(text)
        return True
    except (ValueError, TypeError):
        return False


def validate_range(value: float, min_val: float, max_val: float) -> bool:
    """
    验证值是否在范围内

    Args:
        value: 值
        min_val: 最小值
        max_val: 最大值

    Returns:
        是否在范围内
    """
    return min_val <= value <= max_val


def validate_length(text: str, min_len: int = 0, max_len: int = None) -> bool:
    """
    验证字符串长度

    Args:
        text: 字符串
        min_len: 最小长度
        max_len: 最大长度

    Returns:
        是否有效
    """
    length = len(text)
    if length < min_len:
        return False
    if max_len is not None and length > max_len:
        return False
    return True


if __name__ == "__main__":
    print(f"email: {is_valid_email('test@example.com')}")
    print(f"url: {is_valid_url('https://example.com')}")
    print(f"phone: {is_valid_phone('13812345678')}")
    print(f"ip: {is_valid_ip('192.168.1.1')}")
    print(f"credit card: {is_valid_credit_card('4532015112830366')}")