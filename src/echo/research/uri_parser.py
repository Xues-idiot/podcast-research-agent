"""URI解析器工具"""

from typing import Optional
from urllib.parse import urlparse, parse_qs


class UriParser:
    _instance: Optional["UriParser"] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def parse(self, uri: str) -> Dict[str, Any]:
        parsed = urlparse(uri)
        return {
            "scheme": parsed.scheme,
            "host": parsed.hostname,
            "port": parsed.port,
            "path": parsed.path,
            "query": parse_qs(parsed.query),
            "fragment": parsed.fragment
        }

    def build(self, scheme: str, host: str, path: str = "", port: int = None) -> str:
        port_str = f":{port}" if port else ""
        return f"{scheme}://{host}{port_str}{path}"


def get_uri_parser() -> UriParser:
    return UriParser()
