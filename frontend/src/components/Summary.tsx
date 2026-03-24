"use client"

import { motion } from "motion/react"
import { Card, CardHeader, CardTitle, CardContent } from "@/components/ui/card"
import type { ResearchResult } from "@/lib/api"

interface SummaryProps {
  summary: ResearchResult["summary"]
}

export function Summary({ summary }: SummaryProps) {
  return (
    <motion.div
      initial={{ opacity: 0, y: 20 }}
      animate={{ opacity: 1, y: 0 }}
      transition={{ duration: 0.4, delay: 0.1 }}
    >
      <Card className="border-l-4 border-l-[#2C3E50]">
        <CardHeader>
          <CardTitle className="flex items-center gap-2">
            <span className="text-2xl">📝</span>
            {summary.title || "内容摘要"}
          </CardTitle>
        </CardHeader>
        <CardContent className="space-y-4">
          <p className="text-[#2C3E50]/80 leading-relaxed">
            {summary.summary}
          </p>

          {summary.highlights && summary.highlights.length > 0 && (
            <div className="mt-4">
              <h4 className="font-semibold text-[#2C3E50] mb-2">亮点</h4>
              <ul className="space-y-2">
                {summary.highlights.map((highlight, index) => (
                  <motion.li
                    key={index}
                    initial={{ opacity: 0, x: -10 }}
                    animate={{ opacity: 1, x: 0 }}
                    transition={{ duration: 0.3, delay: 0.2 + index * 0.1 }}
                    className="flex items-start gap-2"
                  >
                    <span className="text-[#E67E22] font-bold">•</span>
                    <span className="text-[#2C3E50]/80">{highlight}</span>
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
