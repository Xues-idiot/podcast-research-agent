"""MIME类型工具"""

from typing import Optional


class MimeTool:
    _instance: Optional["MimeTool"] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def get_type(self, filename: str) -> str:
        import mimetypes
        mime_type, _ = mimetypes.guess_type(filename)
        return mime_type or "application/octet-stream"

    def get_extension(self, mime_type: str) -> Optional[str]:
        import mimetypes
        return mimetypes.guess_extension(mime_type)


def get_mime_tool() -> MimeTool:
    return MimeTool()
