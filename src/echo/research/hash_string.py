"""字符串哈希工具"""

from typing import Optional
import hashlib


class HashStringTool:
    _instance: Optional["HashStringTool"] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def md5(self, text: str) -> str:
        """MD5哈希"""
        return hashlib.md5(text.encode()).hexdigest()

    def sha1(self, text: str) -> str:
        """SHA1哈希"""
        return hashlib.sha1(text.encode()).hexdigest()

    def sha256(self, text: str) -> str:
        """SHA256哈希"""
        return hashlib.sha256(text.encode()).hexdigest()

    def sha512(self, text: str) -> str:
        """SHA512哈希"""
        return hashlib.sha512(text.encode()).hexdigest()

    def crc32(self, text: str) -> str:
        """CRC32校验"""
        import zlib
        return hex(zlib.crc32(text.encode()) & 0xffffffff)[2:]

    def murmurhash(self, text: str, seed: int = 0) -> int:
        """MurmurHash3简化版"""
        import struct
        data = text.encode()
        c1 = 0xcc9e2d51
        c2 = 0x1b873593
        h1 = seed
        length = len(data)
        rounded_end = (length // 4) * 4
        for i in range(0, rounded_end, 4):
            k1 = struct.unpack("<I", data[i:i+4])[0]
            k1 = (k1 * c1) & 0xFFFFFFFF
            k1 = ((k1 << 15) | (k1 >> 17)) & 0xFFFFFFFF
            k1 = (k1 * c2) & 0xFFFFFFFF
            h1 ^= k1
            h1 = ((h1 << 13) | (h1 >> 19)) & 0xFFFFFFFF
            h1 = ((h1 * 5) + 0xe6546b64) & 0xFFFFFFFF
        k1 = 0
        tail = length & 3
        if tail >= 3:
            k1 ^= data[rounded_end + 2] << 16
        if tail >= 2:
            k1 ^= data[rounded_end + 1] << 8
        if tail >= 1:
            k1 ^= data[rounded_end]
            k1 = (k1 * c1) & 0xFFFFFFFF
            k1 = ((k1 << 15) | (k1 >> 17)) & 0xFFFFFFFF
            k1 = (k1 * c2) & 0xFFFFFFFF
            h1 ^= k1
        h1 ^= length
        h1 ^= (h1 >> 16)
        h1 = (h1 * 0x85ebca6b) & 0xFFFFFFFF
        h1 ^= (h1 >> 13)
        h1 = (h1 * 0xc2b2ae35) & 0xFFFFFFFF
        h1 ^= (h1 >> 16)
        return h1


_hash_instance: Optional[HashStringTool] = None


def get_hash_string_tool() -> HashStringTool:
    global _hash_instance
    if _hash_instance is None:
        _hash_instance = HashStringTool()
    return _hash_instance