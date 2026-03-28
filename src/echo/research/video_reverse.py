"""视频反转工具"""

from typing import List, Optional


class VideoReverseTool:
    _instance: Optional["VideoReverseTool"] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def reverse(self, frames: List[List[List[float]]]) -> List[List[List[float]]]:
        if not frames:
            return frames
        return list(reversed(frames))


def get_video_reverse_tool() -> VideoReverseTool:
    return VideoReverseTool()