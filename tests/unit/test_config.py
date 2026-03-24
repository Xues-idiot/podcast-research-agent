"""配置测试"""

import pytest
from echo.config import Config, MiniMaxConfig, TavilyConfig


class TestConfig:
    """配置类测试"""

    def test_minimax_config_from_env(self):
        """测试MiniMax配置从环境变量读取"""
        config = MiniMaxConfig.from_env()
        assert config.base_url is not None
        assert config.model is not None

    def test_tavily_config_from_env(self):
        """测试Tavily配置从环境变量读取"""
        config = TavilyConfig.from_env()
        assert config.api_key is not None

    def test_full_config_from_env(self):
        """测试完整配置"""
        config = Config.from_env()
        assert config.minimax is not None
        assert config.tavily is not None
