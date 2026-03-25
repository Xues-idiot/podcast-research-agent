"""API 模块 - REST API"""

from echo.api.research import router as research_router
from echo.api.research_api import router as webresearch_router
from echo.api.chat import router as chat_router
from echo.api.knowledge import router as knowledge_router
from echo.api.sources import router as sources_router
from echo.api.navigation import router as navigation_router
from echo.api.export import router as export_router
from echo.api.memory import router as memory_router

__all__ = [
    "research_router",
    "webresearch_router",
    "chat_router",
    "knowledge_router",
    "sources_router",
    "navigation_router",
    "export_router",
    "memory_router",
]
