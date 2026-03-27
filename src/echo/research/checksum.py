"""校验和工具"""

import hashlib
from typing import Optional


class ChecksumTool:
    """校验和工具"""

    def md5(self, data: str) -> str:
        """MD5校验和"""
        return hashlib.md5(data.encode()).hexdigest()

    def sha256(self, data: str) -> str:
        """SHA256校验和"""
        return hashlib.sha256(data.encode()).hexdigest()

    def crc32(self, data: str) -> str:
        """CRC32校验和"""
        import zlib
        return hex(zlib.crc32(data.encode()))[2:]


_tool: Optional[ChecksumTool] = None


def get_checksum_tool() -> ChecksumTool:
    global _tool
    if _tool is None:
        _tool = ChecksumTool()
    return _tool