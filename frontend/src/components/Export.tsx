"use client"

import { motion } from "motion/react"
import { Card, CardHeader, CardTitle, CardContent } from "@/components/ui/card"
import { Button } from "@/components/ui/button"
import type { ResearchResult } from "@/lib/api"
import { Download, FileJson, FileText, Table2 } from "lucide-react"

interface ExportProps {
  result: ResearchResult
}

export function Export({ result }: ExportProps) {
  const handleExport = async (format: "json" | "markdown" | "csv") => {
    let content: string
    let filename: string
    let mimeType: string

    if (format === "json") {
      content = JSON.stringify(result, null, 2)
      filename = "research-result.json"
      mimeType = "application/json"
    } else if (format === "markdown") {
      content = generateMarkdown(result)
      filename = "research-result.md"
      mimeType = "text/markdown"
    } else {
      content = generateCSV(result)
      filename = "research-result.csv"
      mimeType = "text/csv"
    }

    // 创建下载
    const blob = new Blob([content], { type: mimeType })
    const url = URL.createObjectURL(blob)
    const a = document.createElement("a")
    a.href = url
    a.download = filename
    document.body.appendChild(a)
    a.click()
    document.body.removeChild(a)
    URL.revokeObjectURL(url)
  }

  const generateMarkdown = (result: ResearchResult): string => {
    const lines = [
      "# 研究报告",
      "",
      `## ${result.summary?.title || "无标题"}`,
      "",
      "## 摘要",
      result.summary?.summary || "",
      "",
      "## 亮点",
      ...(result.summary?.highlights || []).map((h) => `- ${h}`),
      "",
      "## 关键要点",
      ...(result.keypoints || []).map((kp) => `- ${kp.content}`),
      "",
    ]

    if (result.mindmap?.root) {
      lines.push("## 思维导图")
      lines.push(`**主题**: ${result.mindmap.root}`)
      for (const branch of result.mindmap.branches || []) {
        lines.push(`### ${branch.title}`)
        for (const child of branch.children || []) {
          lines.push(`- ${child}`)
        }
      }
    }

    return lines.join("\n")
  }

  const generateCSV = (result: ResearchResult): string => {
    const lines = ["问题,答案,重要性"]
    for (const kp of result.keypoints || []) {
      lines.push(`"${kp.content.replace(/"/g, '""')}","","${kp.importance}"`)
    }
    return lines.join("\n")
  }

  return (
    <motion.div
      initial={{ opacity: 0, y: 20 }}
      animate={{ opacity: 1, y: 0 }}
      transition={{ duration: 0.4, delay: 0.4 }}
    >
      <Card>
        <CardHeader>
          <CardTitle className="flex items-center gap-2">
            <Download className="w-5 h-5 text-[#2C3E50]" />
            导出
          </CardTitle>
        </CardHeader>
        <CardContent>
          <div className="grid grid-cols-3 gap-3">
            <Button
              variant="outline"
              onClick={() => handleExport("json")}
              className="flex flex-col items-center gap-1 h-auto py-4"
            >
              <FileJson className="w-6 h-6" />
              <span className="text-xs">JSON</span>
            </Button>

            <Button
              variant="outline"
              onClick={() => handleExport("markdown")}
              className="flex flex-col items-center gap-1 h-auto py-4"
            >
              <FileText className="w-6 h-6" />
              <span className="text-xs">Markdown</span>
            </Button>

            <Button
              variant="outline"
              onClick={() => handleExport("csv")}
              className="flex flex-col items-center gap-1 h-auto py-4"
            >
              <Table2 className="w-6 h-6" />
              <span className="text-xs">CSV</span>
            </Button>
          </div>
        </CardContent>
      </Card>
    </motion.div>
  )
}
