"""Echo - 播客研究Agent"""

__version__ = "0.1.0"

# 主客户端
from echo.client import EchoClient

# 数据类型
from echo.types import (
    Transcript,
    Summary,
    KeyPoint,
    KnowledgeCard,
    MindMap,
    ResearchResult,
)

# 工具
from echo.validators import URLValidator
from echo.cache import Cache, get_cache

# 异常
from echo.exceptions import (
    EchoError,
    DownloadError,
    TranscriptionError,
    SummaryError,
    KeyPointError,
    MindMapError,
    KnowledgeLinkError,
    ConfigurationError,
    APIError,
)

__all__ = [
    # 主客户端
    "EchoClient",
    # 数据类型
    "Transcript",
    "Summary",
    "KeyPoint",
    "KnowledgeCard",
    "MindMap",
    "ResearchResult",
    # 工具
    "URLValidator",
    "Cache",
    "get_cache",
    # 异常
    "EchoError",
    "DownloadError",
    "TranscriptionError",
    "SummaryError",
    "KeyPointError",
    "MindMapError",
    "KnowledgeLinkError",
    "ConfigurationError",
    "APIError",
]
