"""视频裁剪工具"""

from typing import List, Optional, Tuple


class VideoCropTool:
    _instance: Optional["VideoCropTool"] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def crop(self, frames: List[List[List[float]]], x: int, y: int, width: int, height: int) -> List[List[List[float]]]:
        if not frames:
            return frames
        return [[[frame[y + i][x + j] for j in range(min(width, len(frame[0]) - x))] for i in range(min(height, len(frame) - y))] for frame in frames]


def get_video_crop_tool() -> VideoCropTool:
    return VideoCropTool()