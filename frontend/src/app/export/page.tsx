'use client'

import { useState } from 'react'

interface Task {
  task_id: string
  url: string
  status: string
  created_at: string
}

export default function ExportPage() {
  const [tasks, setTasks] = useState<Task[]>([])
  const [selectedTask, setSelectedTask] = useState<string | null>(null)
  const [exportFormat, setExportFormat] = useState('json')
  const [loading, setLoading] = useState(false)
  const [exportLoading, setExportLoading] = useState(false)

  const fetchTasks = async () => {
    try {
      const res = await fetch('/api/research/tasks')
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
      // 获取研究结果
      const res = await fetch(`/api/research/result/${selectedTask}`)
      if (!res.ok) {
        throw new Error('获取结果失败')
      }
      const result = await res.json()

      // 导出知识卡片
      const exportRes = await fetch('/api/export/knowledge-cards', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
          result: result,
          format: exportFormat,
          entries: result.entries || []
        })
      })

      if (!exportRes.ok) {
        throw new Error('导出失败')
      }

      // 下载文件
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
    <div className="min-h-screen bg-gray-50">
      {/* Header */}
      <header className="bg-white shadow-sm border-b">
        <div className="max-w-7xl mx-auto px-4 py-4 flex items-center justify-between">
          <div className="flex items-center gap-4">
            <a href="/podcast" className="text-gray-600 hover:text-gray-900">
              &larr; 返回研究
            </a>
            <h1 className="text-2xl font-bold text-gray-900">导出管理</h1>
          </div>
        </div>
      </header>

      <main className="max-w-7xl mx-auto px-4 py-8">
        <div className="grid grid-cols-1 lg:grid-cols-3 gap-6">
          {/* Task List */}
          <div className="bg-white rounded-lg shadow p-4">
            <div className="flex items-center justify-between mb-4">
              <h2 className="text-lg font-semibold">研究历史</h2>
              <button
                onClick={loadTasks}
                className="text-blue-600 hover:text-blue-700 text-sm"
                disabled={loading}
              >
                {loading ? '加载中...' : '刷新'}
              </button>
            </div>

            {tasks.length === 0 ? (
              <p className="text-gray-500 text-sm">暂无研究历史</p>
            ) : (
              <div className="space-y-2 max-h-96 overflow-y-auto">
                {tasks.map((task) => (
                  <div
                    key={task.task_id}
                    className={`p-3 rounded-lg cursor-pointer transition ${
                      selectedTask === task.task_id
                        ? 'bg-blue-50 border-blue-200'
                        : 'hover:bg-gray-50'
                    }`}
                    onClick={() => setSelectedTask(task.task_id)}
                  >
                    <div className="font-medium text-gray-900 truncate text-sm">
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
                      <span className="text-xs text-gray-500">
                        {new Date(task.created_at).toLocaleDateString()}
                      </span>
                    </div>
                  </div>
                ))}
              </div>
            )}
          </div>

          {/* Export Options */}
          <div className="lg:col-span-2 space-y-6">
            {/* Format Selection */}
            <div className="bg-white rounded-lg shadow p-6">
              <h2 className="text-lg font-semibold mb-4">选择导出格式</h2>
              <div className="grid grid-cols-2 md:grid-cols-5 gap-4">
                {formats.map((format) => (
                  <button
                    key={format.value}
                    onClick={() => setExportFormat(format.value)}
                    className={`p-4 rounded-lg border-2 transition text-center ${
                      exportFormat === format.value
                        ? 'border-blue-500 bg-blue-50'
                        : 'border-gray-200 hover:border-gray-300'
                    }`}
                  >
                    <div className="font-medium text-gray-900">{format.label}</div>
                    <div className="text-xs text-gray-500 mt-1">{format.desc}</div>
                  </button>
                ))}
              </div>
            </div>

            {/* Export Button */}
            <div className="bg-white rounded-lg shadow p-6">
              <h2 className="text-lg font-semibold mb-4">导出知识卡片</h2>
              <p className="text-gray-600 mb-4">
                将选中的研究结果中的知识卡片导出为 {exportFormat.toUpperCase()} 格式。
                {selectedTask
                  ? ' 已选择研究结果。'
                  : ' 请先在左侧选择一个研究结果。'}
              </p>
              <button
                onClick={exportResult}
                disabled={!selectedTask || exportLoading}
                className={`px-6 py-3 rounded-lg font-medium ${
                  !selectedTask || exportLoading
                    ? 'bg-gray-300 cursor-not-allowed'
                    : 'bg-blue-600 text-white hover:bg-blue-700'
                }`}
              >
                {exportLoading ? '导出中...' : '导出'}
              </button>
            </div>

            {/* Usage Tips */}
            <div className="bg-white rounded-lg shadow p-6">
              <h2 className="text-lg font-semibold mb-4">导出格式说明</h2>
              <div className="space-y-3 text-sm text-gray-600">
                <div>
                  <strong>JSON:</strong> 结构化数据，包含所有知识卡片信息，适合程序处理或导入其他系统。
                </div>
                <div>
                  <strong>Markdown:</strong> 纯文本格式，适合阅读、编辑和版本控制。
                </div>
                <div>
                  <strong>HTML:</strong> 包含完整样式，在浏览器中打开即可看到美观的结果。
                </div>
                <div>
                  <strong>PDF:</strong> 适合打印或在无法访问代码的环境中分享。
                </div>
                <div>
                  <strong>Anki:</strong> 闪卡格式，导入Anki后可利用间隔重复记忆系统进行复习。
                </div>
              </div>
            </div>
          </div>
        </div>
      </main>
    </div>
  )
}
