"""调色板生成工具"""

from typing import List, Optional


class ColorPaletteTool:
    _instance: Optional["ColorPaletteTool"] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def generate_analogous(self, hex_color: str) -> List[str]:
        r, g, b = self._hex_to_rgb(hex_color)
        h, s, l = self._rgb_to_hsl(r, g, b)
        colors = []
        for offset in [-30, -15, 0, 15, 30]:
            new_h = (h + offset / 360) % 1
            r, g, b = self._hsl_to_rgb(new_h, s, l)
            colors.append(f"#{r:02x}{g:02x}{b:02x}")
        return colors

    def generate_complementary(self, hex_color: str) -> List[str]:
        r, g, b = self._hex_to_rgb(hex_color)
        h, s, l = self._rgb_to_hsl(r, g, b)
        comp_h = (h + 0.5) % 1
        r, g, b = self._hsl_to_rgb(comp_h, s, l)
        return [hex_color, f"#{r:02x}{g:02x}{b:02x}"]

    def _hex_to_rgb(self, hex_color: str) -> tuple:
        hex_color = hex_color.lstrip('#')
        return tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4))

    def _rgb_to_hsl(self, r: int, g: int, b: int) -> tuple:
        r, g, b = r/255, g/255, b/255
        max_c = max(r, g, b)
        min_c = min(r, g, b)
        l = (max_c + min_c) / 2
        if max_c == min_c:
            return 0, 0, l
        d = max_c - min_c
        s = d / (2 - max_c - min_c) if l > 0.5 else d / (max_c + min_c)
        if max_c == r:
            h = (g - b) / d + (6 if g < b else 0)
        elif max_c == g:
            h = (b - r) / d + 2
        else:
            h = (r - g) / d + 4
        return h / 6, s, l

    def _hsl_to_rgb(self, h: float, s: float, l: float) -> tuple:
        if s == 0:
            r = g = b = l
        else:
            q = l * (1 + s) if l < 0.5 else l + s - l * s
            p = 2 * l - q
            r = self._hue_to_rgb(p, q, h + 1/3)
            g = self._hue_to_rgb(p, q, h)
            b = self._hue_to_rgb(p, q, h - 1/3)
        return int(r*255), int(g*255), int(b*255)

    def _hue_to_rgb(self, p: float, q: float, t: float) -> float:
        if t < 0: t += 1
        if t > 1: t -= 1
        if t < 1/6: return p + (q - p) * 6 * t
        if t < 1/2: return q
        if t < 2/3: return p + (q - p) * (2/3 - t) * 6
        return p


def get_color_palette_tool() -> ColorPaletteTool:
    return ColorPaletteTool()