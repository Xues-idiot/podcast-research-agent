"""HTML解析工具"""

import re
from typing import Optional


class HtmlParser:
    """HTML解析工具"""

    def extract_text(self, html: str) -> str:
        """提取纯文本"""
        text = re.sub(r'<script[^>]*>.*?</script>', '', html, flags=re.DOTALL)
        text = re.sub(r'<style[^>]*>.*?</style>', '', text, flags=re.DOTALL)
        text = re.sub(r'<[^>]+>', '', text)
        text = re.sub(r'\s+', ' ', text)
        return text.strip()

    def extract_links(self, html: str) -> list[dict]:
        """提取链接"""
        pattern = r'<a[^>]+href=["\']([^"\']+)["\'][^>]*>([^<]*)</a>'
        matches = re.findall(pattern, html)
        return [{"url": url, "text": text.strip()} for url, text in matches]

    def extract_images(self, html: str) -> list[str]:
        """提取图片"""
        pattern = r'<img[^>]+src=["\']([^"\']+)["\']'
        return re.findall(pattern, html)

    def strip_tags(self, html: str) -> str:
        """移除所有HTML标签"""
        return re.sub(r'<[^>]+>', '', html)


_parser: Optional[HtmlParser] = None


def get_html_parser() -> HtmlParser:
    global _parser
    if _parser is None:
        _parser = HtmlParser()
    return _parser