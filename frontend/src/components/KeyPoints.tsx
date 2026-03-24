"use client"

import { motion } from "motion/react"
import { Card, CardHeader, CardTitle, CardContent } from "@/components/ui/card"
import type { ResearchResult } from "@/lib/api"

interface KeyPointsProps {
  keypoints: ResearchResult["keypoints"]
}

const importanceColors = {
  high: "bg-red-100 text-red-700 border-red-200",
  medium: "bg-yellow-100 text-yellow-700 border-yellow-200",
  low: "bg-green-100 text-green-700 border-green-200",
}

export function KeyPoints({ keypoints }: KeyPointsProps) {
  return (
    <motion.div
      initial={{ opacity: 0, y: 20 }}
      animate={{ opacity: 1, y: 0 }}
      transition={{ duration: 0.4, delay: 0.2 }}
    >
      <Card className="border-l-4 border-l-[#E67E22]">
        <CardHeader>
          <CardTitle className="flex items-center gap-2">
            <span className="text-2xl">🎯</span>
            关键要点 ({keypoints.length})
          </CardTitle>
        </CardHeader>
        <CardContent>
          <div className="space-y-4">
            {keypoints.map((point, index) => (
              <motion.div
                key={point.id}
                initial={{ opacity: 0, y: 10 }}
                animate={{ opacity: 1, y: 0 }}
                transition={{ duration: 0.3, delay: 0.3 + index * 0.1 }}
                className="flex items-start gap-3 p-3 rounded-lg bg-[#FAF8F5] hover:bg-[#F5F5DC]/30 transition-colors"
              >
                <span className="flex-shrink-0 w-8 h-8 rounded-full bg-[#2C3E50] text-white flex items-center justify-center font-bold text-sm">
                  {point.id}
                </span>
                <div className="flex-1">
                  <p className="text-[#2C3E50] font-medium">{point.content}</p>
                  <span
                    className={`inline-block mt-1 px-2 py-0.5 text-xs rounded-full border ${
                      importanceColors[point.importance as keyof typeof importanceColors] || importanceColors.medium
                    }`}
                  >
                    {point.importance === "high" ? "高重要性" : point.importance === "low" ? "低重要性" : "中等重要性"}
                  </span>
                </div>
              </motion.div>
            ))}
          </div>
        </CardContent>
      </Card>
    </motion.div>
  )
}
