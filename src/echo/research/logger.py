"""日志工具"""

import logging
from typing import Optional


class Logger:
    """日志工具"""

    def __init__(self, name: str = "echo"):
        self._logger = logging.getLogger(name)
        self._logger.setLevel(logging.INFO)
        if not self._logger.handlers:
            handler = logging.StreamHandler()
            handler.setFormatter(logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s'))
            self._logger.addHandler(handler)

    def info(self, message: str):
        """信息日志"""
        self._logger.info(message)

    def error(self, message: str):
        """错误日志"""
        self._logger.error(message)

    def debug(self, message: str):
        """调试日志"""
        self._logger.debug(message)


_logger: Optional[Logger] = None


def get_logger() -> Logger:
    global _logger
    if _logger is None:
        _logger = Logger()
    return _logger