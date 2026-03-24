"use client"

import { useState } from "react"
import { motion, AnimatePresence } from "motion/react"
import { Card, CardHeader, CardTitle, CardContent } from "@/components/ui/card"
import { MessageCircle, ChevronDown, ChevronUp, Brain, Clock, Star } from "lucide-react"

interface QAPair {
  question: string
  answer: string
  type?: string
  level?: string
  level_name?: string
  knowledge_point?: string
  estimated_time?: string
  scoring_hint?: string
}

// Bloom's taxonomy level colors
const levelColors: Record<string, string> = {
  "L1": "bg-blue-100 text-blue-700",
  "L2": "bg-green-100 text-green-700",
  "L3": "bg-yellow-100 text-yellow-700",
  "L4": "bg-orange-100 text-orange-700",
  "L5": "bg-red-100 text-red-700",
  "L6": "bg-purple-100 text-purple-700",
}

interface QAPairsProps {
  qaPairs: QAPair[]
}

export function QAPairs({ qaPairs }: QAPairsProps) {
  const [openIndex, setOpenIndex] = useState<number | null>(null)

  const toggle = (index: number) => {
    setOpenIndex(openIndex === index ? null : index)
  }

  return (
    <motion.div
      initial={{ opacity: 0, y: 20 }}
      animate={{ opacity: 1, y: 0 }}
      transition={{ duration: 0.4, delay: 0.3 }}
    >
      <Card className="border-l-4 border-l-[#E67E22]">
        <CardHeader>
          <CardTitle className="flex items-center justify-between">
            <span className="flex items-center gap-2">
              <span className="text-2xl">❓</span>
              问答对
            </span>
            <span className="text-sm font-normal text-[#2C3E50]/50">
              {qaPairs.length} 个问题
            </span>
          </CardTitle>
        </CardHeader>
        <CardContent>
          <div className="space-y-3">
            {qaPairs.map((qa, index) => (
              <motion.div
                key={index}
                initial={{ opacity: 0, y: 10 }}
                animate={{ opacity: 1, y: 0 }}
                transition={{ delay: index * 0.05 }}
                className="border border-[#2C3E50]/10 rounded-lg overflow-hidden"
              >
                <button
                  onClick={() => toggle(index)}
                  className="w-full flex items-center justify-between p-4 text-left hover:bg-[#FAF8F5] transition-colors"
                >
                  <div className="flex-1 pr-4">
                    <div className="flex items-center gap-2 mb-1">
                      <span className="text-[#E67E22] font-medium">Q{index + 1}.</span>
                      {qa.level && (
                        <span className={`text-xs px-2 py-0.5 rounded-full font-medium ${levelColors[qa.level] || "bg-gray-100 text-gray-700"}`}>
                          {qa.level} {qa.level_name || ""}
                        </span>
                      )}
                      {qa.knowledge_point && (
                        <span className="text-xs px-2 py-0.5 rounded-full bg-[#2C3E50]/10 text-[#2C3E50]">
                          {qa.knowledge_point}
                        </span>
                      )}
                    </div>
                    <span className="font-medium text-[#2C3E50]">
                      {qa.question}
                    </span>
                  </div>
                  {openIndex === index ? (
                    <ChevronUp className="w-5 h-5 text-[#2C3E50]/50 flex-shrink-0" />
                  ) : (
                    <ChevronDown className="w-5 h-5 text-[#2C3E50]/50 flex-shrink-0" />
                  )}
                </button>

                <AnimatePresence>
                  {openIndex === index && (
                    <motion.div
                      initial={{ height: 0, opacity: 0 }}
                      animate={{ height: "auto", opacity: 1 }}
                      exit={{ height: 0, opacity: 0 }}
                      transition={{ duration: 0.2 }}
                      className="overflow-hidden"
                    >
                      <div className="p-4 bg-[#FAF8F5] border-t border-[#2C3E50]/10 space-y-3">
                        <div className="flex items-start gap-2">
                          <MessageCircle className="w-4 h-4 text-[#E67E22] mt-1 flex-shrink-0" />
                          <span className="text-[#2C3E50]/80 leading-relaxed">
                            {qa.answer}
                          </span>
                        </div>

                        {qa.scoring_hint && (
                          <div className="flex items-start gap-2">
                            <Star className="w-4 h-4 text-[#E67E22] mt-1 flex-shrink-0" />
                            <span className="text-sm text-[#2C3E50]/60">
                              评分提示：{qa.scoring_hint}
                            </span>
                          </div>
                        )}

                        {qa.estimated_time && (
                          <div className="flex items-center gap-2 text-sm text-[#2C3E50]/50">
                            <Clock className="w-4 h-4" />
                            <span>预计时间：{qa.estimated_time}</span>
                          </div>
                        )}
                      </div>
                    </motion.div>
                  )}
                </AnimatePresence>
              </motion.div>
            ))}
          </div>
        </CardContent>
      </Card>
    </motion.div>
  )
}