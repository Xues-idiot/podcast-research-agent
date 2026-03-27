"""超时工具"""

import time
import signal
from typing import Callable, Any, Optional


class Timeout:
    _instance: Optional["Timeout"] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def timeout(self, func: Callable, seconds: int = 5) -> Any:
        def handler(signum, frame):
            raise TimeoutError("Function call timed out")
        try:
            signal.signal(signal.SIGALRM, handler)
            signal.alarm(seconds)
            result = func()
            signal.alarm(0)
            return result
        except TimeoutError:
            return None


def get_timeout() -> Timeout:
    return Timeout()
