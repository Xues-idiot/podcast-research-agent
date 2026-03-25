"use client"

import { useState } from "react"
import { motion } from "motion/react"
import { Card, CardHeader, CardTitle, CardContent } from "@/components/ui/card"
import { FileText, Copy, Check, Download, Maximize2 } from "lucide-react"

interface ReportDisplayProps {
  report: {
    title?: string
    content?: string
    summary?: {
      title?: string
      summary?: string
      highlights?: string[]
    }
    keypoints?: Array<{
      id?: number
      content?: string
      importance?: string
    }>
    mindmap?: {
      root?: string
      branches?: Array<{
        title?: string
        children?: string[]
      }>
    }
  }
}

export function ReportDisplay({ report }: ReportDisplayProps) {
  const [copied, setCopied] = useState(false)
  const [isFullscreen, setIsFullscreen] = useState(false)

  if (!report || !report.content) {
    return null
  }

  const copyToClipboard = async () => {
    try {
      await navigator.clipboard.writeText(report.content || "")
      setCopied(true)
      setTimeout(() => setCopied(false), 2000)
    } catch (err) {
      console.error("Failed to copy:", err)
    }
  }

  const downloadReport = () => {
    const content = `# ${report.title || "研究报告"}\n\n${report.content}`
    const blob = new Blob([content], { type: "text/markdown" })
    const url = URL.createObjectURL(blob)
    const a = document.createElement("a")
    a.href = url
    a.download = `report_${Date.now()}.md`
    document.body.appendChild(a)
    a.click()
    URL.revokeObjectURL(url)
  }

  return (
    <motion.div
      initial={{ opacity: 0, y: 20 }}
      animate={{ opacity: 1, y: 0 }}
      transition={{ duration: 0.4, delay: 0.5 }}
    >
      <Card className={`border-l-4 border-l-[#2C3E50] ${isFullscreen ? "fixed inset-4 z-50 overflow-auto" : ""}`}>
        <CardHeader>
          <div className="flex items-center justify-between">
            <CardTitle className="flex items-center gap-2">
              <FileText className="w-5 h-5 text-[#2C3E50]" />
              {report.title || "研究报告"}
            </CardTitle>
            <div className="flex items-center gap-1">
              <button
                onClick={() => setIsFullscreen(!isFullscreen)}
                className="p-2 rounded-lg hover:bg-[#2C3E50]/10 transition-colors"
                title={isFullscreen ? "退出全屏" : "全屏查看"}
              >
                <Maximize2 className="w-4 h-4 text-[#2C3E50]/50" />
              </button>
              <button
                onClick={copyToClipboard}
                className="p-2 rounded-lg hover:bg-[#2C3E50]/10 transition-colors"
                title="复制报告"
              >
                {copied ? (
                  <Check className="w-4 h-4 text-green-500" />
                ) : (
                  <Copy className="w-4 h-4 text-[#2C3E50]/50" />
                )}
              </button>
              <button
                onClick={downloadReport}
                className="p-2 rounded-lg hover:bg-[#2C3E50]/10 transition-colors"
                title="下载报告"
              >
                <Download className="w-4 h-4 text-[#2C3E50]/50" />
              </button>
            </div>
          </div>
        </CardHeader>
        <CardContent>
          <div className="prose prose-sm max-w-none">
            <div className="text-[#2C3E50]/80 leading-relaxed whitespace-pre-wrap">
              {report.content}
            </div>
          </div>
        </CardContent>
      </Card>

      {/* Fullscreen backdrop */}
      {isFullscreen && (
        <motion.div
          initial={{ opacity: 0 }}
          animate={{ opacity: 1 }}
          className="fixed inset-0 bg-black/20 z-40"
          onClick={() => setIsFullscreen(false)}
        />
      )}
    </motion.div>
  )
}
