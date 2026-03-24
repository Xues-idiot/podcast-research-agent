#!/usr/bin/env python3
"""测试流式 API - 验证 SSE 流式输出"""

import asyncio
import httpx
import json


async def test_streaming_api(base_url: str = "http://localhost:8002"):
    """测试流式 API 端点"""
    print("=" * 60)
    print("Echo 流式 API 测试")
    print("=" * 60)
    print()

    # 测试 URL
    test_url = "https://b23.tv/BV1xx411c7mu"

    print(f"1. 测试端点: POST {base_url}/api/research/stream")
    print(f"   测试 URL: {test_url}")
    print()

    try:
        async with httpx.AsyncClient(timeout=600.0) as client:
            print("2. 发送请求...")
            print("-" * 60)

            async with client.stream(
                "POST",
                f"{base_url}/api/research/stream",
                json={"url": test_url, "num_keypoints": 3},
                headers={"Content-Type": "application/json"},
            ) as response:
                print(f"   状态码: {response.status_code}")
                print()

                if response.status_code != 200:
                    print(f"   [ERROR] 响应错误: {response.status_code}")
                    return False

                event_count = 0
                async for line in response.aiter_lines():
                    if line.startswith("data:"):
                        data = line[5:].strip()
                        if data:
                            try:
                                event = json.loads(data)
                                event_type = event.get("type", "unknown")
                                event_count += 1

                                if event_type == "progress":
                                    step = event.get("current_step", "")
                                    progress = event.get("progress", 0)
                                    msg = event.get("message", "")[:40]
                                    print(f"   [PROGRESS] {step}: {progress}% - {msg}")

                                elif event_type == "complete":
                                    result = event.get("result", {})
                                    print()
                                    print("   [COMPLETE] 研究完成!")
                                    if "summary" in result:
                                        title = result["summary"].get("title", "N/A")
                                        print(f"   标题: {title}")
                                    if "keypoints" in result:
                                        kps = result["keypoints"]
                                        print(f"   要点: {len(kps)} 个")
                                    if "qa_pairs" in result:
                                        qa = result["qa_pairs"]
                                        print(f"   问答: {len(qa)} 对")

                                elif event_type == "error":
                                    error = event.get("error", "Unknown")
                                    print()
                                    print(f"   [ERROR] {error}")

                                elif event_type == "done":
                                    print()
                                    print(f"   [DONE] 流式响应结束 (共 {event_count} 个事件)")
                                    break

                            except json.JSONDecodeError:
                                pass

                print()
                print("3. 测试成功!")
                return True

    except httpx.ConnectError:
        print(f"   [ERROR] 无法连接到 {base_url}")
        print("   提示: 请确保后端 API 服务器正在运行")
        print("   启动命令: python scripts/api_server.py")
        return False
    except Exception as e:
        print(f"   [ERROR] {e}")
        return False


async def test_health_endpoint(base_url: str = "http://localhost:8002"):
    """测试健康检查端点"""
    print()
    print("=" * 60)
    print("健康检查测试")
    print("=" * 60)
    print()

    try:
        async with httpx.AsyncClient() as client:
            response = await client.get(f"{base_url}/health")
            print(f"   状态码: {response.status_code}")
            print(f"   响应: {response.json()}")
            return response.status_code == 200
    except httpx.ConnectError:
        print(f"   [ERROR] 无法连接到 {base_url}")
        return False


async def main():
    """主函数"""
    import sys

    base_url = sys.argv[1] if len(sys.argv) > 1 else "http://localhost:8002"

    # 测试健康检查
    health_ok = await test_health_endpoint(base_url)

    if not health_ok:
        print()
        print("[ERROR] API 服务器未运行，请先启动:")
        print("   python scripts/api_server.py")
        return 1

    # 测试流式 API
    print()
    stream_ok = await test_streaming_api(base_url)

    print()
    print("=" * 60)
    print("测试结果")
    print("=" * 60)
    print(f"   健康检查: {'通过' if health_ok else '失败'}")
    print(f"   流式 API: {'通过' if stream_ok else '失败'}")
    print()

    return 0 if (health_ok and stream_ok) else 1


if __name__ == "__main__":
    exit_code = asyncio.run(main())
    exit(exit_code)