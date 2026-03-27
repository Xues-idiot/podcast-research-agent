"""日志工具"""

import logging
from typing import Optional


class LoggingTool:
    _instance: Optional["LoggingTool"] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def get_logger(self, name: str) -> logging.Logger:
        return logging.getLogger(name)


def get_logging_tool() -> LoggingTool:
    return LoggingTool()
