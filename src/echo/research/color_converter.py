"""颜色转换工具"""

import re
from typing import Optional


class ColorConverter:
    """颜色转换工具"""

    def hex_to_rgb(self, hex_color: str) -> dict:
        """HEX转RGB"""
        hex_color = hex_color.lstrip('#')
        if len(hex_color) == 3:
            hex_color = hex_color * 2
        return {
            "r": int(hex_color[0:2], 16),
            "g": int(hex_color[2:4], 16),
            "b": int(hex_color[4:6], 16)
        }

    def rgb_to_hex(self, r: int, g: int, b: int) -> str:
        """RGB转HEX"""
        return f"#{r:02x}{g:02x}{b:02x}"

    def rgb_to_hsl(self, r: int, g: int, b: int) -> dict:
        """RGB转HSL"""
        r, g, b = r/255, g/255, b/255
        max_c = max(r, g, b)
        min_c = min(r, g, b)
        l = (max_c + min_c) / 2

        if max_c == min_c:
            h = s = 0
        else:
            d = max_c - min_c
            s = d / (2 - max_c - min_c) if l > 0.5 else d / (max_c + min_c)
            if max_c == r:
                h = (g - b) / d + (6 if g < b else 0)
            elif max_c == g:
                h = (b - r) / d + 2
            else:
                h = (r - g) / d + 4
            h /= 6

        return {"h": round(h * 360), "s": round(s * 100), "l": round(l * 100)}


_converter: Optional[ColorConverter] = None


def get_color_converter() -> ColorConverter:
    global _converter
    if _converter is None:
        _converter = ColorConverter()
    return _converter