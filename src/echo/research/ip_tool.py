"""IP地址工具"""

import re
from typing import Optional


class IpTool:
    """IP地址工具"""

    def is_valid_ipv4(self, ip: str) -> bool:
        """验证IPv4"""
        pattern = r'^(\d{1,3}\.){3}\d{1,3}$'
        if not re.match(pattern, ip):
            return False
        parts = ip.split('.')
        return all(0 <= int(p) <= 255 for p in parts)

    def is_valid_ipv6(self, ip: str) -> bool:
        """验证IPv6"""
        pattern = r'^([0-9a-fA-F]{1,4}:){7}[0-9a-fA-F]{1,4}$'
        return bool(re.match(pattern, ip))

    def ip_to_int(self, ip: str) -> int:
        """IP转整数"""
        parts = ip.split('.')
        return sum(int(p) << (8 * (3 - i)) for i, p in enumerate(parts))


_tool: Optional[IpTool] = None


def get_ip_tool() -> IpTool:
    global _tool
    if _tool is None:
        _tool = IpTool()
    return _tool