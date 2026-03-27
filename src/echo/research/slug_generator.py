"""Slug生成工具"""

import re
import unicodedata
from typing import Optional


class SlugGenerator:
    """Slug生成工具"""

    def generate(self, text: str, max_length: int = 50) -> str:
        """生成slug"""
        text = unicodedata.normalize('NFKD', text)
        text = re.sub(r'[^\w\s-]', '', text.lower())
        text = re.sub(r'[-\s]+', '-', text)
        text = text.strip('-')
        return text[:max_length]

    def generate_from_url(self, url: str) -> str:
        """从URL生成slug"""
        import urllib.parse
        parsed = urllib.parse.urlparse(url)
        slug = parsed.path.strip('/')
        slug = slug.replace('/', '-')
        return slug if slug else parsed.netloc


_generator: Optional[SlugGenerator] = None


def get_slug_generator() -> SlugGenerator:
    global _generator
    if _generator is None:
        _generator = SlugGenerator()
    return _generator