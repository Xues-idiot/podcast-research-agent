"""文本哈希工具"""

import hashlib
from typing import Optional


class TextHasher:
    """文本哈希工具"""

    def hash_md5(self, text: str) -> str:
        """MD5哈希"""
        return hashlib.md5(text.encode('utf-8')).hexdigest()

    def hash_sha256(self, text: str) -> str:
        """SHA256哈希"""
        return hashlib.sha256(text.encode('utf-8')).hexdigest()

    def hash_sha1(self, text: str) -> str:
        """SHA1哈希"""
        return hashlib.sha1(text.encode('utf-8')).hexdigest()

    def hash_sha512(self, text: str) -> str:
        """SHA512哈希"""
        return hashlib.sha512(text.encode('utf-8')).hexdigest()

    def hash_xxhash(self, text: str) -> str:
        """xxHash (快速哈希)"""
        try:
            import xxhash
            return xxhash.xxh64(text.encode('utf-8')).hexdigest()
        except ImportError:
            return self.hash_sha256(text)


_hasher: Optional[TextHasher] = None


def get_text_hasher() -> TextHasher:
    global _hasher
    if _hasher is None:
        _hasher = TextHasher()
    return _hasher