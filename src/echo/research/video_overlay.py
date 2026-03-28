"""视频叠加工具"""

from typing import List, Optional


class VideoOverlayTool:
    _instance: Optional["VideoOverlayTool"] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def overlay(self, base: List[List[List[float]]], overlay: List[List[List[float]]], x: int = 0, y: int = 0, alpha: float = 0.5) -> List[List[List[float]]]:
        if not base or not overlay:
            return base
        result = [row[:] for row in base]
        h = min(len(overlay), len(base) - y)
        w = min(len(overlay[0]) if overlay and overlay[0] else 0, len(base[0]) - x if base and base[0] else 0)
        for i in range(h):
            for j in range(w):
                for c in range(3):
                    base_val = result[y + i][x + j][c] if c < len(result[y + i][x + j]) else 0
                    over_val = overlay[i][j][c] if c < len(overlay[i][j]) else 0
                    result[y + i][x + j][c] = base_val * (1 - alpha) + over_val * alpha
        return result


def get_video_overlay_tool() -> VideoOverlayTool:
    return VideoOverlayTool()