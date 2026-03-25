"use client"

import { useState } from "react"
import { motion } from "motion/react"
import { Card, CardHeader, CardTitle, CardContent } from "@/components/ui/card"
import { Button } from "@/components/ui/button"
import type { ResearchResult } from "@/lib/api"
import { Download, FileJson, FileText, Table2, File, FileCode, Presentation, Eye } from "lucide-react"

type ExportFormat = "json" | "markdown" | "csv" | "txt" | "html" | "pdf"

const EXPORT_FORMATS: Array<{ format: ExportFormat; icon: typeof FileJson; label: string }> = [
  { format: "json", icon: FileJson, label: "JSON" },
  { format: "markdown", icon: FileText, label: "Markdown" },
  { format: "csv", icon: Table2, label: "CSV" },
  { format: "html", icon: FileCode, label: "HTML" },
  { format: "pdf", icon: Presentation, label: "PDF" },
  { format: "txt", icon: File, label: "文本" },
]

interface ExportProps {
  result: ResearchResult
}

export function Export({ result }: ExportProps) {
  const [previewFormat, setPreviewFormat] = useState<string | null>(null)

  const getExportPreview = (format: string): string => {
    switch (format) {
      case "json":
        return `包含: 摘要(${result.summary ? 1 : 0}), 要点(${result.keypoints?.length || 0}), 思维导图(${result.mindmap ? 1 : 0}), 问答(${result.qa_pairs?.length || 0})`
      case "markdown":
        return `Markdown格式，适合阅读和笔记整理`
      case "csv":
        return `表格格式，要点+问答共${(result.keypoints?.length || 0) + (result.qa_pairs?.length || 0)}条`
      case "html":
        return `完整样式，浏览器直接打开即可`
      case "pdf":
        return `通过服务器生成PDF文档`
      case "txt":
        return `纯文本格式，通用性最强`
      default:
        return ""
    }
  }

  const handleExport = async (format: "json" | "markdown" | "csv" | "txt" | "html" | "pdf") => {
    setPreviewFormat(null) // Close preview on export
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
    } else if (format === "html") {
      content = generateHTML(result)
      filename = "research-result.html"
      mimeType = "text/html"
    } else if (format === "pdf") {
      // PDF需要通过API生成
      const response = await fetch("/api/research/export", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ result, format: "pdf" }),
      })
      if (response.ok) {
        const blob = await response.blob()
        const url = URL.createObjectURL(blob)
        const a = document.createElement("a")
        a.href = url
        a.download = "research-result.pdf"
        document.body.appendChild(a)
        a.click()
        document.body.removeChild(a)
        URL.revokeObjectURL(url)
      }
      return
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

  const generateHTML = (result: ResearchResult): string => {
    return `<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>${result.summary?.title || "研究报告"} - Echo</title>
    <style>
        * { box-sizing: border-box; margin: 0; padding: 0; }
        body { font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif; line-height: 1.6; color: #333; max-width: 900px; margin: 0 auto; padding: 20px; background: #fafafa; }
        .card { background: white; border-radius: 12px; padding: 24px; margin-bottom: 20px; box-shadow: 0 2px 8px rgba(0,0,0,0.08); }
        h1 { color: #2C3E50; font-size: 2em; margin-bottom: 20px; border-bottom: 3px solid #E67E22; padding-bottom: 10px; }
        h2 { color: #2C3E50; font-size: 1.4em; margin: 20px 0 10px; }
        h3 { color: #34495e; font-size: 1.1em; margin: 15px 0 8px; }
        p { margin: 10px 0; }
        ul, ol { margin: 10px 0 10px 20px; }
        li { margin: 5px 0; }
        .highlight { background: #FFF3E0; border-left: 4px solid #E67E22; padding: 10px 15px; margin: 15px 0; border-radius: 0 8px 8px 0; }
        .mindmap { background: #f8f9fa; padding: 15px; border-radius: 8px; }
        .mindmap-node { font-weight: bold; color: #2C3E50; }
        .branch { margin-left: 20px; border-left: 2px solid #E67E22; padding-left: 15px; }
        .qa-card { background: #f8f9fa; border-radius: 8px; padding: 15px; margin: 10px 0; border: 1px solid #e0e0e0; }
        .qa-question { font-weight: bold; color: #2C3E50; margin-bottom: 8px; }
        .qa-answer { color: #555; margin-left: 15px; }
        .qa-meta { font-size: 0.85em; color: #888; margin-top: 5px; }
        .tag { display: inline-block; background: #E67E22; color: white; padding: 2px 8px; border-radius: 4px; font-size: 0.75em; margin-left: 8px; }
        .report-content { white-space: pre-wrap; background: #f8f9fa; padding: 15px; border-radius: 8px; }
        .footer { text-align: center; color: #888; font-size: 0.85em; margin-top: 30px; padding-top: 20px; border-top: 1px solid #e0e0e0; }
    </style>
</head>
<body>
    <h1>${result.summary?.title || "研究报告"}</h1>

    ${result.summary?.summary ? `
    <div class="card">
        <h2>摘要</h2>
        <div class="highlight">${result.summary.summary}</div>
    </div>
    ` : ""}

    ${result.summary?.highlights?.length ? `
    <div class="card">
        <h2>亮点</h2>
        <ul>
            ${result.summary.highlights.map(h => `<li>${h}</li>`).join("")}
        </ul>
    </div>
    ` : ""}

    ${result.keypoints?.length ? `
    <div class="card">
        <h2>关键要点</h2>
        <ul>
            ${result.keypoints.map(kp => `<li><strong>${kp.content}</strong>${kp.importance ? `<span class="tag">${kp.importance}</span>` : ""}</li>`).join("")}
        </ul>
    </div>
    ` : ""}

    ${result.mindmap?.root ? `
    <div class="card">
        <h2>思维导图</h2>
        <div class="mindmap">
            <div class="mindmap-node">${result.mindmap.root}</div>
            ${result.mindmap.branches?.map(branch => `
                <div class="branch">
                    <strong>${branch.title}</strong>
                    ${branch.children?.length ? `<ul>${branch.children.map(c => `<li>${c}</li>`).join("")}</ul>` : ""}
                </div>
            `).join("")}
        </div>
    </div>
    ` : ""}

    ${result.qa_pairs?.length ? `
    <div class="card">
        <h2>问答对</h2>
        ${result.qa_pairs.map((qa, i) => `
            <div class="qa-card">
                <div class="qa-question">Q${i + 1}: ${qa.question}</div>
                <div class="qa-answer">A: ${qa.answer}</div>
                ${qa.level ? `<div class="qa-meta">认知层次: ${qa.level} - ${qa.level_name || ""}</div>` : ""}
                ${qa.knowledge_point ? `<div class="qa-meta">知识点: ${qa.knowledge_point}</div>` : ""}
            </div>
        `).join("")}
    </div>
    ` : ""}

    ${result.report ? `
    <div class="card">
        <h2>研究报告</h2>
        <div class="report-content">${result.report.content || result.report.title || ""}</div>
    </div>
    ` : ""}

    <div class="footer">
        由 Echo 播客研究Agent生成 | ${new Date().toLocaleDateString("zh-CN")}
    </div>
</body>
</html>`
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
          <div className="grid grid-cols-3 gap-3">
            {previewFormat && (
              <motion.div
                initial={{ opacity: 0, y: -10 }}
                animate={{ opacity: 1, y: 0 }}
                className="col-span-3 p-3 bg-[#FAF8F5] rounded-lg text-sm text-[#2C3E50]/70 mb-2"
              >
                {getExportPreview(previewFormat)}
              </motion.div>
            )}

            {EXPORT_FORMATS.map(({ format, icon: Icon, label }) => (
              <motion.div
                key={format}
                whileHover={{ scale: 1.02 }}
                whileTap={{ scale: 0.98 }}
              >
                <Button
                  variant="outline"
                  onClick={() => handleExport(format)}
                  onMouseEnter={() => setPreviewFormat(format)}
                  onMouseLeave={() => setPreviewFormat(null)}
                  className="flex flex-col items-center gap-1 h-auto py-4 w-full relative"
                >
                  <Icon className={`w-6 h-6 ${previewFormat === format ? 'text-[#E67E22]' : ''}`} />
                  <span className="text-xs">{label}</span>
                </Button>
              </motion.div>
            ))}
          </div>
        </CardContent>
      </Card>
    </motion.div>
  )
}
