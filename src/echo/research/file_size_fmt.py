"""文件大小格式化工具"""

from typing import Optional


class FileSizeFmtTool:
    _instance: Optional["FileSizeFmtTool"] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def format_bytes(self, bytes_val: int, precision: int = 2) -> str:
        """格式化字节大小"""
        units = ["B", "KB", "MB", "GB", "TB", "PB"]
        size = float(bytes_val)
        unit_idx = 0
        while size >= 1024 and unit_idx < len(units) - 1:
            size /= 1024
            unit_idx += 1
        return f"{size:.{precision}f} {units[unit_idx]}"

    def parse_size(self, size_str: str) -> int:
        """解析大小字符串(如"10MB")"""
        size_str = size_str.strip().upper()
        units = {"B": 1, "KB": 1024, "MB": 1024**2, "GB": 1024**3, "TB": 1024**4, "PB": 1024**5}
        for unit, multiplier in units.items():
            if size_str.endswith(unit):
                num_str = size_str[:-len(unit)].strip()
                return int(float(num_str) * multiplier)
        return int(size_str)

    def bytes_to_kb(self, bytes_val: int) -> float:
        """字节转KB"""
        return bytes_val / 1024

    def bytes_to_mb(self, bytes_val: int) -> float:
        """字节转MB"""
        return bytes_val / (1024 * 1024)

    def bytes_to_gb(self, bytes_val: int) -> float:
        """字节转GB"""
        return bytes_val / (1024 * 1024 * 1024)


_fs_instance: Optional[FileSizeFmtTool] = None


def get_file_size_fmt_tool() -> FileSizeFmtTool:
    global _fs_instance
    if _fs_instance is None:
        _fs_instance = FileSizeFmtTool()
    return _fs_instance