# Echo (播客研究Agent) - 初始指令

> 代号 Echo (回声)，意为"让知识回响"

## 项目定位

**核心问题**：想从播客/视频中学习，但时间有限，无法听完每个小时的节目。

**解决方案**：输入播客链接或视频URL，自动转录、提取要点、生成摘要，告诉你"这个播客讲了什么、能用在哪儿"。

> 注意：我们不是做另一个NotebookLM，而是做一个**垂直领域的**、**开源可部署的**版本

---

## 参考项目分析

### notebooklm-py
**Stars**: 7.2k | **架构**: Python + CLI + API

**核心功能**:
- 调用Google NotebookLM的非官方API
- 支持播客转录、摘要生成
- 生成音频Overview、问答、思维导图

**技术要点**:
```python
from notebooklm import NotebookLMClient

async with NotebookLMClient.from_storage() as client:
    nb = await client.notebooks.create("Research")
    await client.sources.add_url(nb.id, url)
    result = await client.chat.ask(nb.id, "Summarize this")
    # 生成音频、问答、摘要
```

**启发**:
- 完整的notebook概念
- 多模态内容生成（音频、视频、思维导图）
- 与LLM agent集成

**我们的差异**:
- NotebookLM是闭源服务，依赖Google
- 我们要做**开源可部署**版本
- 接入国产模型（DeepSeek/MiniMax）
- **国内市场特色**：B站/抖音视频、微信公众号/视频号、小红书播客RSS

**开源差异** (如果未来发布 GitHub)：
- 原项目 NotebookLM 依赖 Google 闭源服务
- 我们是**纯开源可自托管**版本，数据完全自主
- 支持国内平台（B站、抖音等）是原生能力

---

## 核心功能设计

### 1. 播客/视频输入 → 知识提取
```
输入：B站视频链接 / YouTube链接 / 播客RSS
输出：
┌─────────────────────────────────────────────────────┐
│ 🎙️ 播客研究 - Echo                                  │
├─────────────────────────────────────────────────────┤
│ 📌 标题: 如何用AI提升产品经理的工作效率                │
│ 🎤 主播: 产品二三事                                    │
│ ⏱️ 时长: 58:32                                      │
│ 📅 发布: 2026-03-20                                  │
├─────────────────────────────────────────────────────┤
│ 📝 核心要点 (5个):                                   │
│ 1. AI可以自动化竞品调研（节省40%时间）                 │
│ 2. 用LLM生成PRD初稿不是替代是提效                   │
│ 3. 提醒：AI输出需要人工审核                           │
│ 4. 工具推荐：Claude + Notion AI                      │
│ 5. 最佳实践：先用AI头脑风暴，再用AI写文档             │
├─────────────────────────────────────────────────────┤
│ 💡 能用在哪里:                                        │
│ • 竞品调研环节（用要点1+4）                          │
│ • PRD撰写流程（用要点2+5）                           │
│ • 团队培训分享（用要点3）                             │
├─────────────────────────────────────────────────────┤
│ 🔗 原文链接: https://xxx                             │
│ 置信度: 82%                                         │
└─────────────────────────────────────────────────────┘
```

### 2. 工作流程
```
输入URL/上传文件
       ↓
┌─────────────────────────────────┐
│  转录Agent (Whisper)            │ ← 音频转文字
└─────────────────────────────────┘
       ↓ 文本
┌─────────────────────────────────┐
│  摘要Agent (LLM)                │ ← 提取关键信息
└─────────────────────────────────┘
       ↓
┌─────────────────────────────────┐
│  要点生成Agent                   │ ← 生成结构化要点
└─────────────────────────────────┘
       ↓
┌─────────────────────────────────┐
│  知识关联Agent                   │ ← 与已有知识库关联
└─────────────────────────────────┘
       ↓
┌─────────────────────────────────┐
│  输出: 摘要 + 要点 + 知识卡片     │
└─────────────────────────────────┘
```

### 3. 多模态输出
- 📝 文字摘要
- 🎯 结构化要点
- 🧠 思维导图 (JSON)
- ❓ 问答对
- 📚 延伸阅读推荐

---

## 技术架构

### 后端
```
backend/
├── agents/
│   ├── transcriber.py      # 转录Agent (Whisper)
│   ├── summarizer.py      # 摘要Agent
│   ├── keypoint.py       # 要点生成
│   ├── linker.py         # 知识关联
│   └── exporter.py       # 导出
├── tools/
│   ├── whisper.py         # 语音转文字
│   ├── bilibili.py       # B站视频下载+转录
│   ├── youtube.py        # YouTube下载+转录
│   └── podcast.py         # 播客RSS解析
├── graph/
│   └── research_graph.py # LangGraph编排
└── api/
    └── research.py        # API接口
```

