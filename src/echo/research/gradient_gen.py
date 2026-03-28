"""渐变生成工具"""

from typing import List, Optional


class GradientGenTool:
    _instance: Optional["GradientGenTool"] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def linear_gradient(self, color1: str, color2: str, steps: int = 5) -> List[str]:
        c1 = self._hex_to_rgb(color1)
        c2 = self._hex_to_rgb(color2)
        result = []
        for i in range(steps):
            ratio = i / (steps - 1) if steps > 1 else 0
            r = int(c1[0] * (1 - ratio) + c2[0] * ratio)
            g = int(c1[1] * (1 - ratio) + c2[1] * ratio)
            b = int(c1[2] * (1 - ratio) + c2[2] * ratio)
            result.append(f"#{r:02x}{g:02x}{b:02x}")
        return result

    def _hex_to_rgb(self, hex_color: str) -> tuple:
        hex_color = hex_color.lstrip('#')
        return tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4))


def get_gradient_gen_tool() -> GradientGenTool:
    return GradientGenTool()