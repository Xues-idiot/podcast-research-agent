"""颜色工具"""

from typing import Optional, Tuple


class ColorTool:
    _instance: Optional["ColorTool"] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def hex_to_rgb(self, hex_color: str) -> Tuple[int, int, int]:
        hex_color = hex_color.lstrip("#")
        return tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4))

    def rgb_to_hex(self, r: int, g: int, b: int) -> str:
        return f"#{r:02x}{g:02x}{b:02x}"


def get_color_tool() -> ColorTool:
    return ColorTool()
