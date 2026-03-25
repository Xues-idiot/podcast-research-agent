"use client"

import { motion } from "motion/react"
import { Card, CardHeader, CardTitle, CardContent } from "@/components/ui/card"
import { AlertCircle, RefreshCw, Home, AlertTriangle, Wifi, Download, FileX } from "lucide-react"

interface ErrorDisplayProps {
  error: string
  onRetry?: (url?: string) => void
  onHome?: () => void
}

// 常见错误类型和对应的解决建议
const errorPatterns: Array<{
  pattern: RegExp
  title: string
  icon: React.ReactNode
  suggestion: string
}> = [
  {
    pattern: /network|network error|fetch|connection/i,
    title: "网络连接失败",
    icon: <Wifi className="w-5 h-5" />,
    suggestion: "请检查网络连接，或稍后重试",
  },
  {
    pattern: /download|yt-dlp|youtube|bilibili|b23\.tv/i,
    title: "下载失败",
    icon: <Download className="w-5 h-5" />,
    suggestion: "请确认链接是否有效，或尝试其他视频源",
  },
  {
    pattern: /transcri|whisper|speech/i,
    title: "转录失败",
    icon: <FileX className="w-5 h-5" />,
    suggestion: "音频无法被识别，请尝试其他链接",
  },
  {
    pattern: /timeout|time.*out/i,
    title: "请求超时",
    icon: <AlertTriangle className="w-5 h-5" />,
    suggestion: "服务器响应超时，请稍后重试",
  },
]

function parseError(error: string) {
  for (const { pattern, title, icon, suggestion } of errorPatterns) {
    if (pattern.test(error)) {
      return { title, icon, suggestion }
    }
  }
  return {
    title: "出错了",
    icon: <AlertCircle className="w-5 h-5" />,
    suggestion: "请稍后重试，或联系技术支持",
  }
}

export function ErrorDisplay({ error, onRetry, onHome }: ErrorDisplayProps) {
  const { title, icon, suggestion } = parseError(error)

  // 截断错误信息显示
  const displayError = error.length > 200 ? error.slice(0, 200) + "..." : error

  return (
    <motion.div
      initial={{ opacity: 0, scale: 0.95 }}
      animate={{ opacity: 1, scale: 1 }}
      transition={{ duration: 0.3 }}
    >
      <Card className="border-l-4 border-l-red-500 bg-red-50/50">
        <CardHeader>
          <CardTitle className="flex items-center gap-2 text-red-600">
            {icon}
            {title}
          </CardTitle>
        </CardHeader>
        <CardContent>
          <div className="bg-white/60 rounded-lg p-3 mb-4">
            <p className="text-[#2C3E50]/60 text-sm mb-2">错误详情：</p>
            <p className="text-[#2C3E50]/80 font-mono text-xs">{displayError}</p>
          </div>
          <p className="text-[#2C3E50]/60 text-sm mb-4">
            💡 {suggestion}
          </p>
          <div className="flex gap-3">
            {onRetry && (
              <button
                onClick={() => onRetry()}
                className="flex items-center gap-2 px-4 py-2 bg-[#2C3E50] text-white rounded-lg hover:bg-[#34495E] transition-colors"
              >
                <RefreshCw className="w-4 h-4" />
                重试
              </button>
            )}
            {onHome && (
              <button
                onClick={onHome}
                className="flex items-center gap-2 px-4 py-2 bg-[#E67E22] text-white rounded-lg hover:bg-[#D35400] transition-colors"
              >
                <Home className="w-4 h-4" />
                返回首页
              </button>
            )}
          </div>
        </CardContent>
      </Card>
    </motion.div>
  )
}