"""环状缓冲工具"""

from typing import Any, List, Optional


class RingBuf:
    _instance: Optional["RingBuf"] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def create(self, capacity: int) -> dict:
        return {"data": [None] * capacity, "head": 0, "tail": 0, "size": 0, "capacity": capacity}

    def push(self, buf: dict, item: Any) -> bool:
        if buf["size"] >= buf["capacity"]:
            return False
        buf["data"][buf["tail"]] = item
        buf["tail"] = (buf["tail"] + 1) % buf["capacity"]
        buf["size"] += 1
        return True

    def pop(self, buf: dict) -> Any:
        if buf["size"] == 0:
            return None
        item = buf["data"][buf["head"]]
        buf["head"] = (buf["head"] + 1) % buf["capacity"]
        buf["size"] -= 1
        return item


def get_ring_buf() -> RingBuf:
    return RingBuf()
