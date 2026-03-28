"""视频模糊工具"""

from typing import List, Optional


class VideoBlurTool:
    _instance: Optional["VideoBlurTool"] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def blur(self, frames: List[List[List[float]]], radius: int = 3) -> List[List[List[float]]]:
        if not frames or not frames[0] or radius <= 0:
            return frames
        result = []
        for frame in frames:
            h, w = len(frame), len(frame[0]) if frame else 0
            blurred = [[0.0] * w for _ in range(h)]
            for i in range(h):
                for j in range(w):
                    count = 0
                    total = 0.0
                    for di in range(-radius, radius + 1):
                        for dj in range(-radius, radius + 1):
                            ni, nj = i + di, j + dj
                            if 0 <= ni < h and 0 <= nj < w:
                                total += frame[ni][nj]
                                count += 1
                    blurred[i][j] = total / count if count > 0 else frame[i][j]
            result.append(blurred)
        return result


def get_video_blur_tool() -> VideoBlurTool:
    return VideoBlurTool()