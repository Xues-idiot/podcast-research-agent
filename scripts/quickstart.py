#!/usr/bin/env python3
"""快速测试脚本 - 测试基本功能"""

import asyncio
import sys
from pathlib import Path

# 添加项目根目录到路径
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

from echo.config import config


async def test_config():
    """测试配置加载"""
    print("Testing config...")
    print(f"  MiniMax API configured: {bool(config.minimax.api_key)}")
    print(f"  MiniMax Base URL: {config.minimax.base_url}")
    print(f"  MiniMax Model: {config.minimax.model}")
    print(f"  Tavily API configured: {bool(config.tavily.api_key)}")
    return True


async def test_imports():
    """测试模块导入"""
    print("\nTesting imports...")

    try:
        from echo import EchoClient
        print("  ✅ EchoClient imported")

        from echo.agents import (
            Transcriber,
            Summarizer,
            KeyPointGenerator,
            KnowledgeLinker,
            MindMapGenerator,
        )
        print("  ✅ All agents imported")

        from echo.tools import (
            VideoDownloader,
            BilibiliDownloader,
            YouTubeDownloader,
            PodcastRSSParser,
        )
        print("  ✅ All tools imported")

        from echo.graph import ResearchGraph
        print("  ✅ ResearchGraph imported")

        return True

    except ImportError as e:
        print(f"  ❌ Import error: {e}")
        return False


def main():
    """主函数"""
    print("=" * 50)
    print("Echo - Quick Test")
    print("=" * 50)

    async def run():
        config_ok = await test_config()
        imports_ok = await test_imports()

        print("\n" + "=" * 50)
        if config_ok and imports_ok:
            print("✅ All tests passed!")
            return 0
        else:
            print("❌ Some tests failed")
            return 1

    return asyncio.run(run())


if __name__ == "__main__":
    sys.exit(main())
