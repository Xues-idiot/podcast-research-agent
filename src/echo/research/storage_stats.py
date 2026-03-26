"""存储使用统计"""

import json
from pathlib import Path
from typing import Optional


class StorageStats:
    """存储使用统计"""

    def __init__(self):
        self.echo_dir = Path.home() / ".echo"

    def get_directory_size(self, path: Path) -> int:
        total = 0
        try:
            for item in path.rglob("*"):
                if item.is_file():
                    total += item.stat().st_size
        except:
            pass
        return total

    def get_all_stats(self) -> dict:
        stats = {
            "total_size_bytes": 0,
            "total_size_mb": 0,
            "directories": {},
        }

        if not self.echo_dir.exists():
            return stats

        total = 0
        for subdir in self.echo_dir.iterdir():
            if subdir.is_dir():
                size = self.get_directory_size(subdir)
                stats["directories"][subdir.name] = {
                    "size_bytes": size,
                    "size_mb": round(size / 1024 / 1024, 2),
                }
                total += size

        stats["total_size_bytes"] = total
        stats["total_size_mb"] = round(total / 1024 / 1024, 2)
        return stats

    def cleanup_old_files(self, days: int = 30) -> dict:
        """清理旧文件"""
        import time
        removed = {"files": 0, "size_bytes": 0}
        cutoff = time.time() - (days * 24 * 60 * 60)

        for path in self.echo_dir.rglob("*"):
            if path.is_file():
                try:
                    if path.stat().st_mtime < cutoff:
                        size = path.stat().st_size
                        path.unlink()
                        removed["files"] += 1
                        removed["size_bytes"] += size
                except:
                    pass

        return removed


_stats: Optional[StorageStats] = None

def get_storage_stats() -> StorageStats:
    global _stats
    if _stats is None:
        _stats = StorageStats()
    return _stats
