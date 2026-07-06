interface MessageBubbleProps {
  role: "user" | "assistant";
  content: string;
  isStreaming?: boolean;
}

export default function MessageBubble({
  role,
  content,
  isStreaming = false,
}: MessageBubbleProps) {
  const isUser = role === "user";

  return (
    <div
      className={`flex w-full mb-4 ${
        isUser ? "justify-end" : "justify-start"
      }`}
    >
      {/* JARVIS avatar */}
      {!isUser && (
        <div className="w-8 h-8 rounded-full bg-cyan-500 flex items-center justify-center text-black font-bold text-sm mr-3 mt-1 flex-shrink-0">
          J
        </div>
      )}

      {/* Message bubble */}
      <div
        className={`max-w-[75%] rounded-2xl px-4 py-3 ${
          isUser
            ? "bg-blue-600 text-white rounded-tr-sm"
            : "bg-gray-800 text-gray-100 rounded-tl-sm"
        }`}
      >
        {/* Sender label */}
        <div
          className={`text-xs font-semibold mb-1 ${
            isUser ? "text-blue-200" : "text-cyan-400"
          }`}
        >
          {isUser ? "You" : "JARVIS"}
        </div>

        {/* Message content */}
        <div
          className={`text-sm leading-relaxed whitespace-pre-wrap ${
            isStreaming ? "cursor-blink" : ""
          }`}
        >
          {content}
        </div>
      </div>

      {/* User avatar */}
      {isUser && (
        <div className="w-8 h-8 rounded-full bg-blue-600 flex items-center justify-center text-white font-bold text-sm ml-3 mt-1 flex-shrink-0">
          D
        </div>
      )}
    </div>
  );
}