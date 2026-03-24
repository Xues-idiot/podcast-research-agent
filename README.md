---
name: echo-podcast-research
description: Echo - 播客研究Agent，让知识回响
---

# Echo - 播客研究Agent

> 代号 Echo (回声)，意为"让知识回响"

## 概述

Echo 是一个开源的播客研究Agent，帮助用户从播客/视频中高效提取知识。

**核心问题**：想从播客/视频中学习，但时间有限，无法听完每个小时的节目。

**解决方案**：输入播客链接或视频URL，自动转录、提取要点、生成摘要，告诉你"这个播客讲了什么、能用在哪儿"。

## 功能

- 🎙️ **转录** - 下载音视频并用 Whisper 转成文字
- 📝 **摘要** - 用 LLM 生成结构化摘要
- 🎯 **要点提取** - 提取核心观点和关键信息
- 🧠 **思维导图** - 生成知识结构图
- 💡 **知识关联** - 与已有知识库关联
- ❓ **问答生成** - 基于Bloom's Taxonomy认知层次生成问答对
- 🃏 **闪卡导出** - 导出为JSON/Markdown/HTML格式
- 📄 **报告生成** - 生成完整研究报告

## 支持的平台

- 🎬 **B站** - bilibili.com/video/BVxxx, b23.tv/xxx
- 📺 **YouTube** - youtube.com/watch?v=xxx, youtu.be/xxx
- 🎧 **播客RSS** - 支持标准RSS 2.0格式

## 安装

### 基本安装

```bash
pip install -e .
```

### 开发安装

```bash
pip install -e ".[dev]"
```

### API支持 (FastAPI)

```bash
pip install -e ".[api]"
```

### 完整安装

```bash
pip install -e ".[all]"
```

### 前端安装

```bash
cd frontend
npm install
```

## 配置

复制 `.env.example` 为 `.env`，填入API密钥：

```bash
cp .env.example .env
```

编辑 `.env`：

```bash
MINIMAX_API_KEY=your_minimax_api_key
MINIMAX_BASE_URL=https://api.minimaxi.com/anthropic
MINIMAX_MODEL=MiniMax-M2.7
TAVILY_API_KEY=your_tavily_api_key  # 可选，用于知识关联
```

## 使用

### Python API

```python
import asyncio
from echo import EchoClient

async def main():
    async with EchoClient() as client:
        result = await client.research(
            url="https://b23.tv/xxx",
            num_keypoints=5
        )

        # 打印摘要
        print(result["summary"]["title"])
        print(result["summary"]["summary"])

        # 打印要点
        for kp in result["keypoints"]:
            print(f"- {kp['content']}")

        # 思维导图
        print(result["mindmap"])

        # 问答对
        for qa in result.get("qa_pairs", []):
            print(f"Q: {qa['question']}")
            print(f"A: {qa['answer']}")
            print(f"Level: {qa.get('level', 'N/A')}")

asyncio.run(main())
```

### CLI

```bash
# 检查配置状态
echo status

# 研究播客/视频
echo research "https://b23.tv/xxx" --keypoints 5 --output ./output

# 获取视频信息（不下载）
echo info "https://youtube.com/watch?v=xxx"

# 输出格式 (json/markdown/both)
echo research "URL" --format both
```

### API Server

```bash
# 启动API服务器 (端口8002)
python scripts/api_server.py

# 或者使用uvicorn
uvicorn echo.api.research:router --host 0.0.0.0 --port 8002
```

### 前端界面

```bash
cd frontend
npm run dev
# 访问 http://localhost:3555
```

### SSE流式API

```bash
# 启动后端后，前端使用SSE接收实时进度
POST http://localhost:8002/api/research/stream
Content-Type: application/json

{"url": "https://b23.tv/xxx", "num_keypoints": 5}
```

事件流格式：
- `progress` - 当前步骤和进度
- `complete` - 完成，结果数据
- `error` - 错误信息
- `done` - 结束信号

## 项目结构

```
src/echo/
├── __init__.py           # 模块入口
├── client.py              # EchoClient 主客户端
├── config.py              # 配置管理
├── types.py               # 数据类型定义
├── exceptions.py          # 异常定义
├── agents/                # AI Agent 模块
│   ├── transcriber.py     # 音频转录 (Whisper)
│   ├── summarizer.py      # 摘要生成 (LLM)
│   ├── keypoint.py        # 要点提取 (LLM)
│   ├── linker.py          # 知识关联 (Tavily)
│   ├── mindmap.py         # 思维导图 (LLM)
│   ├── report.py          # 报告生成 (LLM)
│   ├── flashcard.py       # 闪卡导出
│   └── qa.py             # 问答生成
├── tools/                 # 工具模块
│   ├── downloader.py      # 统一下载接口
│   ├── bilibili.py        # B站下载
│   ├── youtube.py         # YouTube下载
│   └── podcast.py         # RSS解析
├── graph/                 # LangGraph编排
│   └── research_graph.py  # 研究流程图
└── api/                  # API接口
    └── research.py        # FastAPI路由

echo_cli/                  # CLI入口
frontend/                  # Next.js前端
├── src/
│   ├── app/               # App Router页面
│   ├── components/       # React组件
│   └── lib/              # 工具函数
tests/                     # 测试
├── unit/
└── integration/
scripts/                   # 脚本
├── quickstart.py
└── api_server.py         # API服务器入口
```

## 开发

```bash
# 安装开发依赖
pip install -e ".[dev]"

# 运行测试
pytest

# 代码格式化
ruff format src/ tests/

# 类型检查
mypy src/echo --ignore-missing-imports

# 一键检查
ruff format src/ tests/ && ruff check src/ tests/ && mypy src/echo --ignore-missing-imports && pytest
```

## 输出示例

```json
{
  "transcript": {
    "text": "...",
    "segments": [...],
    "language": "zh"
  },
  "summary": {
    "title": "如何用AI提升产品经理工作效率",
    "summary": "本集播客讨论了...",
    "highlights": ["AI自动化竞品调研", "LLM生成PRD初稿"]
  },
  "keypoints": [
    {"id": 1, "content": "AI可以自动化竞品调研", "importance": "high"}
  ],
  "mindmap": {
    "root": "AI提升PM效率",
    "branches": [...]
  },
  "knowledge_cards": [
    {
      "keypoint": "AI自动化调研",
      "related": [{"title": "竞品分析方法", "url": "https://..."}],
      "confidence": 0.85
    }
  ],
  "report": {
    "title": "AI时代PM效率提升指南",
    "content": "..."
  },
  "qa_pairs": [
    {
      "question": "如何用AI提升产品经理工作效率？",
      "answer": "可以通过AI自动化竞品调研、LLM生成PRD初稿等方式...",
      "level": "L2",
      "level_name": "理解",
      "knowledge_point": "AI应用",
      "estimated_time": "1-2分钟",
      "scoring_hint": "答案准确且完整地回应问题即可得分"
    }
  ]
}
```

## License

MIT

---

*代号: Echo | 2026-03-25*