### 前端
```
frontend/
├── src/
│   ├── app/
│   │   └── podcast/
│   │       └── page.tsx  # 研究页面
│   ├── components/
│   │   ├── URLInput.tsx  # 链接输入
│   │   ├── Summary.tsx   # 摘要展示
│   │   ├── KeyPoints.tsx # 要点展示
│   │   ├── MindMap.tsx  # 思维导图
│   │   ├── Export.tsx   # 导出
│   │   └── ui/             # shadcn/ui 组件
│   ├── lib/
│   │   ├── api.ts          # API 调用
│   │   └── utils.ts         # 工具函数
│   └── store/
│       └── podcast-store.ts  # Zustand 状态管理
```

**前端设计规范** ⚠️ 必须遵循，避免 AI 死板风格：

1. **动画优先**
   - 必须使用 `motion` (Framer Motion) 做动画
   - 禁止出现"死板"、没有过渡效果的 UI
   - 卡片加载、进度展示、思维导图展开都要有动画
   - 参考：https://motion.dev/

2. **配色方案**
   - ❌ 禁止用默认的 AI 蓝/紫色（#007AFF, #6366F1 等）
   - ✅ MVP阶段：shadcn/ui `zinc` 或 `stone` 主题（温暖中性质感）
   - ✅ 后续可调整：学术感（藏青+暖色）、播客暖色调、年度流行色
   - 参考 shadcn/ui 的默认配色
   - 配色工具：https://ui.shadcn.com/themes

3. **字体选择**
   - ✅ 使用 Inter 或其他成熟无衬线字体
   - ❌ 禁止用系统默认中文字体
   - 字体平台：Google Fonts

4. **技术栈**
   - Next.js 15 + React 19 + TypeScript
   - Tailwind CSS v4 + shadcn/ui
   - Zustand 状态管理
   - SSE 流式输出（用于转录进度、摘要生成）
   - Motion 动画

5. **组件规范**
   - 优先使用 shadcn/ui 组件
   - 组件要有 hover、focus、active 状态
   - 进度条要有动画
   - 思维导图要有展开/收起动画

6. **设计参考**
   - https://v0.dev/ - Vercel AI UI 参考
   - https://ui.shadcn.com/ - shadcn/ui 组件库
   - https://motion.dev/ - 动画库

---

## 技术要点

### 1. 转录
```python
# Whisper 本地转录
import whisper
model = whisper.load_model("base")
result = model.transcribe("audio.mp3")
```

### 2. 视频下载
```python
# yt-dlp 下载B站/YouTube
import yt_dlp
ydl_opts = {...}
with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    ydl.download([url])
```

### 3. 知识提取
```python
# 用LLM提取要点
response = llm.invoke(f"""
请从以下转录文本中提取5个核心要点：

{transcript}

格式：
1. [要点1]
2. [要点2]
...
""")
```

### 4. 知识关联
```python
# 与已有知识库关联
results = vectorstore.similarity_search(key_point, k=3)
```

---

## 服务配置

### 端口配置
```
前端: http://localhost:3555
后端API: http://localhost:8002/docs
```

### 配色方案（播客研究项目特色）
- **主色**: 藏青 `#2C3E50`（学术、沉稳）
- **辅色**: 暖橙 `#E67E22`（温暖、亲和）
- **点缀色**: 米白 `#F5F5DC`（知识、书籍感）
- **背景**: 暖灰 `#FAF8F5`（纸质、柔和）
- MVP阶段: shadcn/ui `stone` 主题 + 上述配色点缀

### 学习参考
- **现有项目**: `pm-assistant/` (Pi) - 学习端口配置、预测系统架构
- **现有项目**: `private-operation-agent/` (Nu) - 学习工作流设计
- **参考项目**: `notebooklm-py/` - 播客研究架构

---

## 参考资料

```
_reference/
└── notebooklm-py/      # NotebookLM API参考
    ├── src/notebooklm/
    ├── docs/
    └── SKILL.md
```

---

## 配置信息

### 环境变量 (.env)
```
MINIMAX_API_KEY=sk-cp-VcIZBwmaK5F8jNkpaJ4vvxjCoVSujEVSRyMhn-Xu2aaOth6JbMXVOcRt8pZ9ZFsqTcZ8MESiP8VP833TvcibXmw3hdOS9Evr5wcIN3eCjPoYbkQuxOyFz9s
MINIMAX_BASE_URL=https://api.minimaxi.com/anthropic
MINIMAX_MODEL=MiniMax-M2.7
TAVILY_API_KEY=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
GITHUB_TOKEN=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
```

### Sigma Skills 参考
```
D:/PM-AI-Workstation/01-ai-agents/pm-agent-forge/skills/
├── data-analytics/            # 数据分析Skills
│   ├── data-mining/
│   └── visualization-creation/
├── finance/                    # 金融相关Skills
│   └── financial-report-analysis/
└── common/
    └── critical-thinking/    # 批判性思维
```

---

## 初始任务

1. 研究notebooklm-py的API调用方式
2. 选一个视频平台（B站）实现下载+转录
3. 用LLM实现要点提取
4. 实现思维导图生成
5. 添加前端UI

---

*代号: Echo | 2026-03-24*
