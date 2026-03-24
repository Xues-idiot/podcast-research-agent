"use client"

import { motion } from "motion/react"
import { Card, CardHeader, CardTitle, CardContent } from "@/components/ui/card"

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
  if (!report || !report.content) {
    return null
  }

  return (
    <motion.div
      initial={{ opacity: 0, y: 20 }}
      animate={{ opacity: 1, y: 0 }}
      transition={{ duration: 0.4, delay: 0.5 }}
    >
      <Card className="border-l-4 border-l-[#2C3E50]">
        <CardHeader>
          <CardTitle className="flex items-center gap-2">
            <span className="text-2xl">📄</span>
            {report.title || "研究报告"}
          </CardTitle>
        </CardHeader>
        <CardContent>
          <div className="prose prose-sm max-w-none">
            <div className="text-[#2C3E50]/80 leading-relaxed whitespace-pre-wrap">
              {report.content}
            </div>
          </div>
        </CardContent>
      </Card>
    </motion.div>
  )
}