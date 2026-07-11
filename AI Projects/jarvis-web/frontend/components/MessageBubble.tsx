import MarkdownRenderer from "./MarkdownRenderer";

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
    <div className={`flex w-full mb-6 ${isUser ? "justify-end" : "justify-start"}`}>

      {!isUser && (
        <div className="w-9 h-9 rounded-full bg-cyan-500 
                       flex items-center justify-center 
                       text-black font-bold text-sm 
                       mr-3 mt-1 flex-shrink-0 shadow-lg
                       shadow-cyan-500/20">
          J
        </div>
      )}


      <div
        className={`max-w-[80%] rounded-2xl px-4 py-3 ${
          isUser
            ? "bg-blue-600 text-white rounded-tr-sm"
            : "bg-gray-800/80 text-gray-100 rounded-tl-sm border border-gray-700/50"
        }`}
      >
        {/* Sender label */}
        <div className={`text-xs font-semibold mb-2 ${
          isUser ? "text-blue-200" : "text-cyan-400"
        }`}>
          {isUser ? "You" : "JARVIS"}
        </div>

        {/* Message content */}
        {isUser ? (
          <p className="text-sm leading-relaxed whitespace-pre-wrap">
            {content}
          </p>
        ) : (
          <div className={`text-sm ${isStreaming ? "cursor-blink" : ""}`}>
            <MarkdownRenderer content={content} />
          </div>
        )}
      </div>

      {isUser && (
        <div className="w-9 h-9 rounded-full bg-blue-600 
                       flex items-center justify-center 
                       text-white font-bold text-sm 
                       ml-3 mt-1 flex-shrink-0">
          D
        </div>
      )}
    </div>
  );
}