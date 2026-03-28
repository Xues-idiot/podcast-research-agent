"""CSS颜色解析工具"""

import re
from typing import Optional, Tuple


class CssParserTool:
    _instance: Optional["CssParserTool"] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def parse(self, css_color: str) -> Optional[Tuple[int, int, int]]:
        css_color = css_color.strip().lower()

        if css_color.startswith('#'):
            return self._parse_hex(css_color)

        if css_color.startswith('rgb'):
            return self._parse_rgb(css_color)

        if css_color.startswith('hsl'):
            return self._parse_hsl(css_color)

        return self._parse_named_color(css_color)

    def _parse_hex(self, hex_color: str) -> Optional[Tuple[int, int, int]]:
        hex_color = hex_color.lstrip('#')
        if len(hex_color) == 3:
            hex_color = ''.join(c * 2 for c in hex_color)
        if len(hex_color) != 6:
            return None
        return tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4))

    def _parse_rgb(self, rgb_str: str) -> Optional[Tuple[int, int, int]]:
        match = re.search(r'rgb\s*\(\s*(\d+)\s*,\s*(\d+)\s*,\s*(\d+)\s*\)', rgb_str)
        if match:
            return int(match.group(1)), int(match.group(2)), int(match.group(3))
        return None

    def _parse_hsl(self, hsl_str: str) -> Optional[Tuple[int, int, int]]:
        match = re.search(r'hsl\s*\(\s*(\d+)\s*,\s*(\d+)%?\s*,\s*(\d+)%?\s*\)', hsl_str)
        if match:
            h, s, l = int(match.group(1)), int(match.group(2)), int(match.group(3))
            return self._hsl_to_rgb(h, s, l)
        return None

    def _hsl_to_rgb(self, h: int, s: int, l: int) -> Tuple[int, int, int]:
        s, l = s / 100, l / 100
        c = (1 - abs(2 * l - 1)) * s
        x = c * (1 - abs((h / 60) % 2 - 1))
        m = l - c / 2
        if 0 <= h < 60:
            r, g, b = c, x, 0
        elif 60 <= h < 120:
            r, g, b = x, c, 0
        elif 120 <= h < 180:
            r, g, b = 0, c, x
        elif 180 <= h < 240:
            r, g, b = 0, x, c
        elif 240 <= h < 300:
            r, g, b = x, 0, c
        else:
            r, g, b = c, 0, x
        return int((r + m) * 255), int((g + m) * 255), int((b + m) * 255)

    def _parse_named_color(self, name: str) -> Optional[Tuple[int, int, int]]:
        named_colors = {
            "red": (255, 0, 0),
            "green": (0, 128, 0),
            "blue": (0, 0, 255),
            "white": (255, 255, 255),
            "black": (0, 0, 0),
            "orange": (255, 165, 0),
            "purple": (128, 0, 128),
        }
        return named_colors.get(name.lower())


def get_css_parser_tool() -> CssParserTool:
    return CssParserTool()