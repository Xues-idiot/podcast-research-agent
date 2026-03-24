#!/usr/bin/env python3
"""端到端测试脚本 - 验证 Echo 完整研究流程"""

import asyncio
import sys
from pathlib import Path

# 添加项目根目录到路径
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

from echo import EchoClient
from echo.config import config


async def test_research_flow():
    """测试完整的研究流程"""
    print("=" * 60)
    print("Echo 端到端测试")
    print("=" * 60)
    print()

    # 检查配置
    print("1. 检查配置...")
    if not config.minimax_api_key:
        print("   [SKIP] MINIMAX_API_KEY 未设置，跳过实际测试")
        print("   提示: 请在 .env 文件中设置 MINIMAX_API_KEY")
        return False

    if not config.tavily_api_key:
        print("   [WARN] TAVILY_API_KEY 未设置，知识关联功能将被跳过")

    print(f"   [OK] MiniMax API Key: {config.minimax_api_key[:10]}...")
    print(f"   [OK] Tavily API Key: {'已设置' if config.tavily_api_key else '未设置'}")
    print()

    # 测试 URL
    test_url = "https://b23.tv/BV1xx411c7mu"  # 示例 B站视频

    print(f"2. 开始研究流程测试...")
    print(f"   URL: {test_url}")
    print()

    try:
        async with EchoClient() as client:
            print("3. 执行研究流程...")
            print("-" * 60)

            # 模拟进度显示
            steps = [
                ("download", "下载音视频"),
                ("transcribe", "转录中"),
                ("summarize", "生成摘要"),
                ("keypoint", "提取要点"),
                ("mindmap", "生成思维导图"),
                ("link", "关联知识"),
                ("report", "生成报告"),
                ("qa", "生成问答"),
            ]

            for i, (step_key, step_name) in enumerate(steps, 1):
                print(f"   [{'=' * 30}] {(i-1) * 100 // 8:3d}% | {step_name}")
                await asyncio.sleep(0.1)  # 模拟处理时间

            print("-" * 60)
            print("   正在调用 MiniMax API...")

            # 执行研究
            result = await client.research(test_url, num_keypoints=3)

            print()
            print("4. 研究结果:")
            print("-" * 60)

            # 摘要
            if "summary" in result:
                summary = result["summary"]
                print(f"   标题: {summary.get('title', 'N/A')}")
                print(f"   摘要: {summary.get('summary', 'N/A')[:200]}...")
                print()

            # 要点
            if "keypoints" in result:
                kps = result["keypoints"]
                print(f"   要点数量: {len(kps)}")
                for i, kp in enumerate(kps[:3], 1):
                    print(f"   {i}. {kp.get('content', 'N/A')[:80]}...")
                print()

            # 思维导图
            if "mindmap" in result:
                mm = result["mindmap"]
                print(f"   思维导图根节点: {mm.get('root', 'N/A')}")
                print()

            # 报告
            if "report" in result:
                report = result["report"]
                print(f"   报告标题: {report.get('title', 'N/A')}")
                print()

            # 问答对
            if "qa_pairs" in result:
                qa_pairs = result["qa_pairs"]
                print(f"   问答对数量: {len(qa_pairs)}")
                for i, qa in enumerate(qa_pairs[:2], 1):
                    print(f"   {i}. Q: {qa.get('question', 'N/A')[:60]}...")
                    print(f"      A: {qa.get('answer', 'N/A')[:60]}...")
                    print(f"      Level: {qa.get('level', 'N/A')} ({qa.get('level_name', 'N/A')})")
                print()

            print("   [SUCCESS] 研究流程完成!")
            print("5. 测试完成!")

    except Exception as e:
        print(f"   [ERROR] 测试异常: {e}")
        import traceback
        traceback.print_exc()
        return False

    return True


async def test_status_command():
    """测试 status 命令"""
    print()
    print("=" * 60)
    print("测试配置状态检查")
    print("=" * 60)
    print()

    checks = [
        ("MINIMAX_API_KEY", bool(config.minimax_api_key)),
        ("MINIMAX_BASE_URL", bool(config.minimax_base_url)),
        ("MINIMAX_MODEL", bool(config.minimax_model)),
        ("TAVILY_API_KEY", bool(config.tavily_api_key)),
    ]

    all_passed = True
    for name, passed in checks:
        status = "[OK]" if passed else "[MISSING]"
        print(f"   {status} {name}")
        if not passed:
            all_passed = False

    return all_passed


async def main():
    """主函数"""
    # 先测试状态
    status_ok = await test_status_command()

    if not status_ok:
        print()
        print("[WARN] 部分配置缺失，某些功能可能无法正常工作")
        print()

    # 测试研究流程
    result_ok = await test_research_flow()

    # 总结
    print()
    print("=" * 60)
    print("测试总结")
    print("=" * 60)
    print(f"   配置状态: {'通过' if status_ok else '部分缺失'}")
    print(f"   研究流程: {'通过' if result_ok else '失败'}")
    print()

    if status_ok and result_ok:
        print("[SUCCESS] 所有测试通过!")
        return 0
    else:
        print("[WARN] 部分测试未通过，请检查配置")
        return 1


if __name__ == "__main__":
    exit_code = asyncio.run(main())
    sys.exit(exit_code)