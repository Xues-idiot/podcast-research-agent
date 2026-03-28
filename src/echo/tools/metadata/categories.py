"""工具分类定义"""

from typing import Dict, List

TOOL_CATEGORIES: Dict[str, Dict] = {
    "podcast_research": {
        "id": "podcast_research",
        "name": "播客研究工具",
        "name_en": "Podcast Research",
        "icon": "mic",
        "description": "播客内容处理核心工具",
        "color": "#E67E22",
        "subcategories": ["downloader", "transcriber", "summarizer", "keypoint", "mindmap", "linker", "qa"]
    },
    "text_processing": {
        "id": "text_processing",
        "name": "文本处理工具",
        "name_en": "Text Processing",
        "icon": "file-text",
        "description": "文本格式化和处理",
        "color": "#3498DB",
        "subcategories": ["format", "extract", "transform", "search", "statistics", "cleaner"]
    },
    "math": {
        "id": "math",
        "name": "数学计算工具",
        "name_en": "Math & Statistics",
        "icon": "calculator",
        "description": "数学运算和统计分析",
        "color": "#9B59B6",
        "subcategories": ["basic", "statistical", "probability", "linear_algebra", "signal_processing"]
    },
    "data_structures": {
        "id": "data_structures",
        "name": "数据结构工具",
        "name_en": "Data Structures",
        "icon": "database",
        "description": "列表、字典、集合、树、图",
        "color": "#1ABC9C",
        "subcategories": ["list", "dict", "set", "tree", "graph", "heap", "stack", "queue"]
    },
    "encoding": {
        "id": "encoding",
        "name": "编码转换工具",
        "name_en": "Encoding & Conversion",
        "icon": "refresh-cw",
        "description": "Base64、URL、HTML、UUID等编码转换",
        "color": "#E74C3C",
        "subcategories": ["base64", "url", "html", "uuid", "hex", "binary"]
    },
    "validation": {
        "id": "validation",
        "name": "验证工具",
        "name_en": "Validation",
        "icon": "check-circle",
        "description": "邮箱、电话、URL、JSON验证",
        "color": "#2ECC71",
        "subcategories": ["email", "phone", "url", "json", "credit_card", "id"]
    },
    "datetime": {
        "id": "datetime",
        "name": "日期时间工具",
        "name_en": "Date & Time",
        "icon": "calendar",
        "description": "日期格式化和计算",
        "color": "#F39C12",
        "subcategories": ["format", "calculate", "timezone", "timestamp"]
    },
    "file": {
        "id": "file",
        "name": "文件处理工具",
        "name_en": "File Processing",
        "icon": "folder",
        "description": "文件读取、写入、转换",
        "color": "#95A5A6",
        "subcategories": ["read", "write", "convert", "path"]
    },
    "developer": {
        "id": "developer",
        "name": "开发工具",
        "name_en": "Developer Tools",
        "icon": "code",
        "description": "调试、日志、性能工具",
        "color": "#34495E",
        "subcategories": ["debug", "log", "performance", "async"]
    },
    "random": {
        "id": "random",
        "name": "随机生成工具",
        "name_en": "Random & Generation",
        "icon": "shuffle",
        "description": "随机数和ID生成",
        "color": "#E91E63",
        "subcategories": ["random", "uuid", "password", "id"]
    }
}


def get_all_categories() -> List[Dict]:
    """获取所有分类列表"""
    return list(TOOL_CATEGORIES.values())


def get_category_by_id(category_id: str) -> Dict:
    """根据ID获取分类"""
    return TOOL_CATEGORIES.get(category_id, {})


def get_categories_with_tools() -> List[Dict]:
    """获取有工具的分类列表"""
    from echo.tools.metadata.tools import TOOL_REGISTRY

    result = []
    for cat_id, cat_info in TOOL_CATEGORIES.items():
        tools = [t for t in TOOL_REGISTRY.values() if t.get("category") == cat_id]
        if tools:
            result.append({
                **cat_info,
                "tool_count": len(tools)
            })
    return result
