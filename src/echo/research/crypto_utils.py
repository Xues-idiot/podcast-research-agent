"""加密工具集合"""
import secrets
import string


def generate_token(length: int = 32) -> str:
    return secrets.token_urlsafe(length)


def generate_random_hex(length: int = 32) -> str:
    return secrets.token_hex(length)


def generate_random_bytes(length: int = 32) -> bytes:
    return secrets.token_bytes(length)


def generate_password(length: int = 16, chars: str = None) -> str:
    if chars is None:
        chars = string.ascii_letters + string.digits + string.punctuation
    return ''.join(secrets.choice(chars) for _ in range(length))


def secure_random_int(min_val: int = 0, max_val: int = 100) -> int:
    return secrets.randbelow(max_val - min_val + 1) + min_val


def generate_uuid() -> str:
    return str(secrets.uuid4())


def constant_time_compare(a: str, b: str) -> bool:
    return secrets.compare_digest(a, b)


def salt() -> str:
    return secrets.token_hex(16)
