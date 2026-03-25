"use client"

import { useState } from "react"
import { motion, AnimatePresence } from "motion/react"
import { Card, CardHeader, CardTitle, CardContent } from "@/components/ui/card"
import type { ResearchResult } from "@/lib/api"
import { ChevronDown, ChevronRight, Brain, ZoomIn, ZoomOut, Maximize2 } from "lucide-react"

interface MindMapProps {
  mindmap: ResearchResult["mindmap"]
}

export function MindMap({ mindmap }: MindMapProps) {
  const [expandedBranches, setExpandedBranches] = useState<Set<number>>(
    new Set(mindmap.branches.map((_, i) => i))
  )
  const [isFullscreen, setIsFullscreen] = useState(false)

  const allExpanded = expandedBranches.size === mindmap.branches.length

  const toggleBranch = (index: number) => {
    setExpandedBranches((prev) => {
      const next = new Set(prev)
      if (next.has(index)) {
        next.delete(index)
      } else {
        next.add(index)
      }
      return next
    })
  }

  const toggleAll = () => {
    if (allExpanded) {
      setExpandedBranches(new Set())
    } else {
      setExpandedBranches(new Set(mindmap.branches.map((_, i) => i)))
    }
  }

  return (
    <motion.div
      initial={{ opacity: 0, y: 20 }}
      animate={{ opacity: 1, y: 0 }}
      transition={{ duration: 0.4, delay: 0.3 }}
    >
      <Card className={`border-l-4 border-l-[#F5F5DC] ${isFullscreen ? "fixed inset-4 z-50 overflow-auto" : ""}`}>
        <CardHeader>
          <CardTitle className="flex items-center justify-between">
            <span className="flex items-center gap-2">
              <Brain className="w-6 h-6 text-[#2C3E50]" />
              思维导图
            </span>
            <div className="flex items-center gap-1">
              <button
                onClick={toggleAll}
                className="text-xs px-2 py-1 rounded bg-[#2C3E50]/10 hover:bg-[#2C3E50]/20 text-[#2C3E50] transition-colors"
              >
                {allExpanded ? "收起全部" : "展开全部"}
              </button>
              <button
                onClick={() => setIsFullscreen(!isFullscreen)}
                className="p-2 rounded-lg hover:bg-[#2C3E50]/10 transition-colors"
                title={isFullscreen ? "退出全屏" : "全屏查看"}
              >
                <Maximize2 className="w-4 h-4 text-[#2C3E50]/50" />
              </button>
            </div>
          </CardTitle>
        </CardHeader>
        <CardContent>
          <div className="space-y-3">
            {/* 根节点 */}
            <motion.div
              initial={{ scale: 0.9 }}
              animate={{ scale: 1 }}
              className="flex items-center justify-center p-4 bg-gradient-to-br from-[#2C3E50] to-[#34495E] text-white rounded-xl font-semibold text-lg shadow-lg"
            >
              <Brain className="w-6 h-6 mr-2 opacity-70" />
              {mindmap.root || "主题"}
            </motion.div>

            {/* 分支 */}
            <div className="ml-4 md:ml-8 space-y-2 border-l-2 border-[#2C3E50]/20 pl-4">
              {mindmap.branches.map((branch, index) => {
                const isExpanded = expandedBranches.has(index)

                return (
                  <div key={index}>
                    {/* 分支标题 */}
                    <motion.button
                      initial={{ opacity: 0 }}
                      animate={{ opacity: 1 }}
                      transition={{ delay: 0.4 + index * 0.1 }}
                      onClick={() => toggleBranch(index)}
                      className="flex items-center gap-2 w-full text-left p-2 rounded-lg hover:bg-[#FAF8F5] transition-colors group"
                    >
                      <span className="text-[#E67E22]">
                        {isExpanded ? (
                          <ChevronDown className="w-4 h-4" />
                        ) : (
                          <ChevronRight className="w-4 h-4" />
                        )}
                      </span>
                      <span className="font-medium text-[#2C3E50] group-hover:text-[#E67E22] transition-colors">
                        {branch.title}
                      </span>
                      <span className="text-xs text-[#2C3E50]/40 bg-[#2C3E50]/5 px-2 py-0.5 rounded-full">
                        {branch.children?.length || 0} 项
                      </span>
                    </motion.button>

                    {/* 子节点 */}
                    <AnimatePresence>
                      {isExpanded && branch.children && (
                        <motion.div
                          initial={{ height: 0, opacity: 0 }}
                          animate={{ height: "auto", opacity: 1 }}
                          exit={{ height: 0, opacity: 0 }}
                          transition={{ duration: 0.3 }}
                          className="ml-6 space-y-1 overflow-hidden"
                        >
                          {branch.children.map((child, childIndex) => (
                            <motion.div
                              key={childIndex}
                              initial={{ opacity: 0, x: -10 }}
                              animate={{ opacity: 1, x: 0 }}
                              transition={{ delay: childIndex * 0.05 }}
                              className="flex items-center gap-2 p-2 rounded bg-[#FAF8F5] text-sm text-[#2C3E50]/80 hover:bg-[#E67E22]/5 transition-colors"
                            >
                              <span className="w-1.5 h-1.5 rounded-full bg-[#E67E22]" />
                              {child}
                            </motion.div>
                          ))}
                        </motion.div>
                      )}
                    </AnimatePresence>
                  </div>
                )
              })}
            </div>
          </div>
        </CardContent>
      </Card>

      {/* Fullscreen backdrop */}
      {isFullscreen && (
        <motion.div
          initial={{ opacity: 0 }}
          animate={{ opacity: 1 }}
          className="fixed inset-0 bg-black/20 z-40"
          onClick={() => setIsFullscreen(false)}
        />
      )}
    </motion.div>
  )
}
