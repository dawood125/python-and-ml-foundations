import ReactMarkdown from "react-markdown";
import CodeBlock from "./CodeBlock";

interface MarkdownRendererProps {
  content: string;  
}

export default function MarkdownRenderer({ content }: MarkdownRendererProps) {
  return (
    <ReactMarkdown

      components={{

        code({ node, inline, className, children, ...props }: any) {
          
          const match = /language-(\w+)/.exec(className || "");
          const language = match ? match[1] : "";
          const codeText = String(children).replace(/\n$/, "");

          if (inline) {
            return (
              <code
                className="bg-gray-700 text-cyan-300 px-1.5 py-0.5 
                           rounded text-sm font-mono"
                {...props}
              >
                {children}
              </code>
            );
          }

          return (
            <CodeBlock language={language}>
              {codeText}
            </CodeBlock>
          );
        },


        p({ children }) {
          return (
            <p className="mb-3 last:mb-0 leading-relaxed">
              {children}
            </p>
          );
        },

        // Bold text — **text**
        strong({ children }) {
          return (
            <strong className="text-white font-semibold">
              {children}
            </strong>
          );
        },

        // Italic text — *text*
        em({ children }) {
          return (
            <em className="text-gray-300 italic">
              {children}
            </em>
          );
        },

        // Headings — # ## ###
        h1({ children }) {
          return (
            <h1 className="text-xl font-bold text-white mt-4 mb-2">
              {children}
            </h1>
          );
        },
        h2({ children }) {
          return (
            <h2 className="text-lg font-bold text-cyan-400 mt-4 mb-2">
              {children}
            </h2>
          );
        },
        h3({ children }) {
          return (
            <h3 className="text-base font-bold text-cyan-300 mt-3 mb-1">
              {children}
            </h3>
          );
        },

        // Unordered list — bullet points
        ul({ children }) {
          return (
            <ul className="list-disc list-inside mb-3 space-y-1 
                          text-gray-200 ml-2">
              {children}
            </ul>
          );
        },

        // Ordered list — numbered list
        ol({ children }) {
          return (
            <ol className="list-decimal list-inside mb-3 space-y-1 
                          text-gray-200 ml-2">
              {children}
            </ol>
          );
        },

        // List item
        li({ children }) {
          return (
            <li className="text-gray-200 leading-relaxed">
              {children}
            </li>
          );
        },

        // Blockquote — > text
        blockquote({ children }) {
          return (
            <blockquote className="border-l-4 border-cyan-500 
                                   pl-4 my-3 text-gray-300 italic">
              {children}
            </blockquote>
          );
        },

        // Horizontal rule — ---
        hr() {
          return <hr className="border-gray-700 my-4" />;
        },
      }}
    >
      {content}
    </ReactMarkdown>
  );
}