"""MIME类型检测工具"""

from typing import Optional
import mimetypes


class MimeTypeDetectTool:
    _instance: Optional["MimeTypeDetectTool"] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def from_extension(self, filename: str) -> str:
        """从文件扩展名获取MIME类型"""
        mime, _ = mimetypes.guess_type(filename)
        return mime or "application/octet-stream"

    def from_filename(self, filename: str) -> str:
        """从完整文件名获取"""
        return self.from_extension(filename)

    def extension_from_mime(self, mime_type: str) -> str:
        """从MIME类型获取扩展名"""
        ext = mimetypes.guess_extension(mime_type)
        return ext or ""

    def is_text(self, filename: str) -> bool:
        """判断是否为文本文件"""
        mime = self.from_extension(filename)
        return mime.startswith("text/") or mime in ("application/json", "application/xml", "application/javascript")

    def is_image(self, filename: str) -> bool:
        """判断是否为图片"""
        mime = self.from_extension(filename)
        return mime.startswith("image/")

    def is_audio(self, filename: str) -> bool:
        """判断是否为音频"""
        mime = self.from_extension(filename)
        return mime.startswith("audio/")

    def is_video(self, filename: str) -> bool:
        """判断是否为视频"""
        mime = self.from_extension(filename)
        return mime.startswith("video/")


_mime_instance: Optional[MimeTypeDetectTool] = None


def get_mime_type_detect_tool() -> MimeTypeDetectTool:
    global _mime_instance
    if _mime_instance is None:
        _mime_instance = MimeTypeDetectTool()
    return _mime_instance