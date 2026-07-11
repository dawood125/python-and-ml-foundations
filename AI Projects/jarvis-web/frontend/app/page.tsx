"use client";

import { useState, useRef, useEffect } from "react";
import MessageBubble from "../components/MessageBubble";
import InputBar from "../components/InputBar";

interface Message {
  role: "user" | "assistant";
  content: string;
}

export default function Home() {
  const [messages, setMessages] = useState<Message[]>([
    {
      role: "assistant",
      content:
        "Assalamu Alaikum Dawood! 👋\n\nMain JARVIS hoon — tera personal AI tutor. Aaj kya seekhna hai? Koi concept samajhna hai, code debug karna hai, ya roadmap dekhna hai?\n\nBas poocho — main yahan hoon.",
    },
  ]);

  const [isLoading, setIsLoading] = useState(false);
  const [streamingContent, setStreamingContent] = useState("");
  const bottomRef = useRef<HTMLDivElement>(null);


  useEffect(() => {
    bottomRef.current?.scrollIntoView({ behavior: "smooth" });
  }, [messages, streamingContent]);

  const sendMessage = async (userMessage: string) => {
    const newMessages: Message[] = [
      ...messages,
      { role: "user", content: userMessage },
    ];
    setMessages(newMessages);
    setIsLoading(true);
    setStreamingContent("");

    try {
      const response = await fetch("http://localhost:8000/chat", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({

          messages: newMessages.map((m) => ({
            role: m.role,
            content: m.content,
          })),
        }),
      });

      if (!response.ok) {
        throw new Error("Backend error");
      }

      const reader = response.body!.getReader();
      const decoder = new TextDecoder();
      let fullResponse = "";

      while (true) {
        const { done, value } = await reader.read();

        if (done) break;

        const chunk = decoder.decode(value, { stream: true });
        fullResponse += chunk;
        setStreamingContent(fullResponse);
      }


      setMessages([
        ...newMessages,
        { role: "assistant", content: fullResponse },
      ]);
      setStreamingContent("");
    } catch (error) {
      setMessages([
        ...newMessages,
        {
          role: "assistant",
          content:
            "Yaar, kuch error aa gayi backend se. Check karo ke FastAPI server chal raha hai (port 8000).",
        },
      ]);
      setStreamingContent("");
    } finally {
      setIsLoading(false);
    }
  };

  return (
    <div className="flex flex-col h-screen bg-gray-950 text-white">
      
      
```tsx
{/* Header */}
<div className="border-b border-gray-800 bg-gray-900/95 
               backdrop-blur-sm px-6 py-4 sticky top-0 z-10">
  <div className="max-w-4xl mx-auto flex items-center gap-3">
    
    {/* JARVIS logo with glow effect */}
    <div className="relative">
      <div className="w-10 h-10 rounded-full bg-cyan-500 
                     flex items-center justify-center 
                     text-black font-bold text-lg
                     shadow-lg shadow-cyan-500/30">
        J
      </div>
      {/* Online indicator */}
      <div className="absolute -bottom-0.5 -right-0.5 
                     w-3 h-3 bg-green-400 rounded-full 
                     border-2 border-gray-900" />
    </div>

    <div>
      <h1 className="font-bold text-white text-lg leading-tight">
        JARVIS
      </h1>
      <p className="text-gray-400 text-xs">
        Personal AI Tutor • Python & AI/ML
      </p>
    </div>

    {/* Clear chat button */}
    <button
      onClick={() => {
        if (confirm("Clear conversation?")) {
          setMessages([
            {
              role: "assistant",
              content: "Conversation clear ho gayi. Kya seekhna hai aaj?",
            },
          ]);
        }
      }}
      className="ml-auto text-xs text-gray-500 hover:text-gray-300 
                 transition-colors bg-gray-800 hover:bg-gray-700
                 px-3 py-1.5 rounded-lg"
    >
      Clear Chat
    </button>
  </div>
</div>

      {/* Chat messages area */}
      <div className="flex-1 overflow-y-auto chat-scroll px-4 py-6">
        <div className="max-w-4xl mx-auto">
          
          {/* Render all completed messages */}
          {messages.map((message, index) => (
            <MessageBubble
              key={index}
              role={message.role}
              content={message.content}
            />
          ))}

          {/* Show streaming message while loading */}
          {isLoading && (
            <MessageBubble
              role="assistant"
              content={streamingContent || ""}
              isStreaming={true}
            />
          )}

          {/* Invisible div to scroll to */}
          <div ref={bottomRef} />
        </div>
      </div>

      {/* Input bar at bottom */}
      <InputBar onSend={sendMessage} isLoading={isLoading} />
    </div>
  );
}