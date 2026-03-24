"use client"

import { useCallback } from "react"
import { motion } from "motion/react"
import { usePodcastStore } from "@/store/podcast-store"
import {
  URLInput,
  Summary,
  KeyPoints,
  MindMap,
  Progress,
  Export,
  StepIndicator,
  ErrorDisplay,
  KnowledgeCards,
  ReportDisplay,
  ApiStatus,
  TranscriptPlayer,
  QAPairs,
} from "@/components"
import { streamResearch } from "@/lib/api"
import { Mic } from "lucide-react"

export default function PodcastPage() {
  const {
    status,
    result,
    error,
    progress,
    currentStep,
    url,
    setStatus,
    setError,
    setResult,
    setProgress,
    setCurrentStep,
    reset,
  } = usePodcastStore()

  const handleSubmit = useCallback(
    async (submitUrl: string) => {
      reset()
      setStatus("loading")
      setProgress(0)
      setCurrentStep("download")

      try {
        // 使用SSE流式研究
        for await (const event of streamResearch({ url: submitUrl })) {
          if (event.type === 'progress') {
            setProgress(event.progress || 0)
            if (event.step) {
              setCurrentStep(event.step)
            }
          } else if (event.type === 'complete' && event.result) {
            setProgress(100)
            setResult(event.result)
          } else if (event.type === 'error') {
            throw new Error(event.error || "研究失败")
          }
        }
      } catch (err) {
        console.error("Research error:", err)
        setError(err instanceof Error ? err.message : "研究失败")
      }
    },
    [reset, setCurrentStep, setError, setProgress, setResult, setStatus]
  )

  const handleRetry = useCallback(() => {
    if (url) {
      handleSubmit(url)
    }
  }, [url, handleSubmit])

  return (
    <div className="min-h-screen bg-[#FAF8F5]">
      {/* 头部 */}
      <header className="bg-white border-b border-[#2C3E50]/10 sticky top-0 z-10">
        <div className="max-w-5xl mx-auto px-6 py-4">
          <div className="flex items-center justify-between">
            <div className="flex items-center gap-3">
              <div className="w-10 h-10 rounded-xl bg-gradient-to-br from-[#2C3E50] to-[#34495E] flex items-center justify-center">
                <Mic className="w-5 h-5 text-white" />
              </div>
              <div>
                <h1 className="text-xl font-bold text-[#2C3E50]">Echo</h1>
                <p className="text-xs text-[#2C3E50]/60">播客研究Agent · 让知识回响</p>
              </div>
            </div>
            <ApiStatus />
          </div>
        </div>
      </header>

      {/* 主内容 */}
      <main className="max-w-5xl mx-auto px-6 py-8">
        {/* 搜索区域 */}
        <section className="mb-12">
          <motion.div
            initial={{ opacity: 0, y: 20 }}
            animate={{ opacity: 1, y: 0 }}
            transition={{ duration: 0.5 }}
            className="text-center mb-8"
          >
            <h2 className="text-3xl font-bold text-[#2C3E50] mb-3">
              输入链接，开始研究
            </h2>
            <p className="text-[#2C3E50]/70 max-w-xl mx-auto">
              支持B站、YouTube视频和播客RSS链接，自动转录、提取要点、生成摘要
            </p>
          </motion.div>

          <URLInput onSubmit={handleSubmit} />
        </section>

        {/* 结果区域 */}
        {status === "loading" && (
          <section className="mb-8">
            <StepIndicator currentStep={currentStep} progress={progress} />
          </section>
        )}

        {status === "error" && error && (
          <section className="mb-8">
            <ErrorDisplay error={error} onRetry={handleRetry} />
          </section>
        )}

        {status === "success" && result && (
          <section className="space-y-6">
            {/* 转录播放器 */}
            {result.transcript && (
              <TranscriptPlayer transcript={result.transcript} />
            )}

            {/* 摘要 */}
            {result.summary && <Summary summary={result.summary} />}

            {/* 要点 */}
            {result.keypoints && result.keypoints.length > 0 && (
              <KeyPoints keypoints={result.keypoints} />
            )}

            {/* 思维导图 */}
            {result.mindmap && result.mindmap.root && (
              <MindMap mindmap={result.mindmap} />
            )}

            {/* 知识卡片 */}
            {result.knowledge_cards && result.knowledge_cards.length > 0 && (
              <KnowledgeCards knowledgeCards={result.knowledge_cards} />
            )}

            {/* 问答对 */}
            {result.qa_pairs && result.qa_pairs.length > 0 && (
              <QAPairs qaPairs={result.qa_pairs} />
            )}

            {/* 报告 */}
            {result.report && <ReportDisplay report={result.report} />}

            {/* 导出 */}
            <Export result={result} />
          </section>
        )}

        {/* 空状态 */}
        {status === "idle" && (
          <motion.div
            initial={{ opacity: 0 }}
            animate={{ opacity: 1 }}
            transition={{ delay: 0.5 }}
            className="text-center py-16"
          >
            <div className="text-6xl mb-4">🎧</div>
            <p className="text-[#2C3E50]/50">
              输入链接后，这里将展示研究结果
            </p>
          </motion.div>
        )}
      </main>

      {/* 页脚 */}
      <footer className="border-t border-[#2C3E50]/10 bg-white mt-auto">
        <div className="max-w-5xl mx-auto px-6 py-4">
          <p className="text-center text-sm text-[#2C3E50]/50">
            Echo · 播客研究Agent · {new Date().getFullYear()}
          </p>
        </div>
      </footer>
    </div>
  )
}
