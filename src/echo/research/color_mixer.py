"""颜色混合工具"""

from typing import List, Optional


class ColorMixerTool:
    _instance: Optional["ColorMixerTool"] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def mix(self, color1: str, color2: str, ratio: float = 0.5) -> str:
        c1 = self._hex_to_rgb(color1)
        c2 = self._hex_to_rgb(color2)
        r = int(c1[0] * (1 - ratio) + c2[0] * ratio)
        g = int(c1[1] * (1 - ratio) + c2[1] * ratio)
        b = int(c1[2] * (1 - ratio) + c2[2] * ratio)
        return f"#{r:02x}{g:02x}{b:02x}"

    def _hex_to_rgb(self, hex_color: str) -> tuple:
        hex_color = hex_color.lstrip('#')
        return tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4))


def get_color_mixer_tool() -> ColorMixerTool:
    return ColorMixerTool()