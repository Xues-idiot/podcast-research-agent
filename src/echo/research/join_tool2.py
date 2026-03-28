"""连接工具v2"""

from typing import List, Optional


class JoinTool2:
    _instance: Optional["JoinTool2"] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def join(self, *signals: List[float]) -> List[float]:
        result = []
        for s in signals:
            result.extend(s)
        return result


def get_join_tool2() -> JoinTool2:
    return JoinTool2()
