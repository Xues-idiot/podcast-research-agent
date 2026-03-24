"use client"

import { motion } from "motion/react"
import { Card, CardHeader, CardTitle, CardContent } from "@/components/ui/card"
import { AlertCircle, RefreshCw, Home } from "lucide-react"

interface ErrorDisplayProps {
  error: string
  onRetry?: (url?: string) => void
  onHome?: () => void
}

export function ErrorDisplay({ error, onRetry, onHome }: ErrorDisplayProps) {
  return (
    <motion.div
      initial={{ opacity: 0, scale: 0.95 }}
      animate={{ opacity: 1, scale: 1 }}
      transition={{ duration: 0.3 }}
    >
      <Card className="border-l-4 border-l-red-500 bg-red-50/50">
        <CardHeader>
          <CardTitle className="flex items-center gap-2 text-red-600">
            <AlertCircle className="w-5 h-5" />
            出错了
          </CardTitle>
        </CardHeader>
        <CardContent>
          <p className="text-[#2C3E50]/80 mb-4">{error}</p>
          <div className="flex gap-3">
            {onRetry && (
              <button
                onClick={() => onRetry()}
                className="flex items-center gap-2 px-4 py-2 bg-[#2C3E50] text-white rounded-lg hover:bg-[#34495E] transition-colors"
              >
                <RefreshCw className="w-4 h-4" />
                重试
              </button>
            )}
            {onHome && (
              <button
                onClick={onHome}
                className="flex items-center gap-2 px-4 py-2 bg-[#E67E22] text-white rounded-lg hover:bg-[#D35400] transition-colors"
              >
                <Home className="w-4 h-4" />
                返回首页
              </button>
            )}
          </div>
        </CardContent>
      </Card>
    </motion.div>
  )
}