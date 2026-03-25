"use client"

import { useEffect, useCallback } from "react"

interface KeyboardNavOptions {
  onNextSection?: () => void
  onPrevSection?: () => void
  onFocusSearch?: () => void
  onToggleTheme?: () => void
  enabled?: boolean
}

export function useKeyboardNavigation(options: KeyboardNavOptions = {}) {
  const {
    onNextSection,
    onPrevSection,
    onFocusSearch,
    onToggleTheme,
    enabled = true
  } = options

  const handleKeyDown = useCallback((e: KeyboardEvent) => {
    if (!enabled) return

    // Skip if user is typing in an input
    if (e.target instanceof HTMLInputElement || e.target instanceof HTMLTextAreaElement) {
      return
    }

    // j or ArrowDown - next section
    if (e.key === "j" || e.key === "ArrowDown") {
      if (onNextSection && !e.metaKey && !e.ctrlKey) {
        e.preventDefault()
        onNextSection()
      }
    }

    // k or ArrowUp - previous section
    if (e.key === "k" || e.key === "ArrowUp") {
      if (onPrevSection && !e.metaKey && !e.ctrlKey) {
        e.preventDefault()
        onPrevSection()
      }
    }

    // t - toggle theme
    if (e.key === "t" && onToggleTheme) {
      e.preventDefault()
      onToggleTheme()
    }
  }, [enabled, onNextSection, onPrevSection, onToggleTheme])

  useEffect(() => {
    window.addEventListener("keydown", handleKeyDown)
    return () => window.removeEventListener("keydown", handleKeyDown)
  }, [handleKeyDown])
}

// Keyboard shortcuts help component
export function KeyboardShortcutsHelp() {
  const shortcuts = [
    { key: "/", description: "聚焦搜索框" },
    { key: "Esc", description: "回到顶部" },
    { key: "j", description: "下一节" },
    { key: "k", description: "上一节" },
    { key: "t", description: "切换主题" },
  ]

  return (
    <div className="text-xs text-[#2C3E50]/40 space-y-1">
      {shortcuts.map(({ key, description }) => (
        <div key={key} className="flex items-center gap-2">
          <kbd className="px-1.5 py-0.5 bg-[#2C3E50]/10 rounded text-[10px] font-mono">
            {key}
          </kbd>
          <span>{description}</span>
        </div>
      ))}
    </div>
  )
}
