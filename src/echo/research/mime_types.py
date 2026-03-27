"""MIME类型工具"""

from typing import Optional


class MimeTypesTool:
    """MIME类型工具"""

    EXT_TO_MIME = {
        "txt": "text/plain",
        "html": "text/html",
        "css": "text/css",
        "js": "application/javascript",
        "json": "application/json",
        "xml": "application/xml",
        "pdf": "application/pdf",
        "zip": "application/zip",
        "png": "image/png",
        "jpg": "image/jpeg",
        "jpeg": "image/jpeg",
        "gif": "image/gif",
        "svg": "image/svg+xml",
        "mp3": "audio/mpeg",
        "mp4": "video/mp4",
        "csv": "text/csv",
        "md": "text/markdown",
    }

    def get_mime_type(self, filename: str) -> str:
        """获取MIME类型"""
        ext = filename.rsplit('.', 1)[-1].lower() if '.' in filename else ''
        return self.EXT_TO_MIME.get(ext, "application/octet-stream")

    def get_extension(self, mime_type: str) -> str:
        """获取扩展名"""
        for ext, mt in self.EXT_TO_MIME.items():
            if mt == mime_type:
                return ext
        return ""


_tool: Optional[MimeTypesTool] = None


def get_mime_types_tool() -> MimeTypesTool:
    global _tool
    if _tool is None:
        _tool = MimeTypesTool()
    return _tool