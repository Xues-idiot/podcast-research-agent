"""视频反色工具"""

from typing import List, Optional


class VideoInvertTool:
    _instance: Optional["VideoInvertTool"] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def invert(self, frames: List[List[List[float]]]) -> List[List[List[float]]]:
        if not frames:
            return frames
        result = []
        for frame in frames:
            result.append([[[1.0 - c for c in pixel] for pixel in row] for row in frame])
        return result


def get_video_invert_tool() -> VideoInvertTool:
    return VideoInvertTool()