# Echo 部署文档

本文档涵盖 Echo 播客研究 Agent 的完整部署流程。

---

## 环境要求

### 基础环境

| 组件 | 版本要求 | 说明 |
|------|---------|------|
| Python | >= 3.10 | 推荐 3.11+ |
| Node.js | >= 18.0 | 推荐 20.x LTS |
| npm | >= 9.0 | 随 Node.js 一起安装 |
| FFmpeg | 最新版 | 音频处理必需 |

### 必需 API 密钥

| 服务 | 密钥 | 获取地址 |
|------|------|---------|
| MiniMax API | `MINIMAX_API_KEY` | https://platform.minimaxi.com/ |
| Tavily API | `TAVILY_API_KEY` | https://tavily.com/ (可选) |

---

## 安装步骤

### 1. 克隆项目

```bash
git clone <repository-url>
cd podcast-research-agent
```

### 2. 配置环境变量

```bash
# 复制环境变量模板
cp .env.example .env

# 编辑 .env 文件，填入你的 API 密钥
MINIMAX_API_KEY=your_minimax_api_key
MINIMAX_BASE_URL=https://api.minimaxi.com/anthropic
MINIMAX_MODEL=MiniMax-M2.7
TAVILY_API_KEY=your_tavily_api_key  # 可选
```

### 3. 安装后端依赖

```bash
# 使用 pip 安装
pip install -e .

# 或安装所有可选依赖
pip install -e ".[all]"

# 开发依赖
pip install -e ".[dev]"
```

### 4. 安装前端依赖

```bash
cd frontend
npm install
```

### 5. 安装 FFmpeg

**macOS:**
```bash
brew install ffmpeg
```

**Ubuntu/Debian:**
```bash
sudo apt update
sudo apt install ffmpeg
```

**Windows:**
从 [ffmpeg.org](https://ffmpeg.org/download.html) 下载或使用 winget:
```bash
winget install ffmpeg
```

---

## 运行

### 开发模式

**后端 API 服务器:**
```bash
# 在项目根目录
python scripts/api_server.py

# 或使用 uvicorn 直接启动
uvicorn echo.api.research:router --host 0.0.0.0 --port 8002 --reload
```

**前端开发服务器:**
```bash
cd frontend
npm run dev
```

访问:
- 前端: http://localhost:3555
- 后端 API: http://localhost:8002

### 生产模式构建

**前端构建:**
```bash
cd frontend
npm run build
npm start
```

**后端运行:**
```bash
# 使用 gunicorn (推荐)
pip install gunicorn
gunicorn -w 4 -k uvicorn.workers.UvicornWorker "echo.api.research:router"

# 或使用 uvicorn
uvicorn echo.api.research:router --host 0.0.0.0 --port 8002 --workers 4
```

---

## Docker 部署 (可选)

### Dockerfile

```dockerfile
FROM python:3.11-slim

WORKDIR /app

# 安装系统依赖
RUN apt-get update && apt-get install -y \
    ffmpeg \
    && rm -rf /var/lib/apt/lists/*

# 复制并安装 Python 依赖
COPY pyproject.toml .
RUN pip install -e .

# 复制应用代码
COPY . .

# 暴露端口
EXPOSE 8002

# 启动命令
CMD ["uvicorn", "echo.api.research:router", "--host", "0.0.0.0", "--port", "8002"]
```

### 构建和运行

```bash
# 构建镜像
docker build -t echo-podcast-research .

# 运行容器
docker run -p 8002:8002 \
  -e MINIMAX_API_KEY=your_key \
  -e TAVILY_API_KEY=your_key \
  echo-podcast-research
```

---

## 目录结构

```
podcast-research-agent/
├── src/echo/                 # 后端源码
│   ├── agents/              # AI Agent 模块
│   ├── tools/               # 工具模块
│   ├── graph/              # LangGraph 流程
│   └── api/                 # FastAPI 路由
├── frontend/                # Next.js 前端
│   ├── src/
│   │   ├── app/           # 页面
│   │   └── components/    # React 组件
│   └── public/             # 静态资源
├── scripts/
│   └── api_server.py      # API 服务器入口
├── docs/
│   ├── deployment.md       # 本文档
│   └── examples.md        # 使用示例
└── tests/                  # 测试
```

---

## 验证部署

### 检查后端状态

```bash
curl http://localhost:8002/health
```

响应:
```json
{"status": "healthy"}
```

### 检查配置

```bash
echo status
```

### 测试研究流程

```bash
echo research "https://b23.tv/xxx" --keypoints 3
```

### 端到端测试脚本

项目提供了两个测试脚本用于验证部署:

#### 1. 直接测试 (需要 API 密钥)

```bash
# 启动后端
python scripts/api_server.py &

# 运行端到端测试
python scripts/test_e2e.py
```

#### 2. API 流式测试 (需要后端运行)

```bash
# 先启动后端
python scripts/api_server.py

# 另开终端运行流式 API 测试
python scripts/test_streaming_api.py
```

### 端到端测试内容

测试脚本验证以下功能:

| 测试项 | 说明 |
|-------|------|
| 配置检查 | 验证 API 密钥是否设置 |
| 下载 | B站/YouTube 视频下载 |
| 转录 | Whisper 音频转文字 |
| 摘要 | LLM 生成摘要 |
| 要点 | 提取关键要点 |
| 思维导图 | 生成知识结构 |
| 报告 | 生成完整报告 |
| 问答 | 基于 Bloom's Taxonomy 生成问答 |
| 流式输出 | SSE 实时进度推送 |

---

## 常见问题

### 1. Whisper 转录失败

**原因:** FFmpeg 未安装或不在 PATH 中

**解决:**
```bash
# 验证 FFmpeg 安装
ffmpeg -version

# Windows: 重启终端或手动添加到 PATH
```

### 2. API 连接错误

**原因:** API 密钥无效或网络问题

**解决:**
- 检查 `.env` 中的 `MINIMAX_API_KEY`
- 确认网络可以访问 `api.minimaxi.com`

### 3. 前端无法连接后端

**原因:** CORS 配置或端口不匹配

**解决:**
- 确认后端运行在 `http://localhost:8002`
- 检查前端 `api.ts` 中的 `API_BASE_URL`

### 4. 内存不足

**原因:** 处理长视频时 Whisper 占用大量内存

**解决:**
- 使用更小的 Whisper 模型 (如 `base` 而非 `large`)
- 增加系统虚拟内存

---

## 性能优化

### Whisper 模型选择

| 模型 | 内存需求 | 速度 | 精度 |
|------|---------|------|------|
| tiny | ~1GB | 最快 | 较低 |
| base | ~1GB | 快 | 中等 |
| small | ~2GB | 中等 | 较高 |
| medium | ~5GB | 慢 | 高 |
| large | ~10GB | 最慢 | 最高 |

设置环境变量切换模型:
```bash
WHISPER_MODEL=base
```

### 并发限制

API 服务器默认单 worker，开发环境够用。生产环境建议:
```bash
# 4 worker 示例
uvicorn echo.api.research:router --workers 4
```

---

## 安全注意事项

1. **API 密钥保护**: 不要将 `.env` 提交到版本控制
2. **CORS**: 生产环境建议限制 `allow_origins`
3. **速率限制**: API 已实现内置限流 (每分钟10次请求)
4. **文件上传**: 注意处理大文件时的资源限制

---

## 下一步

部署完成后，你可以:

- 使用 `echo research <URL>` 开始研究播客
- 访问 http://localhost:3555 使用前端界面
- 查看 [examples.md](examples.md) 了解更多使用场景

---

*部署文档 | Echo | 2026-03-25*