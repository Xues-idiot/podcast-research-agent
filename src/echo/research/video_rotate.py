"""视频旋转工具"""

from typing import List, Optional


class VideoRotateTool:
    _instance: Optional["VideoRotateTool"] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def rotate_90(self, frames: List[List[List[float]]], clockwise: bool = True) -> List[List[List[float]]]:
        if not frames or not frames[0]:
            return frames
        if clockwise:
            return [list(row) for row in zip(*reversed(frames))]
        return [list(row) for row in zip(*frames)]

    def rotate_180(self, frames: List[List[List[float]]]) -> List[List[List[float]]]:
        return [list(reversed(list(reversed(frame)))) for frame in reversed(frames)]

    def rotate_270(self, frames: List[List[List[float]]]) -> List[List[List[float]]]:
        return self.rotate_90(frames, clockwise=False)


def get_video_rotate_tool() -> VideoRotateTool:
    return VideoRotateTool()