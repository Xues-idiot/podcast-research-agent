"""配置管理 - 从环境变量读取配置"""

from dataclasses import dataclass
from os import getenv
from dotenv import load_dotenv

# 加载 .env 文件
load_dotenv()


@dataclass
class MiniMaxConfig:
    """MiniMax API 配置"""
    api_key: str
    base_url: str
    model: str

    @classmethod
    def from_env(cls) -> "MiniMaxConfig":
        return cls(
            api_key=getenv("MINIMAX_API_KEY", ""),
            base_url=getenv("MINIMAX_BASE_URL", "https://api.minimaxi.com/anthropic"),
            model=getenv("MINIMAX_MODEL", "MiniMax-M2.7"),
        )


@dataclass
class TavilyConfig:
    """Tavily API 配置"""
    api_key: str

    @classmethod
    def from_env(cls) -> "TavilyConfig":
        return cls(api_key=getenv("TAVILY_API_KEY", ""))


@dataclass
class Config:
    """全局配置"""
    minimax: MiniMaxConfig
    tavily: TavilyConfig

    @classmethod
    def from_env(cls) -> "Config":
        return cls(
            minimax=MiniMaxConfig.from_env(),
            tavily=TavilyConfig.from_env(),
        )


# 全局配置实例
config = Config.from_env()
