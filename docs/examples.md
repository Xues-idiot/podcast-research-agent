# Echo 使用示例

## 基础使用

### 1. 研究B站视频

```python
from echo import EchoClient
import asyncio

async def main():
    async with EchoClient() as client:
        result = await client.research(
            url="https://bilibili.com/video/BV1xx411c7mD",
            num_keypoints=5
        )
        print(result["summary"])

asyncio.run(main())
```

### 2. 研究YouTube视频

```python
from echo import EchoClient
import asyncio

async def main():
    async with EchoClient() as client:
        result = await client.research(
            url="https://www.youtube.com/watch?v=dQw4w9WgXcQ",
            num_keypoints=5
        )
        print(result["keypoints"])

asyncio.run(main())
```

### 3. 研究播客RSS

```python
from echo.tools.podcast import PodcastRSSParser
from echo import EchoClient
import asyncio

async def main():
    # 获取播客剧集
    parser = PodcastRSSParser()
    episodes = await parser.parse("https://example.com/podcast.rss")

    # 研究最新一集
    if episodes:
        async with EchoClient() as client:
            result = await client.research(
                url=episodes[0].audio_url,
                num_keypoints=5
            )

asyncio.run(main())
```

## 高级使用

### 4. 使用缓存

```python
from echo import EchoClient, get_cache
import asyncio

async def main():
    cache = get_cache()
    url = "https://bilibili.com/video/BVxxx"

    # 检查缓存
    cached = cache.get(url)
    if cached:
        print("使用缓存结果")
        print(cached)
        return

    # 执行研究
    async with EchoClient() as client:
        result = await client.research(url)

    # 存入缓存
    cache.set(url, result)
    print("结果已缓存")

asyncio.run(main())
```

### 5. 批量处理

```python
from echo import EchoClient
import asyncio

async def process_urls(urls: list):
    """批量处理多个URL"""
    results = []

    async with EchoClient() as client:
        for url in urls:
            try:
                result = await client.research(url)
                results.append({"url": url, "result": result, "success": True})
            except Exception as e:
                results.append({"url": url, "error": str(e), "success": False})

    return results

# 使用
urls = [
    "https://bilibili.com/video/BV1xx",
    "https://youtube.com/watch?v=xxx",
]

asyncio.run(process_urls(urls))
```

### 6. 自定义输出

```python
from echo.agents.flashcard import Exporter
from echo import EchoClient
import asyncio

async def main():
    async with EchoClient() as client:
        result = await client.research("https://bilibili.com/video/BVxxx")

        # 导出为多种格式
        exporter = Exporter("./output")
        paths = exporter.export_all(result)

        print("导出文件:")
        for format, path in paths.items():
            print(f"  {format}: {path}")

asyncio.run(main())
```

### 7. 使用API服务

```bash
# 启动API服务
uvicorn echo.api.research:router --host 0.0.0.0 --port 8000
```

```python
import httpx

# 调用API
async def call_api():
    async with httpx.AsyncClient() as client:
        # 启动研究任务
        response = await client.post(
            "http://localhost:8000/api/research/start",
            json={"url": "https://bilibili.com/video/BVxxx", "num_keypoints": 5}
        )
        task_id = response.json()["task_id"]

        # 等待完成
        import asyncio
        while True:
            await asyncio.sleep(5)
            status_response = await client.get(f"http://localhost:8000/api/research/status/{task_id}")
            status = status_response.json()
            print(f"Status: {status['status']}")
            if status["status"] in ("completed", "failed"):
                break

        # 获取结果
        result_response = await client.get(f"http://localhost:8000/api/research/result/{task_id}")
        return result_response.json()
```

### 8. 使用流式API (SSE)

```python
import httpx
import json

async def stream_research():
    """使用SSE流式接收研究进度"""
    async with httpx.AsyncClient(timeout=600.0) as client:
        async with client.stream(
            "POST",
            "http://localhost:8002/api/research/stream",
            json={"url": "https://b23.tv/BVxxx", "num_keypoints": 5}
        ) as response:
            async for line in response.aiter_lines():
                if line.startswith("data:"):
                    data = json.loads(line[5:])
                    if data["type"] == "progress":
                        print(f"进度: {data['progress']}% - {data.get('current_step', '')}")
                    elif data["type"] == "complete":
                        print("研究完成!")
                        return data["result"]
                    elif data["type"] == "error":
                        print(f"错误: {data['error']}")
```

## CLI使用

```bash
# 检查配置
echo status

# 研究视频
echo research "https://bilibili.com/video/BVxxx" --keypoints 5

# 指定输出目录
echo research "URL" --output ./results

# 指定输出格式
echo research "URL" --format json

# 获取视频信息
echo info "https://youtube.com/watch?v=xxx"
```

## 导出格式

### JSON导出

```python
from echo.agents.flashcard import Exporter

exporter = Exporter("./output")
exporter.export_json(result, "result.json")
```

### Markdown导出

```python
exporter.export_markdown(result, "result.md")
```

### CSV导出 (要点)

```python
exporter.export_csv(result, "keypoints.csv")
```

### 闪卡导出

```python
# JSON格式
exporter.export_flashcards(result, "cards.json", format="json")

# Markdown格式
exporter.export_flashcards(result, "cards.md", format="markdown")

# HTML格式
exporter.export_flashcards(result, "cards.html", format="html")
```
