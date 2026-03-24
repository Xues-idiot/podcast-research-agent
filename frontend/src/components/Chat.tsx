"use client"

import { useState, useRef, useEffect } from "react"
import { motion, AnimatePresence } from "motion/react"
import { Card, CardHeader, CardTitle, CardContent } from "@/components/ui/card"
import { Button } from "@/components/ui/button"
import { Input } from "@/components/ui/input"
import { Send, Bot, User, Trash2, Download } from "lucide-react"

interface Message {
  id: string
  role: "user" | "assistant"
  content: string
  timestamp: Date
}

interface ChatProps {
  researchResult: {
    transcript?: { text: string; segments?: Array<{ start: number; end: number; text: string }> }
    summary?: { title: string; summary: string; highlights?: string[] }
    keypoints?: Array<{ id: number; content: string; importance: string }>
    mindmap?: { root: string; branches: Array<{ title: string; children?: string[] }> }
  }
}

export function Chat({ researchResult: _researchResult }: ChatProps) {
  // TODO: 将 researchResult 传递给后端用于上下文检索
  // eslint-disable-next-line @typescript-eslint/no-unused-vars
  const [messages, setMessages] = useState<Message[]>([])
  const [input, setInput] = useState("")
  const [isLoading, setIsLoading] = useState(false)
  const [conversationId, setConversationId] = useState<string | null>(null)
  const messagesEndRef = useRef<HTMLDivElement>(null)

  const scrollToBottom = () => {
    messagesEndRef.current?.scrollIntoView({ behavior: "smooth" })
  }

  useEffect(() => {
    scrollToBottom()
  }, [messages])

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault()
    if (!input.trim() || isLoading) return

    const userMessage: Message = {
      id: Date.now().toString(),
      role: "user",
      content: input.trim(),
      timestamp: new Date()
    }

    setMessages(prev => [...prev, userMessage])
    setInput("")
    setIsLoading(true)

    try {
      // 调用对话API
      const response = await fetch("/api/chat/chat", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({
          query: userMessage.content,
          conversation_id: conversationId,
          stream: true
        })
      })

      if (!response.ok) {
        throw new Error("Chat request failed")
      }

      // 处理流式响应
      const reader = response.body?.getReader()
      const decoder = new TextDecoder()
      let assistantContent = ""
      let newConversationId = conversationId

      const assistantMessage: Message = {
        id: (Date.now() + 1).toString(),
        role: "assistant",
        content: "",
        timestamp: new Date()
      }

      setMessages(prev => [...prev, assistantMessage])

      while (reader) {
        const { done, value } = await reader.read()
        if (done) break

        const chunk = decoder.decode(value)
        const lines = chunk.split("\n")

        for (const line of lines) {
          if (line.startsWith("data: ")) {
            const data = line.slice(6)

            if (data.startsWith("[DONE]")) {
              newConversationId = data.replace("[DONE]", "").trim()
              setConversationId(newConversationId)
            } else if (data.startsWith("[ERROR]")) {
              throw new Error(data.replace("[ERROR]", "").trim())
            } else {
              assistantContent += data
              setMessages(prev =>
                prev.map(msg =>
                  msg.id === assistantMessage.id
                    ? { ...msg, content: assistantContent }
                    : msg
                )
              )
            }
          }
        }
      }
    } catch (error) {
      console.error("Chat error:", error)
      setMessages(prev =>
        [...prev, {
          id: (Date.now() + 1).toString(),
          role: "assistant",
          content: "抱歉，发生了错误，请稍后重试。",
          timestamp: new Date()
        }]
      )
    } finally {
      setIsLoading(false)
    }
  }

  const clearChat = () => {
    setMessages([])
    setConversationId(null)
  }

  const exportChat = async () => {
    if (!conversationId) return

    try {
      const response = await fetch(`/api/chat/conversation/${conversationId}/export?format=markdown`)
      const data = await response.json()

      const blob = new Blob([data.content], { type: "text/markdown" })
      const url = URL.createObjectURL(blob)
      const a = document.createElement("a")
      a.href = url
      a.download = data.filename
      a.click()
      URL.revokeObjectURL(url)
    } catch (error) {
      console.error("Export error:", error)
    }
  }

  return (
    <motion.div
      initial={{ opacity: 0, y: 20 }}
      animate={{ opacity: 1, y: 0 }}
      transition={{ duration: 0.4, delay: 0.5 }}
    >
      <Card className="border-l-4 border-l-[#E67E22]">
        <CardHeader>
          <CardTitle className="flex items-center justify-between">
            <span className="flex items-center gap-2">
              <Bot className="w-6 h-6 text-[#E67E22]" />
              对话问答
            </span>
            <div className="flex items-center gap-2">
              {conversationId && (
                <>
                  <Button
                    variant="ghost"
                    size="sm"
                    onClick={exportChat}
                    title="导出对话"
                  >
                    <Download className="w-4 h-4" />
                  </Button>
                  <Button
                    variant="ghost"
                    size="sm"
                    onClick={clearChat}
                    title="清空对话"
                  >
                    <Trash2 className="w-4 h-4" />
                  </Button>
                </>
              )}
            </div>
          </CardTitle>
        </CardHeader>
        <CardContent>
          <div className="flex flex-col h-96">
            {/* 消息列表 */}
            <div className="flex-1 overflow-y-auto space-y-4 mb-4">
              {messages.length === 0 ? (
                <div className="text-center text-[#2C3E50]/50 py-8">
                  <Bot className="w-12 h-12 mx-auto mb-2 opacity-50" />
                  <p>基于播客内容开始对话吧</p>
                  <p className="text-sm mt-1">可以询问关于内容的任何问题</p>
                </div>
              ) : (
                <AnimatePresence>
                  {messages.map(message => (
                    <motion.div
                      key={message.id}
                      initial={{ opacity: 0, y: 10 }}
                      animate={{ opacity: 1, y: 0 }}
                      className={`flex gap-3 ${
                        message.role === "user" ? "flex-row-reverse" : ""
                      }`}
                    >
                      <div className={`flex-shrink-0 w-8 h-8 rounded-full flex items-center justify-center ${
                        message.role === "user"
                          ? "bg-[#E67E22] text-white"
                          : "bg-[#2C3E50] text-white"
                      }`}>
                        {message.role === "user" ? (
                          <User className="w-4 h-4" />
                        ) : (
                          <Bot className="w-4 h-4" />
                        )}
                      </div>
                      <div className={`flex-1 max-w-[80%] ${
                        message.role === "user" ? "text-right" : ""
                      }`}>
                        <div className={`inline-block p-3 rounded-lg ${
                          message.role === "user"
                            ? "bg-[#E67E22]/10 text-[#2C3E50]"
                            : "bg-[#FAF8F5] text-[#2C3E50]"
                        }`}>
                          <p className="whitespace-pre-wrap">{message.content}</p>
                        </div>
                        <p className="text-xs text-[#2C3E50]/50 mt-1">
                          {message.timestamp.toLocaleTimeString()}
                        </p>
                      </div>
                    </motion.div>
                  ))}
                </AnimatePresence>
              )}
              <div ref={messagesEndRef} />
            </div>

            {/* 输入框 */}
            <form onSubmit={handleSubmit} className="flex gap-2">
              <Input
                value={input}
                onChange={(e) => setInput(e.target.value)}
                placeholder="输入问题..."
                disabled={isLoading}
                className="flex-1"
              />
              <Button
                type="submit"
                disabled={isLoading || !input.trim()}
                className="bg-[#E67E22] hover:bg-[#D35400]"
              >
                <Send className="w-4 h-4" />
              </Button>
            </form>
          </div>
        </CardContent>
      </Card>
    </motion.div>
  )
}
