"""URL工具"""

from urllib.parse import urlparse, parse_qs, urlencode, urljoin
from typing import Optional


class UrlTool:
    """URL工具"""

    def parse(self, url: str) -> dict:
        """解析URL"""
        parsed = urlparse(url)
        return {
            "scheme": parsed.scheme,
            "netloc": parsed.netloc,
            "path": parsed.path,
            "params": parsed.params,
            "query": parsed.query,
            "fragment": parsed.fragment
        }

    def build(self, scheme: str = "https", netloc: str = "", path: str = "", query: dict = None, fragment: str = "") -> str:
        """构建URL"""
        query_str = urlencode(query) if query else ""
        return urlparse("")._replace(
            scheme=scheme, netloc=netloc, path=path, query=query_str, fragment=fragment
        ).geturl()

    def join(self, base: str, relative: str) -> str:
        """拼接URL"""
        return urljoin(base, relative)

    def get_query_params(self, url: str) -> dict:
        """获取查询参数"""
        return dict(parse_qs(urlparse(url).query))


_tool: Optional[UrlTool] = None


def get_url_tool() -> UrlTool:
    global _tool
    if _tool is None:
        _tool = UrlTool()
    return _tool