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
      
      {/* Header */}
      <div className="border-b border-gray-800 bg-gray-900 px-6 py-4">
        <div className="max-w-4xl mx-auto flex items-center gap-3">
          {/* JARVIS logo */}
          <div className="w-10 h-10 rounded-full bg-cyan-500 
                         flex items-center justify-center 
                         text-black font-bold text-lg">
            J
          </div>
          <div>
            <h1 className="font-bold text-white text-lg leading-tight">
              JARVIS
            </h1>
            <p className="text-cyan-400 text-xs">
              Personal AI Tutor • Online
            </p>
          </div>

          {/* Status indicator */}
          <div className="ml-auto flex items-center gap-2">
            <div className="w-2 h-2 rounded-full bg-green-400 
                           animate-pulse" />
            <span className="text-gray-400 text-xs">Active</span>
          </div>
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