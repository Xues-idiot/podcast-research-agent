"""日志工具"""

from typing import Optional


class LoggerTool:
    """日志工具"""

    def log(self, message: str, level: str = "INFO") -> None:
        """记录日志"""
        print(f"[{level}] {message}")


_logger_tool: Optional[LoggerTool] = None


def get_logger_tool() -> LoggerTool:
    global _logger_tool
    if _logger_tool is None:
        _logger_tool = LoggerTool()
    return _logger_tool