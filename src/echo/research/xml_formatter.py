"""XML格式化工具"""

import re
from typing import Optional


class XmlFormatter:
    """XML格式化工具"""

    def format(self, xml_str: str, indent: str = "  ") -> str:
        """格式化XML"""
        formatted = []
        level = 0
        parts = re.split(r'(<[^>]+>)', xml_str)

        for part in parts:
            if not part.strip():
                continue
            if part.startswith('</'):
                level = max(0, level - 1)
                formatted.append(indent * level + part)
            elif part.startswith('<') and not part.endswith('/>'):
                formatted.append(indent * level + part)
                level += 1
            else:
                formatted.append(indent * level + part)

        return '\n'.join(formatted)

    def minify(self, xml_str: str) -> str:
        """压缩XML"""
        xml_str = re.sub(r'>\s+<', '><', xml_str)
        xml_str = re.sub(r'\s+', ' ', xml_str)
        return xml_str.strip()


_formatter: Optional[XmlFormatter] = None


def get_xml_formatter() -> XmlFormatter:
    global _formatter
    if _formatter is None:
        _formatter = XmlFormatter()
    return _formatter