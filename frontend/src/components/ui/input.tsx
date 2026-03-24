import * as React from "react"
import { cn } from "@/lib/utils"

export interface InputProps
  extends React.InputHTMLAttributes<HTMLInputElement> {}

const Input = React.forwardRef<HTMLInputElement, InputProps>(
  ({ className, type, ...props }, ref) => {
    return (
      <input
        type={type}
        className={cn(
          "flex h-10 w-full rounded-lg border-2 border-[#2C3E50]/20 bg-white px-4 py-2 text-sm",
          "placeholder:text-[#2C3E50]/50",
          "focus:border-[#2C3E50] focus:outline-none focus:ring-2 focus:ring-[#2C3E50]/20",
          "transition-all duration-200",
          className
        )}
        ref={ref}
        {...props}
      />
    )
  }
)
Input.displayName = "Input"

export { Input }
