"use client"

import { motion } from "motion/react"
import { Card, CardHeader, CardTitle, CardContent } from "@/components/ui/card"
import type { ResearchResult } from "@/lib/api"
import { Link2, ExternalLink } from "lucide-react"

interface KnowledgeCardsProps {
  knowledgeCards: ResearchResult["knowledge_cards"]
}

export function KnowledgeCards({ knowledgeCards }: KnowledgeCardsProps) {
  if (!knowledgeCards || knowledgeCards.length === 0) {
    return null
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
          <div className="space-y-4">
            {knowledgeCards.map((card, index) => (
              <motion.div
                key={index}
                initial={{ opacity: 0, y: 10 }}
                animate={{ opacity: 1, y: 0 }}
                transition={{ delay: 0.4 + index * 0.1 }}
                className="p-3 rounded-lg bg-[#FAF8F5] hover:bg-[#F5F5DC]/30 transition-colors"
              >
                <p className="text-sm font-medium text-[#2C3E50] mb-2">
                  {card.keypoint}
                </p>

                {card.related && card.related.length > 0 && (
                  <div className="space-y-1">
                    {card.related.slice(0, 3).map((item, itemIndex) => (
                      <a
                        key={itemIndex}
                        href={item.url}
                        target="_blank"
                        rel="noopener noreferrer"
                        className="flex items-center gap-2 text-xs text-[#E67E22] hover:underline"
                      >
                        <ExternalLink className="w-3 h-3" />
                        {item.title}
                      </a>
                    ))}
                  </div>
                )}

                {card.confidence > 0 && (
                  <div className="mt-2 flex items-center gap-2">
                    <div className="flex-1 h-1 bg-[#2C3E50]/10 rounded-full overflow-hidden">
                      <motion.div
                        initial={{ width: 0 }}
                        animate={{ width: `${card.confidence * 100}%` }}
                        transition={{ delay: 0.5 + index * 0.1 }}
                        className="h-full bg-[#E67E22]"
                      />
                    </div>
                    <span className="text-xs text-[#2C3E50]/50">
                      {card.confidence.toFixed(0)}%
                    </span>
                  </div>
                )}
              </motion.div>
            ))}
          </div>
        </CardContent>
      </Card>
    </motion.div>
  )
}
