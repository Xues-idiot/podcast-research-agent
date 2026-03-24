"use client"

import { motion } from "motion/react"
import { Card, CardContent } from "@/components/ui/card"
import { Loader2, CheckCircle2, Circle } from "lucide-react"

interface ProgressProps {
  currentStep: string
  progress: number
}

const steps = [
  { key: "download", label: "下载音视频" },
  { key: "transcribe", label: "转录中" },
  { key: "summarize", label: "生成摘要" },
  { key: "keypoint", label: "提取要点" },
  { key: "mindmap", label: "生成思维导图" },
  { key: "link", label: "关联知识" },
  { key: "report", label: "生成报告" },
  { key: "qa", label: "生成问答" },
]

export function Progress({ currentStep, progress }: ProgressProps) {
  const currentIndex = steps.findIndex((s) => s.key === currentStep) || 0

  return (
    <motion.div
      initial={{ opacity: 0, y: 20 }}
      animate={{ opacity: 1, y: 0 }}
      transition={{ duration: 0.4 }}
    >
      <Card className="border-l-4 border-l-[#E67E22]">
        <CardContent className="pt-6">
          {/* 进度条 */}
          <div className="mb-6">
            <div className="h-2 bg-[#2C3E50]/10 rounded-full overflow-hidden">
              <motion.div
                initial={{ width: 0 }}
                animate={{ width: `${progress}%` }}
                transition={{ duration: 0.5 }}
                className="h-full bg-gradient-to-r from-[#2C3E50] to-[#E67E22]"
              />
            </div>
            <p className="text-center mt-2 text-sm text-[#2C3E50]/70">
              {progress.toFixed(0)}%
            </p>
          </div>

          {/* 步骤列表 */}
          <div className="space-y-3">
            {steps.map((step, index) => {
              const isComplete = index < currentIndex
              const isCurrent = index === currentIndex

              return (
                <motion.div
                  key={step.key}
                  initial={{ opacity: 0, x: -20 }}
                  animate={{ opacity: 1, x: 0 }}
                  transition={{ delay: index * 0.1 }}
                  className="flex items-center gap-3"
                >
                  {isComplete ? (
                    <CheckCircle2 className="w-5 h-5 text-green-500" />
                  ) : isCurrent ? (
                    <Loader2 className="w-5 h-5 text-[#E67E22] animate-spin" />
                  ) : (
                    <Circle className="w-5 h-5 text-[#2C3E50]/30" />
                  )}

                  <span
                    className={`text-sm ${
                      isCurrent
                        ? "text-[#E67E22] font-medium"
                        : isComplete
                        ? "text-green-600"
                        : "text-[#2C3E50]/50"
                    }`}
                  >
                    {step.label}
                  </span>

                  {isCurrent && (
                    <motion.span
                      animate={{ opacity: [1, 0, 1] }}
                      transition={{ duration: 1.5, repeat: Infinity }}
                      className="text-xs text-[#E67E22]"
                    >
                      进行中...
                    </motion.span>
                  )}
                </motion.div>
              )
            })}
          </div>
        </CardContent>
      </Card>
    </motion.div>
  )
}
