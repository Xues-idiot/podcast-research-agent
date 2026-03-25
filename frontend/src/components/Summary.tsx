"use client"

import { useState } from "react"
import { motion } from "motion/react"
import { Card, CardHeader, CardTitle, CardContent } from "@/components/ui/card"
import type { ResearchResult } from "@/lib/api"
import { Sparkles, Copy, Check, Quote, MessageSquare } from "lucide-react"

interface SummaryProps {
  summary: ResearchResult["summary"]
}

export function Summary({ summary }: SummaryProps) {
  const [copied, setCopied] = useState(false)

  const copyToClipboard = async () => {
    try {
      const text = `${summary.title || "播客摘要"}\n\n${summary.summary}\n\n亮点:\n${summary.highlights?.map(h => `• ${h}`).join("\n") || ""}`
      await navigator.clipboard.writeText(text)
      setCopied(true)
      setTimeout(() => setCopied(false), 2000)
    } catch (err) {
      console.error("Failed to copy:", err)
    }
  }

  return (
    <motion.div
      initial={{ opacity: 0, y: 20 }}
      animate={{ opacity: 1, y: 0 }}
      transition={{ duration: 0.4, delay: 0.1 }}
    >
      <Card className="border-l-4 border-l-[#2C3E50]">
        <CardHeader>
          <div className="flex items-center justify-between">
            <CardTitle className="flex items-center gap-2">
              <Sparkles className="w-5 h-5 text-[#E67E22]" />
              {summary.title || "内容摘要"}
            </CardTitle>
            <button
              onClick={copyToClipboard}
              className="p-2 rounded-lg hover:bg-[#2C3E50]/10 transition-colors"
              title="复制摘要"
            >
              {copied ? (
                <Check className="w-4 h-4 text-green-500" />
              ) : (
                <Copy className="w-4 h-4 text-[#2C3E50]/50" />
              )}
            </button>
          </div>
        </CardHeader>
        <CardContent className="space-y-6">
          {/* Main summary */}
          <div className="relative">
            <Quote className="absolute -left-2 -top-2 w-8 h-8 text-[#E67E22]/10" />
            <p className="text-[#2C3E50]/80 leading-relaxed pl-4 text-lg">
              {summary.summary}
            </p>
          </div>

          {/* Highlights */}
          {summary.highlights && summary.highlights.length > 0 && (
            <div className="bg-[#FAF8F5] rounded-lg p-4">
              <div className="flex items-center gap-2 mb-3">
                <MessageSquare className="w-4 h-4 text-[#E67E22]" />
                <h4 className="font-semibold text-[#2C3E50]">亮点</h4>
              </div>
              <ul className="space-y-2">
                {summary.highlights.map((highlight, index) => (
                  <motion.li
                    key={index}
                    initial={{ opacity: 0, x: -10 }}
                    animate={{ opacity: 1, x: 0 }}
                    transition={{ duration: 0.3, delay: 0.2 + index * 0.1 }}
                    className="flex items-start gap-2"
                  >
                    <span className="text-[#E67E22] font-bold mt-1">•</span>
                    <span className="text-[#2C3E50]/80 flex-1">{highlight}</span>
                  </motion.li>
                ))}
              </ul>
            </div>
          )}
        </CardContent>
      </Card>
    </motion.div>
  )
}
