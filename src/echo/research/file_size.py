"""文件大小工具"""

from typing import Optional


class FileSizeTool:
    """文件大小工具"""

    def bytes_to_human(self, bytes_count: int) -> str:
        """字节转人类可读"""
        for unit in ['B', 'KB', 'MB', 'GB', 'TB', 'PB']:
            if bytes_count < 1024:
                return f"{bytes_count:.2f} {unit}"
            bytes_count /= 1024
        return f"{bytes_count:.2f} EB"

    def human_to_bytes(self, size_str: str) -> int:
        """人类可读转字节"""
        units = {'B': 1, 'KB': 1024, 'MB': 1024**2, 'GB': 1024**3, 'TB': 1024**4}
        size_str = size_str.strip().upper()
        for unit, multiplier in units.items():
            if size_str.endswith(unit):
                num = float(size_str[:-len(unit)].strip())
                return int(num * multiplier)
        return int(size_str)


_tool: Optional[FileSizeTool] = None


def get_file_size_tool() -> FileSizeTool:
    global _tool
    if _tool is None:
        _tool = FileSizeTool()
    return _tool