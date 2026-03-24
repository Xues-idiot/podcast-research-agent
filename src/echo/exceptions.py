"""Echo 异常定义"""


class EchoError(Exception):
    """Echo基础异常"""
    pass


class DownloadError(EchoError):
    """下载失败"""
    pass


class TranscriptionError(EchoError):
    """转录失败"""
    pass


class SummaryError(EchoError):
    """摘要生成失败"""
    pass


class KeyPointError(EchoError):
    """要点提取失败"""
    pass


class MindMapError(EchoError):
    """思维导图生成失败"""
    pass


class KnowledgeLinkError(EchoError):
    """知识关联失败"""
    pass


class ConfigurationError(EchoError):
    """配置错误"""
    pass


class APIError(EchoError):
    """API调用错误"""
    pass
