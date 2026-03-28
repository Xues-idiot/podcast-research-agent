"""视频翻转工具"""

from typing import List, Optional


class VideoFlipTool:
    _instance: Optional["VideoFlipTool"] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def flip_horizontal(self, frames: List[List[List[float]]]) -> List[List[List[float]]]:
        return [list(reversed(frame)) for frame in frames]

    def flip_vertical(self, frames: List[List[List[float]]]) -> List[List[List[float]]]:
        return list(reversed(frames))


def get_video_flip_tool() -> VideoFlipTool:
    return VideoFlipTool()