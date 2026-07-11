"use client";

import { useState } from "react";
import { Prism as SyntaxHighlighter } from "react-syntax-highlighter";
import { oneDark } from "react-syntax-highlighter/dist/esm/styles/prism";

interface CodeBlockProps {
  language: string;
  children: string;
}

export default function CodeBlock({ language, children }: CodeBlockProps) {
  const [copied, setCopied] = useState(false);

  const handleCopy = async () => {
    try {
      await navigator.clipboard.writeText(children);
      setCopied(true);

      setTimeout(() => setCopied(false), 2000);
    } catch (error) {
      console.error("Copy failed:", error);
    }
  };
  return (

    <div className="relative my-4 rounded-xl overflow-hidden border border-gray-700">
      <div
        className="flex items-center justify-between 
                      bg-gray-800 px-4 py-2"
      >
        <span className="text-xs text-gray-400 font-mono">
          {language || "code"}
        </span>

        <button
          onClick={handleCopy}
          className="text-xs text-gray-400 hover:text-white 
                     transition-colors flex items-center gap-1
                     bg-gray-700 hover:bg-gray-600 
                     px-2 py-1 rounded"
        >
          {copied ? (
            <>
              <svg
                className="w-3 h-3 text-green-400"
                fill="none"
                stroke="currentColor"
                viewBox="0 0 24 24"
              >
                <path
                  strokeLinecap="round"
                  strokeLinejoin="round"
                  strokeWidth={2}
                  d="M5 13l4 4L19 7"
                />
              </svg>
              <span className="text-green-400">Copied!</span>
            </>
          ) : (
            <>
              <svg
                className="w-3 h-3"
                fill="none"
                stroke="currentColor"
                viewBox="0 0 24 24"
              >
                <path
                  strokeLinecap="round"
                  strokeLinejoin="round"
                  strokeWidth={2}
                  d="M8 16H6a2 2 0 01-2-2V6a2 2 0 012-2h8a2 2 0 012 2v2m-6 12h8a2 2 0 002-2v-8a2 2 0 00-2-2h-8a2 2 0 00-2-2v8a2 2 0 002 2z"
                />
              </svg>
              Copy
            </>
          )}
        </button>
      </div>

      <SyntaxHighlighter
        language={language || "text"}
        style={oneDark} 
        customStyle={{
          margin: 0, 
          borderRadius: 0, 
          fontSize: "13px", 
          padding: "16px",
        }}
        showLineNumbers={true}
        wrapLines={true} 
      >
        {children}
      </SyntaxHighlighter>
    </div>
  );
}
