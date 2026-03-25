"use client"

import { useState, useEffect } from "react"
import { Sun, Moon } from "lucide-react"

export function ThemeToggle() {
  const [theme, setTheme] = useState<"light" | "dark">("light")
  const [mounted, setMounted] = useState(false)

  useEffect(() => {
    setMounted(true)
    const stored = localStorage.getItem("echo-theme") as "light" | "dark" | null
    if (stored) {
      setTheme(stored)
      document.documentElement.classList.toggle("dark", stored === "dark")
    } else if (window.matchMedia("(prefers-color-scheme: dark)").matches) {
      setTheme("dark")
      document.documentElement.classList.add("dark")
    }
  }, [])

  const toggleTheme = () => {
    const newTheme = theme === "light" ? "dark" : "light"
    setTheme(newTheme)
    document.documentElement.classList.toggle("dark", newTheme === "dark")
    localStorage.setItem("echo-theme", newTheme)
  }

  if (!mounted) {
    return (
      <div className="w-8 h-8" />
    )
  }

  return (
    <button
      onClick={toggleTheme}
      className="p-2 rounded-lg hover:bg-[#2C3E50]/10 transition-colors"
      title={theme === "light" ? "切换深色模式" : "切换浅色模式"}
    >
      {theme === "light" ? (
        <Moon className="w-4 h-4 text-[#2C3E50]" />
      ) : (
        <Sun className="w-4 h-4 text-[#E67E22]" />
      )}
    </button>
  )
}
