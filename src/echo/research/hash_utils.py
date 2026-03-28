"""哈希工具集合"""
import hashlib
from typing import Any


def md5(text: str) -> str:
    return hashlib.md5(text.encode()).hexdigest()


def sha1(text: str) -> str:
    return hashlib.sha1(text.encode()).hexdigest()


def sha256(text: str) -> str:
    return hashlib.sha256(text.encode()).hexdigest()


def sha512(text: str) -> str:
    return hashlib.sha512(text.encode()).hexdigest()


def crc32(text: str) -> str:
    import zlib
    return hex(zlib.crc32(text.encode()))


def hash_any(obj: Any) -> str:
    import json
    s = json.dumps(obj, sort_keys=True)
    return hashlib.md5(s.encode()).hexdigest()


def verify_hash(text: str, hash_value: str, algo: str = "md5") -> bool:
    algorithms = {
        "md5": md5,
        "sha1": sha1,
        "sha256": sha256,
        "sha512": sha512
    }
    algo_fn = algorithms.get(algo, md5)
    return algo_fn(text) == hash_value
