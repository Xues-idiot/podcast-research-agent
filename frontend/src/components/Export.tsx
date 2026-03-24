"use client"

import { motion } from "motion/react"
import { Card, CardHeader, CardTitle, CardContent } from "@/components/ui/card"
import { Button } from "@/components/ui/button"
import type { ResearchResult } from "@/lib/api"
import { Download, FileJson, FileText, Table2, File } from "lucide-react"

interface ExportProps {
  result: ResearchResult
}

export function Export({ result }: ExportProps) {
  const handleExport = async (format: "json" | "markdown" | "csv" | "txt") => {
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
    } else if (format === "csv") {
      content = generateCSV(result)
      filename = "research-result.csv"
      mimeType = "text/csv"
    } else {
      content = generatePlainText(result)
      filename = "research-result.txt"
      mimeType = "text/plain"
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
      lines.push("")
    }

    // 问答对
    if (result.qa_pairs && result.qa_pairs.length > 0) {
      lines.push("## 问答对")
      lines.push("")
      for (let i = 0; i < result.qa_pairs.length; i++) {
        const qa = result.qa_pairs[i]
        lines.push(`### Q${i + 1}: ${qa.question}`)
        lines.push("")
        lines.push(`**A:** ${qa.answer}`)
        lines.push("")
        if (qa.level) {
          lines.push(`*认知层次: ${qa.level} - ${qa.level_name || ""}*`)
          lines.push("")
        }
        if (qa.knowledge_point) {
          lines.push(`*知识点: ${qa.knowledge_point}*`)
          lines.push("")
        }
        if (qa.scoring_hint) {
          lines.push(`*评分提示: ${qa.scoring_hint}*`)
          lines.push("")
        }
        lines.push("---")
        lines.push("")
      }
    }

    // 报告
    if (result.report) {
      lines.push("## 研究报告")
      lines.push("")
      lines.push(`### ${result.report.title || "报告"}`)
      lines.push("")
      lines.push(result.report.content || "")
      lines.push("")
    }

    return lines.join("\n")
  }

  const generateCSV = (result: ResearchResult): string => {
    const lines = ["类型,问题,答案,认知层次,知识点,预计时间"]

    // 要点
    for (const kp of result.keypoints || []) {
      lines.push(`"要点","${kp.content.replace(/"/g, '""')}","","","${kp.importance || ""}"`)
    }

    // 问答对
    for (const qa of result.qa_pairs || []) {
      lines.push(`"问答","${qa.question.replace(/"/g, '""')}","${qa.answer.replace(/"/g, '""')}","${qa.level || ""} ${qa.level_name || ""}","${qa.knowledge_point || ""}","${qa.estimated_time || ""}"`)
    }

    return lines.join("\n")
  }

  const generatePlainText = (result: ResearchResult): string => {
    const lines: string[] = []

    // 标题
    lines.push(result.summary?.title || "研究报告")
    lines.push("=".repeat(30))
    lines.push("")

    // 摘要
    if (result.summary?.summary) {
      lines.push("【摘要】")
      lines.push(result.summary.summary)
      lines.push("")
    }

    // 要点
    if (result.keypoints && result.keypoints.length > 0) {
      lines.push("【关键要点】")
      for (let i = 0; i < result.keypoints.length; i++) {
        lines.push(`${i + 1}. ${result.keypoints[i].content}`)
      }
      lines.push("")
    }

    // 思维导图
    if (result.mindmap?.root) {
      lines.push("【思维导图】")
      lines.push(`主题: ${result.mindmap.root}`)
      for (const branch of result.mindmap.branches || []) {
        lines.push(`  - ${branch.title}`)
        if (branch.children) {
          for (const child of branch.children) {
            lines.push(`    * ${child}`)
          }
        }
      }
      lines.push("")
    }

    // 问答对
    if (result.qa_pairs && result.qa_pairs.length > 0) {
      lines.push("【问答对】")
      for (let i = 0; i < result.qa_pairs.length; i++) {
        const qa = result.qa_pairs[i]
        lines.push(`Q${i + 1}: ${qa.question}`)
        lines.push(`A: ${qa.answer}`)
        if (qa.level) {
          lines.push(`  [${qa.level} ${qa.level_name || ""}]`)
        }
        lines.push("")
      }
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
          <div className="grid grid-cols-4 gap-3">
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

            <Button
              variant="outline"
              onClick={() => handleExport("txt")}
              className="flex flex-col items-center gap-1 h-auto py-4"
            >
              <File className="w-6 h-6" />
              <span className="text-xs">文本</span>
            </Button>
          </div>
        </CardContent>
      </Card>
    </motion.div>
  )
}
