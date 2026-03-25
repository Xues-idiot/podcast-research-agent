'use client'

import { useState, useEffect } from 'react'

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

  const loadData = async () => {
    setLoading(true)
    try {
      if (activeTab === 'research') {
        const res = await fetch('/api/research/tasks')
        const data = await res.json()
        setTasks(data.tasks || [])
      } else {
        const res = await fetch('/api/chat/conversations')
        const data = await res.json()
        setConversations(data.conversations || [])
      }
    } catch (error) {
      console.error('Failed to load data:', error)
    } finally {
      setLoading(false)
    }
  }

  const deleteTask = async (taskId: string) => {
    if (!confirm('确定要删除这个研究记录吗？')) return

    try {
      await fetch(`/api/research/${taskId}`, { method: 'DELETE' })
      loadData()
    } catch (error) {
      console.error('Failed to delete:', error)
    }
  }

  const deleteConversation = async (convId: string) => {
    if (!confirm('确定要删除这个对话记录吗？')) return

    try {
      await fetch(`/api/chat/conversation/${convId}`, { method: 'DELETE' })
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
        return 'bg-green-100 text-green-700'
      case 'failed':
        return 'bg-red-100 text-red-700'
      case 'running':
        return 'bg-blue-100 text-blue-700'
      default:
        return 'bg-yellow-100 text-yellow-700'
    }
  }

  return (
    <div className="min-h-screen bg-gray-50">
      {/* Header */}
      <header className="bg-white shadow-sm border-b">
        <div className="max-w-7xl mx-auto px-4 py-4 flex items-center justify-between">
          <div className="flex items-center gap-4">
            <a href="/podcast" className="text-gray-600 hover:text-gray-900">
              &larr; 返回研究
            </a>
            <h1 className="text-2xl font-bold text-gray-900">历史记录</h1>
          </div>
        </div>
      </header>

      <main className="max-w-4xl mx-auto px-4 py-8">
        {/* Tabs */}
        <div className="bg-white rounded-lg shadow mb-6">
          <div className="flex border-b">
            <button
              onClick={() => setActiveTab('research')}
              className={`flex-1 px-6 py-4 font-medium text-center ${
                activeTab === 'research'
                  ? 'text-blue-600 border-b-2 border-blue-600'
                  : 'text-gray-500 hover:text-gray-700'
              }`}
            >
              研究历史 ({tasks.length})
            </button>
            <button
              onClick={() => setActiveTab('chat')}
              className={`flex-1 px-6 py-4 font-medium text-center ${
                activeTab === 'chat'
                  ? 'text-blue-600 border-b-2 border-blue-600'
                  : 'text-gray-500 hover:text-gray-700'
              }`}
            >
              对话历史 ({conversations.length})
            </button>
          </div>
        </div>

        {/* Content */}
        <div className="bg-white rounded-lg shadow">
          {loading ? (
            <div className="p-8 text-center text-gray-500">加载中...</div>
          ) : activeTab === 'research' ? (
            tasks.length === 0 ? (
              <div className="p-8 text-center text-gray-500">
                暂无研究历史，<a href="/podcast" className="text-blue-600 hover:underline">开始研究</a>
              </div>
            ) : (
              <div className="divide-y">
                {tasks.map((task) => (
                  <div key={task.task_id} className="p-4 hover:bg-gray-50">
                    <div className="flex items-start justify-between">
                      <div className="flex-1">
                        <div className="font-medium text-gray-900 truncate">
                          {task.url}
                        </div>
                        <div className="flex items-center gap-3 mt-2">
                          <span
                            className={`text-xs px-2 py-0.5 rounded ${getStatusColor(task.status)}`}
                          >
                            {task.status}
                          </span>
                          <span className="text-sm text-gray-500">
                            {formatDate(task.created_at)}
                          </span>
                        </div>
                      </div>
                      <div className="flex items-center gap-2">
                        {task.status === 'completed' && (
                          <a
                            href={`/podcast?task=${task.task_id}`}
                            className="text-blue-600 hover:text-blue-700 text-sm"
                          >
                            查看
                          </a>
                        )}
                        <button
                          onClick={() => deleteTask(task.task_id)}
                          className="text-red-600 hover:text-red-700 text-sm"
                        >
                          删除
                        </button>
                      </div>
                    </div>
                  </div>
                ))}
              </div>
            )
          ) : conversations.length === 0 ? (
            <div className="p-8 text-center text-gray-500">
              暂无对话历史，<a href="/podcast" className="text-blue-600 hover:underline">开始研究</a>
            </div>
          ) : (
            <div className="divide-y">
              {conversations.map((conv) => (
                <div key={conv.id} className="p-4 hover:bg-gray-50">
                  <div className="flex items-start justify-between">
                    <div className="flex-1">
                      <div className="font-medium text-gray-900">
                        对话 {conv.id}
                      </div>
                      <div className="flex items-center gap-3 mt-2">
                        <span className="text-sm text-gray-500">
                          {conv.message_count} 条消息
                        </span>
                        <span className="text-sm text-gray-500">
                          {formatDate(conv.created_at)}
                        </span>
                      </div>
                    </div>
                    <div className="flex items-center gap-2">
                      <a
                        href={`/podcast?conversation=${conv.id}`}
                        className="text-blue-600 hover:text-blue-700 text-sm"
                      >
                        继续
                      </a>
                      <button
                        onClick={() => deleteConversation(conv.id)}
                        className="text-red-600 hover:text-red-700 text-sm"
                      >
                        删除
                      </button>
                    </div>
                  </div>
                </div>
              ))}
            </div>
          )}
        </div>
      </main>
    </div>
  )
}
