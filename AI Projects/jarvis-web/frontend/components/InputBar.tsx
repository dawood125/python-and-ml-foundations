import { useState, KeyboardEvent } from "react";

interface InputBarProps {
  onSend: (message: string) => void;
  isLoading: boolean;
}

export default function InputBar({ onSend, isLoading }: InputBarProps) {
  const [input, setInput] = useState("");

  const handleSend = () => {
    const trimmed = input.trim();
    if (!trimmed || isLoading) return;
    onSend(trimmed);
    setInput("");
  };

  const handleKeyDown = (e: KeyboardEvent<HTMLTextAreaElement>) => {
    if (e.key === "Enter" && !e.shiftKey) {
      e.preventDefault();
      handleSend();
    }
  };

  return (
    <div className="border-t border-gray-700 p-4 bg-gray-900">
      <div className="flex items-end gap-3 max-w-4xl mx-auto">
        {/* Text input */}
        <textarea
          value={input}
          onChange={(e) => setInput(e.target.value)}
          onKeyDown={handleKeyDown}
          placeholder={
            isLoading
              ? "JARVIS is thinking..."
              : "Kuch poocho JARVIS se... (Enter to send)"
          }
          disabled={isLoading}
          rows={1}
          className="flex-1 bg-gray-800 text-white placeholder-gray-500 
                     rounded-xl px-4 py-3 text-sm resize-none
                     border border-gray-700 focus:border-cyan-500 
                     focus:outline-none transition-colors
                     disabled:opacity-50 disabled:cursor-not-allowed
                     max-h-32 overflow-y-auto"
          style={{
            height: "auto",
            minHeight: "48px",
          }}
          onInput={(e) => {
            // Auto resize textarea
            const target = e.target as HTMLTextAreaElement;
            target.style.height = "auto";
            target.style.height = `${target.scrollHeight}px`;
          }}
        />

        {/* Send button */}
        <button
          onClick={handleSend}
          disabled={isLoading || !input.trim()}
          className="bg-cyan-500 hover:bg-cyan-400 disabled:bg-gray-700
                     disabled:cursor-not-allowed text-black font-bold
                     rounded-xl px-4 py-3 transition-colors
                     flex items-center justify-center min-w-[48px]"
        >
          {isLoading ? (
            // Loading spinner
            <div className="w-5 h-5 border-2 border-gray-500 
                           border-t-cyan-400 rounded-full animate-spin" />
          ) : (
            // Send arrow
            <svg
              className="w-5 h-5"
              fill="none"
              stroke="currentColor"
              viewBox="0 0 24 24"
            >
              <path
                strokeLinecap="round"
                strokeLinejoin="round"
                strokeWidth={2}
                d="M12 19l9 2-9-18-9 18 9-2zm0 0v-8"
              />
            </svg>
          )}
        </button>
      </div>

      {/* Helper text */}
      <p className="text-center text-gray-600 text-xs mt-2">
        Enter to send • Shift+Enter for new line
      </p>
    </div>
  );
}