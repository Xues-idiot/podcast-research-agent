"""随机工具集合"""
import random
import string
import uuid
from typing import List


def random_int(min_val: int = 0, max_val: int = 100) -> int:
    return random.randint(min_val, max_val)


def random_float(min_val: float = 0.0, max_val: float = 1.0) -> float:
    return random.uniform(min_val, max_val)


def random_choice(choices: List) -> any:
    return random.choice(choices)


def random_sample(population: List, n: int = 1) -> List:
    return random.sample(population, min(n, len(population)))


def random_string(length: int = 10, charset: str = None) -> str:
    if charset is None:
        charset = string.ascii_letters + string.digits
    return ''.join(random.choice(charset) for _ in range(length))


def random_uuid() -> str:
    return str(uuid.uuid4())


def random_bool() -> bool:
    return random.choice([True, False])


def random_color() -> str:
    return '#{:06x}'.format(random.randint(0, 0xFFFFFF))


def random_date() -> str:
    from datetime import datetime, timedelta
    start = datetime(2020, 1, 1)
    delta = datetime.now() - start
    random_days = random.randint(0, delta.days)
    return (start + timedelta(days=random_days)).strftime("%Y-%m-%d")
