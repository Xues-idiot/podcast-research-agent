'use client'

import { useState } from 'react'
import { motion } from 'motion/react'
import { Card, CardHeader, CardTitle, CardContent } from '@/components/ui/card'
import { Button } from '@/components/ui/button'
import { Download, RefreshCw, FileJson, FileText, FileCode, FileTextIcon, Layers, ArrowLeft } from 'lucide-react'
import { ThemeToggle } from '@/components/ThemeToggle'
import { API_BASE, getResult } from '@/lib/api'

interface Task {
  task_id: string
  url: string
  status: string
  created_at: string
}

const formatIcons = {
  json: FileJson,
  markdown: FileText,
  html: FileCode,
  pdf: FileTextIcon,
  anki: Layers,
}

export default function ExportPage() {
  const [tasks, setTasks] = useState<Task[]>([])
  const [selectedTask, setSelectedTask] = useState<string | null>(null)
  const [exportFormat, setExportFormat] = useState('json')
  const [loading, setLoading] = useState(false)
  const [exportLoading, setExportLoading] = useState(false)

  const fetchTasks = async () => {
    try {
      const res = await fetch(`${API_BASE}/research/tasks`)
      if (!res.ok) throw new Error('Failed to fetch tasks')
      const data = await res.json()
      setTasks(data.tasks || [])
    } catch (error) {
      console.error('Failed to fetch tasks:', error)
    }
  }

  const loadTasks = () => {
    setLoading(true)
    fetchTasks().finally(() => setLoading(false))
  }

  const exportResult = async () => {
    if (!selectedTask) {
      alert('请先选择一个研究结果')
      return
    }

    setExportLoading(true)
    try {
      const result = await getResult(selectedTask)

      const exportRes = await fetch(`${API_BASE}/export/knowledge-cards`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
          result: result,
          format: exportFormat,
          entries: []
        })
      })

      if (!exportRes.ok) {
        throw new Error('导出失败')
      }

      const blob = await exportRes.blob()
      const url = window.URL.createObjectURL(blob)
      const a = document.createElement('a')
      a.href = url
      a.download = `knowledge_cards.${exportFormat}`
      document.body.appendChild(a)
      a.click()
      window.URL.revokeObjectURL(url)
      document.body.removeChild(a)
    } catch (error) {
      console.error('Export failed:', error)
      alert('导出失败: ' + (error as Error).message)
    } finally {
      setExportLoading(false)
    }
  }

  const formats = [
    { value: 'json', label: 'JSON', desc: '结构化数据，方便程序处理' },
    { value: 'markdown', label: 'Markdown', desc: '适合阅读和编辑' },
    { value: 'html', label: 'HTML', desc: '完整样式，浏览器查看' },
    { value: 'pdf', label: 'PDF', desc: '适合打印和分享' },
    { value: 'anki', label: 'Anki', desc: '闪卡格式，导入Anki记忆' },
  ]

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
              <a href="/export" className="text-sm font-medium text-[#2C3E50] hover:text-[#E67E22]">导出</a>
              <a href="/history" className="text-sm font-medium text-gray-600 hover:text-[#E67E22]">历史</a>
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
            <Download className="w-6 h-6 text-[#E67E22]" />
            导出管理
          </h1>
          <p className="text-[#2C3E50]/60 mt-1">将研究结果导出为多种格式</p>
        </motion.div>

        <div className="grid grid-cols-1 lg:grid-cols-3 gap-6">
          {/* Task List */}
          <motion.div
            initial={{ opacity: 0, x: -20 }}
            animate={{ opacity: 1, x: 0 }}
            transition={{ delay: 0.1 }}
          >
            <Card>
              <CardHeader>
                <div className="flex items-center justify-between">
                  <CardTitle className="text-lg">研究历史</CardTitle>
                  <Button
                    variant="ghost"
                    size="sm"
                    onClick={loadTasks}
                    disabled={loading}
                    className="text-[#E67E22]"
                  >
                    <RefreshCw className={`w-4 h-4 mr-1 ${loading ? 'animate-spin' : ''}`} />
                    {loading ? '加载中...' : '刷新'}
                  </Button>
                </div>
              </CardHeader>
              <CardContent>
                {tasks.length === 0 ? (
                  <p className="text-[#2C3E50]/50 text-sm text-center py-4">暂无研究历史</p>
                ) : (
                  <div className="space-y-2 max-h-96 overflow-y-auto">
                    {tasks.map((task) => (
                      <motion.div
                        key={task.task_id}
                        whileHover={{ scale: 1.02 }}
                        whileTap={{ scale: 0.98 }}
                        className={`p-3 rounded-lg cursor-pointer transition ${
                          selectedTask === task.task_id
                            ? 'bg-[#E67E22]/10 border-l-2 border-l-[#E67E22]'
                            : 'hover:bg-[#FAF8F5]'
                        }`}
                        onClick={() => setSelectedTask(task.task_id)}
                      >
                        <div className="font-medium text-[#2C3E50] truncate text-sm">
                          {task.url}
                        </div>
                        <div className="flex items-center gap-2 mt-1">
                          <span
                            className={`text-xs px-2 py-0.5 rounded ${
                              task.status === 'completed'
                                ? 'bg-green-100 text-green-700'
                                : task.status === 'failed'
                                ? 'bg-red-100 text-red-700'
                                : 'bg-yellow-100 text-yellow-700'
                            }`}
                          >
                            {task.status}
                          </span>
                          <span className="text-xs text-[#2C3E50]/50">
                            {new Date(task.created_at).toLocaleDateString()}
                          </span>
                        </div>
                      </motion.div>
                    ))}
                  </div>
                )}
              </CardContent>
            </Card>
          </motion.div>

          {/* Export Options */}
          <div className="lg:col-span-2 space-y-6">
            {/* Format Selection */}
            <motion.div
              initial={{ opacity: 0, y: 20 }}
              animate={{ opacity: 1, y: 0 }}
              transition={{ delay: 0.2 }}
            >
              <Card className="border-l-4 border-l-[#2C3E50]">
                <CardHeader>
                  <CardTitle>选择导出格式</CardTitle>
                </CardHeader>
                <CardContent>
                  <div className="grid grid-cols-2 md:grid-cols-5 gap-4">
                    {formats.map((format) => {
                      const Icon = formatIcons[format.value as keyof typeof formatIcons]
                      return (
                        <motion.button
                          key={format.value}
                          whileHover={{ scale: 1.05 }}
                          whileTap={{ scale: 0.95 }}
                          onClick={() => setExportFormat(format.value)}
                          className={`p-4 rounded-lg border-2 transition text-center ${
                            exportFormat === format.value
                              ? 'border-[#E67E22] bg-[#E67E22]/5'
                              : 'border-[#2C3E50]/20 hover:border-[#2C3E50]/40'
                          }`}
                        >
                          {Icon && <Icon className={`w-6 h-6 mx-auto mb-2 ${exportFormat === format.value ? 'text-[#E67E22]' : 'text-[#2C3E50]/50'}`} />}
                          <div className="font-medium text-[#2C3E50]">{format.label}</div>
                          <div className="text-xs text-[#2C3E50]/50 mt-1">{format.desc}</div>
                        </motion.button>
                      )
                    })}
                  </div>
                </CardContent>
              </Card>
            </motion.div>

            {/* Export Button */}
            <motion.div
              initial={{ opacity: 0, y: 20 }}
              animate={{ opacity: 1, y: 0 }}
              transition={{ delay: 0.3 }}
            >
              <Card className="border-l-4 border-l-[#E67E22]">
                <CardHeader>
                  <CardTitle>导出知识卡片</CardTitle>
                </CardHeader>
                <CardContent>
                  <p className="text-[#2C3E50]/70 mb-4">
                    将选中的研究结果中的知识卡片导出为 {exportFormat.toUpperCase()} 格式。
                    {selectedTask
                      ? ' 已选择研究结果。'
                      : ' 请先在左侧选择一个研究结果。'}
                  </p>
                  <Button
                    onClick={exportResult}
                    disabled={!selectedTask || exportLoading}
                    className={`${
                      !selectedTask || exportLoading
                        ? 'bg-[#2C3E50]/20 cursor-not-allowed'
                        : 'bg-[#E67E22] hover:bg-[#D35400]'
                    }`}
                  >
                    <Download className="w-4 h-4 mr-2" />
                    {exportLoading ? '导出中...' : '导出'}
                  </Button>
                </CardContent>
              </Card>
            </motion.div>

            {/* Usage Tips */}
            <motion.div
              initial={{ opacity: 0, y: 20 }}
              animate={{ opacity: 1, y: 0 }}
              transition={{ delay: 0.4 }}
            >
              <Card>
                <CardHeader>
                  <CardTitle>导出格式说明</CardTitle>
                </CardHeader>
                <CardContent>
                  <div className="space-y-3 text-sm text-[#2C3E50]/70">
                    <div>
                      <strong className="text-[#2C3E50]">JSON:</strong> 结构化数据，包含所有知识卡片信息，适合程序处理或导入其他系统。
                    </div>
                    <div>
                      <strong className="text-[#2C3E50]">Markdown:</strong> 纯文本格式，适合阅读、编辑和版本控制。
                    </div>
                    <div>
                      <strong className="text-[#2C3E50]">HTML:</strong> 包含完整样式，在浏览器中打开即可看到美观的结果。
                    </div>
                    <div>
                      <strong className="text-[#2C3E50]">PDF:</strong> 适合打印或在无法访问代码的环境中分享。
                    </div>
                    <div>
                      <strong className="text-[#2C3E50]">Anki:</strong> 闪卡格式，导入Anki后可利用间隔重复记忆系统进行复习。
                    </div>
                  </div>
                </CardContent>
              </Card>
            </motion.div>
          </div>
        </div>
      </main>
    </div>
  )
}
