"""视频稳定工具"""

from typing import List, Optional


class VideoStabilizeTool:
    _instance: Optional["VideoStabilizeTool"] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def stabilize(self, frames: List[List[List[float]]], strength: float = 0.5) -> List[List[List[float]]]:
        if not frames:
            return frames
        offset = int(strength * 5)
        if offset == 0:
            return frames
        stabilized = []
        for i, frame in enumerate(frames):
            shift = offset // 2 if i % 2 == 0 else -offset // 2
            stabilized.append(self._shift_frame(frame, shift, shift))
        return stabilized

    def _shift_frame(self, frame: List[List[List[float]]], dx: int, dy: int) -> List[List[List[float]]]:
        h = len(frame)
        w = len(frame[0]) if frame and frame[0] else 0
        result = [[frame[max(0, min(h-1, i - dy))][max(0, min(w-1, j - dx))] for j in range(w)] for i in range(h)]
        return result


def get_video_stabilize_tool() -> VideoStabilizeTool:
    return VideoStabilizeTool()