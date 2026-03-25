"use client"

import { useState } from "react"
import { motion } from "motion/react"
import { Card, CardHeader, CardTitle, CardContent } from "@/components/ui/card"
import type { ResearchResult } from "@/lib/api"
import { Link2, ExternalLink, ChevronDown, ChevronUp, Globe, BookOpen } from "lucide-react"

interface KnowledgeCardsProps {
  knowledgeCards: ResearchResult["knowledge_cards"]
}

export function KnowledgeCards({ knowledgeCards }: KnowledgeCardsProps) {
  const [expandedCards, setExpandedCards] = useState<Set<number>>(new Set())

  if (!knowledgeCards || knowledgeCards.length === 0) {
    return null
  }

  const toggleCard = (index: number) => {
    setExpandedCards((prev) => {
      const next = new Set(prev)
      if (next.has(index)) {
        next.delete(index)
      } else {
        next.add(index)
      }
      return next
    })
  }

  const getConfidenceColor = (confidence: number) => {
    if (confidence >= 0.8) return "bg-green-500"
    if (confidence >= 0.5) return "bg-yellow-500"
    return "bg-red-500"
  }

  const getConfidenceLabel = (confidence: number) => {
    if (confidence >= 0.8) return "高置信度"
    if (confidence >= 0.5) return "中置信度"
    return "低置信度"
  }

  return (
    <motion.div
      initial={{ opacity: 0, y: 20 }}
      animate={{ opacity: 1, y: 0 }}
      transition={{ duration: 0.4, delay: 0.35 }}
    >
      <Card className="border-l-4 border-l-[#34495E]">
        <CardHeader>
          <CardTitle className="flex items-center gap-2">
            <Link2 className="w-5 h-5 text-[#2C3E50]" />
            相关知识 ({knowledgeCards.length})
          </CardTitle>
        </CardHeader>
        <CardContent>
          <div className="space-y-3">
            {knowledgeCards.map((card, index) => {
              const isExpanded = expandedCards.has(index)
              const relatedCount = card.related?.length || 0

              return (
                <motion.div
                  key={index}
                  initial={{ opacity: 0, y: 10 }}
                  animate={{ opacity: 1, y: 0 }}
                  transition={{ delay: 0.4 + index * 0.08 }}
                  className="rounded-lg border border-[#2C3E50]/10 overflow-hidden"
                >
                  {/* Header - always visible */}
                  <button
                    onClick={() => toggleCard(index)}
                    className="w-full flex items-start gap-3 p-3 hover:bg-[#FAF8F5] transition-colors text-left"
                  >
                    <div className="flex-1 min-w-0">
                      <p className="text-sm font-medium text-[#2C3E50] line-clamp-2">
                        {card.keypoint}
                      </p>

                      {/* Confidence bar */}
                      {card.confidence > 0 && (
                        <div className="flex items-center gap-2 mt-2">
                          <div className="flex-1 h-1.5 bg-[#2C3E50]/10 rounded-full overflow-hidden">
                            <motion.div
                              initial={{ width: 0 }}
                              animate={{ width: `${card.confidence * 100}%` }}
                              transition={{ delay: 0.5 + index * 0.1, duration: 0.5 }}
                              className={`h-full ${getConfidenceColor(card.confidence)}`}
                            />
                          </div>
                          <span className="text-xs text-[#2C3E50]/50 w-16">
                            {getConfidenceLabel(card.confidence)}
                          </span>
                        </div>
                      )}
                    </div>

                    {/* Expand indicator */}
                    {relatedCount > 0 && (
                      <div className="flex items-center gap-1 text-xs text-[#2C3E50]/40">
                        {isExpanded ? (
                          <ChevronUp className="w-4 h-4" />
                        ) : (
                          <ChevronDown className="w-4 h-4" />
                        )}
                        <span>{relatedCount}</span>
                      </div>
                    )}
                  </button>

                  {/* Expanded content */}
                  {isExpanded && card.related && card.related.length > 0 && (
                    <motion.div
                      initial={{ height: 0, opacity: 0 }}
                      animate={{ height: "auto", opacity: 1 }}
                      exit={{ height: 0, opacity: 0 }}
                      transition={{ duration: 0.2 }}
                      className="border-t border-[#2C3E50]/10 bg-[#FAF8F5]"
                    >
                      <div className="p-3 space-y-2">
                        <div className="flex items-center gap-2 text-xs text-[#2C3E50]/60 mb-2">
                          <BookOpen className="w-3.5 h-3.5" />
                          <span>相关资料</span>
                        </div>
                        {card.related.map((item, itemIndex) => (
                          <a
                            key={itemIndex}
                            href={item.url}
                            target="_blank"
                            rel="noopener noreferrer"
                            className="flex items-center gap-2 p-2 rounded bg-white hover:bg-[#E67E22]/5 transition-colors group"
                          >
                            <Globe className="w-4 h-4 text-[#2C3E50]/40 flex-shrink-0" />
                            <span className="flex-1 text-sm text-[#2C3E50] group-hover:text-[#E67E22] line-clamp-1">
                              {item.title}
                            </span>
                            <ExternalLink className="w-3.5 h-3.5 text-[#2C3E50]/30 group-hover:text-[#E67E22]" />
                          </a>
                        ))}
                      </div>
                    </motion.div>
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
