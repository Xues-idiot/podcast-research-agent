'use client'

import { useState, useEffect, useCallback } from 'react'
import { motion, AnimatePresence } from 'motion/react'
import { Card, CardContent } from '@/components/ui/card'
import { Mic, History, MessageCircle, Trash2, ExternalLink, ArrowLeft } from 'lucide-react'
import { ThemeToggle } from '@/components/ThemeToggle'
import { getConversations, deleteConversation as deleteConversationApi } from '@/lib/api'
import { API_BASE } from '@/lib/api'

interface Task {
  task_id: string
  url: string
  status: string
  created_at: string
}

interface Conversation {
  id: string
  created_at: string
  message_count: number
}

export default function HistoryPage() {
  const [tasks, setTasks] = useState<Task[]>([])
  const [conversations, setConversations] = useState<Conversation[]>([])
  const [activeTab, setActiveTab] = useState<'research' | 'chat'>('research')
  const [loading, setLoading] = useState(true)

  useEffect(() => {
    loadData()
  }, [activeTab])

  const loadData = useCallback(async () => {
    setLoading(true)
    try {
      if (activeTab === 'research') {
        const res = await fetch(`${API_BASE}/research/tasks`)
        if (!res.ok) throw new Error('Failed to fetch tasks')
        const data = await res.json()
        setTasks(data.tasks || [])
      } else {
        const conversations = await getConversations()
        setConversations(conversations)
      }
    } catch (error) {
      console.error('Failed to load data:', error)
    } finally {
      setLoading(false)
    }
  }, [activeTab])

  const deleteTask = async (taskId: string) => {
    if (!confirm('确定要删除这个研究记录吗？')) return

    try {
      await fetch(`${API_BASE}/research/${taskId}`, { method: 'DELETE' })
      loadData()
    } catch (error) {
      console.error('Failed to delete:', error)
    }
  }

  const handleDeleteConversation = async (convId: string) => {
    if (!confirm('确定要删除这个对话记录吗？')) return

    try {
      await deleteConversationApi(convId)
      loadData()
    } catch (error) {
      console.error('Failed to delete:', error)
    }
  }

  const formatDate = (dateStr: string) => {
    const date = new Date(dateStr)
    return date.toLocaleString()
  }

  const getStatusColor = (status: string) => {
    switch (status) {
      case 'completed':
        return 'bg-green-100 text-green-700 border-green-200'
      case 'failed':
        return 'bg-red-100 text-red-700 border-red-200'
      case 'running':
        return 'bg-blue-100 text-blue-700 border-blue-200'
      default:
        return 'bg-yellow-100 text-yellow-700 border-yellow-200'
    }
  }

  return (
    <div className="min-h-screen bg-[#FAF8F5]">
      {/* Header */}
      <header className="bg-white border-b border-[#2C3E50]/10">
        <div className="max-w-5xl mx-auto px-6 py-4">
          <div className="flex items-center justify-between">
            <div className="flex items-center gap-3">
              <a href="/podcast" className="flex items-center gap-2 text-[#2C3E50]/60 hover:text-[#E67E22] transition-colors">
                <ArrowLeft className="w-4 h-4" />
                <span className="text-sm">返回研究</span>
              </a>
            </div>
            <nav className="flex items-center gap-4">
              <ThemeToggle />
              <a href="/podcast" className="text-sm font-medium text-gray-600 hover:text-[#E67E22]">研究</a>
              <a href="/knowledge" className="text-sm font-medium text-gray-600 hover:text-[#E67E22]">知识库</a>
              <a href="/export" className="text-sm font-medium text-gray-600 hover:text-[#E67E22]">导出</a>
              <a href="/history" className="text-sm font-medium text-[#2C3E50] hover:text-[#E67E22]">历史</a>
            </nav>
          </div>
        </div>
      </header>

      <main className="max-w-5xl mx-auto px-6 py-8">
        <motion.div
          initial={{ opacity: 0, y: 20 }}
          animate={{ opacity: 1, y: 0 }}
          className="mb-8"
        >
          <h1 className="text-2xl font-bold text-[#2C3E50] flex items-center gap-2">
            <History className="w-6 h-6 text-[#E67E22]" />
            历史记录
          </h1>
          <p className="text-[#2C3E50]/60 mt-1">管理研究历史和对话记录</p>
        </motion.div>

        {/* Tabs */}
        <motion.div
          initial={{ opacity: 0, y: 20 }}
          animate={{ opacity: 1, y: 0 }}
          transition={{ delay: 0.1 }}
        >
          <Card className="mb-6">
            <CardContent className="p-0">
              <div className="flex border-b border-[#2C3E50]/10">
                <button
                  onClick={() => setActiveTab('research')}
                  className={`flex-1 px-6 py-4 font-medium text-center transition-colors flex items-center justify-center gap-2 ${
                    activeTab === 'research'
                      ? 'text-[#E67E22] border-b-2 border-b-[#E67E22]'
                      : 'text-[#2C3E50]/50 hover:text-[#2C3E50]'
                  }`}
                >
                  <Mic className="w-4 h-4" />
                  研究历史 ({tasks.length})
                </button>
                <button
                  onClick={() => setActiveTab('chat')}
                  className={`flex-1 px-6 py-4 font-medium text-center transition-colors flex items-center justify-center gap-2 ${
                    activeTab === 'chat'
                      ? 'text-[#E67E22] border-b-2 border-b-[#E67E22]'
                      : 'text-[#2C3E50]/50 hover:text-[#2C3E50]'
                  }`}
                >
                  <MessageCircle className="w-4 h-4" />
                  对话历史 ({conversations.length})
                </button>
              </div>
            </CardContent>
          </Card>
        </motion.div>

        {/* Content */}
        <AnimatePresence mode="wait">
          <motion.div
            key={activeTab}
            initial={{ opacity: 0, y: 10 }}
            animate={{ opacity: 1, y: 0 }}
            transition={{ duration: 0.2 }}
          >
            <Card>
              <CardContent className="p-0">
                {loading ? (
                  <div className="p-8 text-center text-[#2C3E50]/50">加载中...</div>
                ) : activeTab === 'research' ? (
                  tasks.length === 0 ? (
                    <div className="p-8 text-center text-[#2C3E50]/50">
                      暂无研究历史，<a href="/podcast" className="text-[#E67E22] hover:underline">开始研究</a>
                    </div>
                  ) : (
                    <div className="divide-y divide-[#2C3E50]/10">
                      {tasks.map((task) => (
                        <div key={task.task_id} className="p-4 hover:bg-[#FAF8F5] transition-colors">
                          <div className="flex items-start justify-between">
                            <div className="flex-1 min-w-0">
                              <div className="font-medium text-[#2C3E50] truncate">
                                {task.url}
                              </div>
                              <div className="flex items-center gap-3 mt-2">
                                <span
                                  className={`text-xs px-2 py-0.5 rounded-full border ${getStatusColor(task.status)}`}
                                >
                                  {task.status}
                                </span>
                                <span className="text-sm text-[#2C3E50]/50">
                                  {formatDate(task.created_at)}
                                </span>
                              </div>
                            </div>
                            <div className="flex items-center gap-2 ml-4">
                              {task.status === 'completed' && (
                                <a
                                  href={`/podcast?task=${task.task_id}`}
                                  className="flex items-center gap-1 text-[#E67E22] hover:text-[#D35400] text-sm"
                                >
                                  <ExternalLink className="w-4 h-4" />
                                  查看
                                </a>
                              )}
                              <button
                                onClick={() => deleteTask(task.task_id)}
                                className="flex items-center gap-1 text-red-500 hover:text-red-600 text-sm"
                              >
                                <Trash2 className="w-4 h-4" />
                                删除
                              </button>
                            </div>
                          </div>
                        </div>
                      ))}
                    </div>
                  )
                ) : conversations.length === 0 ? (
                  <div className="p-8 text-center text-[#2C3E50]/50">
                    暂无对话历史，<a href="/podcast" className="text-[#E67E22] hover:underline">开始研究</a>
                  </div>
                ) : (
                  <div className="divide-y divide-[#2C3E50]/10">
                    {conversations.map((conv) => (
                      <div key={conv.id} className="p-4 hover:bg-[#FAF8F5] transition-colors">
                        <div className="flex items-start justify-between">
                          <div className="flex-1">
                            <div className="font-medium text-[#2C3E50]">
                              对话 {conv.id.slice(0, 8)}...
                            </div>
                            <div className="flex items-center gap-3 mt-2">
                              <span className="text-sm text-[#2C3E50]/50">
                                {conv.message_count} 条消息
                              </span>
                              <span className="text-sm text-[#2C3E50]/50">
                                {formatDate(conv.created_at)}
                              </span>
                            </div>
                          </div>
                          <div className="flex items-center gap-2 ml-4">
                            <a
                              href={`/podcast?conversation=${conv.id}`}
                              className="flex items-center gap-1 text-[#E67E22] hover:text-[#D35400] text-sm"
                            >
                              <ExternalLink className="w-4 h-4" />
                              继续
                            </a>
                            <button
                              onClick={() => handleDeleteConversation(conv.id)}
                              className="flex items-center gap-1 text-red-500 hover:text-red-600 text-sm"
                            >
                              <Trash2 className="w-4 h-4" />
                              删除
                            </button>
                          </div>
                        </div>
                      </div>
                    ))}
                  </div>
                )}
              </CardContent>
            </Card>
          </motion.div>
        </AnimatePresence>
      </main>
    </div>
  )
}
