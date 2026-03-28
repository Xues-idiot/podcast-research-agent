"""颜色变亮工具"""

from typing import Optional


class ColorLightenTool:
    _instance: Optional["ColorLightenTool"] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def lighten(self, hex_color: str, amount: float = 0.2) -> str:
        r, g, b = self._hex_to_rgb(hex_color)
        r = min(255, int(r + (255 - r) * amount))
        g = min(255, int(g + (255 - g) * amount))
        b = min(255, int(b + (255 - b) * amount))
        return f"#{r:02x}{g:02x}{b:02x}"

    def darken(self, hex_color: str, amount: float = 0.2) -> str:
        r, g, b = self._hex_to_rgb(hex_color)
        r = max(0, int(r * (1 - amount)))
        g = max(0, int(g * (1 - amount)))
        b = max(0, int(b * (1 - amount)))
        return f"#{r:02x}{g:02x}{b:02x}"

    def _hex_to_rgb(self, hex_color: str) -> tuple:
        hex_color = hex_color.lstrip('#')
        return tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4))


def get_color_lighten_tool() -> ColorLightenTool:
    return ColorLightenTool()