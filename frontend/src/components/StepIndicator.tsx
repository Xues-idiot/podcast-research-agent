"use client"

import { motion } from "motion/react"
import { Download, FileText, Sparkles, List, Network, Link2, FileCheck, MessageCircle, CheckCircle2 } from "lucide-react"

interface Step {
  id: string
  label: string
  icon: React.ReactNode
}

interface StepIndicatorProps {
  currentStep: string
  progress: number
}

const steps: Step[] = [
  { id: "download", label: "下载", icon: <Download className="w-4 h-4" /> },
  { id: "transcribe", label: "转录", icon: <FileText className="w-4 h-4" /> },
  { id: "summarize", label: "摘要", icon: <Sparkles className="w-4 h-4" /> },
  { id: "keypoint", label: "要点", icon: <List className="w-4 h-4" /> },
  { id: "mindmap", label: "导图", icon: <Network className="w-4 h-4" /> },
  { id: "link", label: "链接", icon: <Link2 className="w-4 h-4" /> },
  { id: "report", label: "报告", icon: <FileCheck className="w-4 h-4" /> },
  { id: "qa", label: "问答", icon: <MessageCircle className="w-4 h-4" /> },
]

const stepOrder = steps.map((s) => s.id)

export function StepIndicator({ currentStep, progress }: StepIndicatorProps) {
  const currentIndex = stepOrder.indexOf(currentStep)

  return (
    <motion.div
      initial={{ opacity: 0, y: 20 }}
      animate={{ opacity: 1, y: 0 }}
      className="bg-white rounded-xl p-4 border border-[#2C3E50]/10"
    >
      <div className="flex items-center justify-between mb-4">
        <h3 className="text-sm font-medium text-[#2C3E50]">研究进度</h3>
        <span className="text-sm font-bold text-[#E67E22]">{progress}%</span>
      </div>

      <div className="relative">
        {/* Progress line background */}
        <div className="absolute top-5 left-0 right-0 h-0.5 bg-[#2C3E50]/10" />

        {/* Progress line active */}
        <motion.div
          className="absolute top-5 left-0 h-0.5 bg-[#E67E22]"
          initial={{ width: 0 }}
          animate={{ width: `${(currentIndex / (steps.length - 1)) * 100}%` }}
          transition={{ duration: 0.3 }}
        />

        {/* Step circles */}
        <div className="relative flex justify-between">
          {steps.map((step, index) => {
            const isCompleted = index < currentIndex
            const isCurrent = index === currentIndex
            const isPending = index > currentIndex

            return (
              <motion.div
                key={step.id}
                initial={{ scale: 0.8, opacity: 0 }}
                animate={{ scale: 1, opacity: 1 }}
                transition={{ delay: index * 0.1 }}
                className="flex flex-col items-center"
              >
                <div
                  className={`
                    w-10 h-10 rounded-full flex items-center justify-center
                    transition-all duration-300
                    ${
                      isCompleted
                        ? "bg-[#2C3E50] text-white"
                        : isCurrent
                        ? "bg-[#E67E22] text-white ring-4 ring-[#E67E22]/20"
                        : "bg-[#2C3E50]/10 text-[#2C3E50]/30"
                    }
                  `}
                >
                  {isCompleted ? (
                    <CheckCircle2 className="w-5 h-5" />
                  ) : (
                    step.icon
                  )}
                </div>
                <span
                  className={`
                    text-xs mt-2 transition-colors
                    ${
                      isCurrent
                        ? "text-[#E67E22] font-medium"
                        : isCompleted
                        ? "text-[#2C3E50]"
                        : "text-[#2C3E50]/40"
                    }
                  `}
                >
                  {step.label}
                </span>
              </motion.div>
            )
          })}
        </div>
      </div>
    </motion.div>
  )
}