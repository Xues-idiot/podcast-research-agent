# Echo Frontend

播客研究Agent的前端界面。

## 技术栈

- **Next.js 15** - React框架
- **React 19** - UI库
- **TypeScript** - 类型安全
- **Tailwind CSS v4** - 样式
- **shadcn/ui** - UI组件
- **Motion** - 动画
- **Zustand** - 状态管理
- **Lucide React** - 图标

## 安装

```bash
cd frontend
npm install
```

## 开发

```bash
npm run dev
```

访问 http://localhost:3555

## 端口

- 前端: http://localhost:3555
- 后端API: http://localhost:8002

## 目录结构

```
frontend/
├── src/
│   ├── app/                 # Next.js App Router
│   │   ├── layout.tsx      # 根布局
│   │   ├── page.tsx        # 首页
│   │   └── podcast/
│   │       └── page.tsx    # 研究页面
│   ├── components/         # React组件
│   │   ├── ui/             # shadcn/ui组件
│   │   └── *.tsx           # 业务组件
│   ├── lib/
│   │   ├── api.ts          # API调用
│   │   └── utils.ts        # 工具函数
│   └── store/
│       └── podcast-store.ts # 状态管理
├── public/                 # 静态资源
└── package.json
```

## 组件清单

| 组件 | 说明 |
|------|------|
| `URLInput` | 链接输入框 |
| `Summary` | 摘要展示 |
| `KeyPoints` | 要点展示 |
| `MindMap` | 思维导图 |
| `Progress` | 进度条 |
| `Export` | 导出功能 |
| `PlatformBadge` | 平台标识 |
| `ApiStatus` | API状态 |
| `TranscriptPlayer` | 转录播放器 |
| `ErrorDisplay` | 错误展示 |
| `LoadingSkeleton` | 加载骨架屏 |
| `QAPairs` | 问答对 |
| `KnowledgeCards` | 知识卡片 |
| `Waveform` | 波形可视化 |
| `StepIndicator` | 步骤指示器 |
| `SearchInput` | 搜索框 |
| `ReportDisplay` | 报告展示 |
| `VoiceAvatar` | 语音头像 |

## 设计规范

### 配色方案

| 用途 | 颜色 | 值 |
|------|------|-----|
| 主色 | 藏青 | `#2C3E50` |
| 辅色 | 暖橙 | `#E67E22` |
| 点缀 | 米白 | `#F5F5DC` |
| 背景 | 暖灰 | `#FAF8F5` |

### 动画

所有UI元素使用 `motion` (Framer Motion) 实现动画过渡，包括：
- 卡片加载动画
- 进度条动画
- 思维导图展开/收起动画

---

*Echo Frontend | 2026-03-24*
