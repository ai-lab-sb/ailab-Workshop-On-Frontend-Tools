'use client';

import { useRef, useEffect } from 'react';
import type { Message } from '@/types/chat';
import MessageBubble from './MessageBubble';

interface MessageListProps {
  messages: Message[];
  isLoading: boolean;
}

/**
 * MessageList Component
 * 
 * Displays the list of chat messages with auto-scroll functionality.
 */
export default function MessageList({ messages, isLoading }: MessageListProps) {
  const bottomRef = useRef<HTMLDivElement>(null);

  // Auto-scroll to bottom when new messages arrive
  useEffect(() => {
    bottomRef.current?.scrollIntoView({ behavior: 'smooth' });
  }, [messages, isLoading]);

  return (
    <div
      className="h-[500px] overflow-y-auto p-4 bg-gradient-to-b from-gray-50 to-white custom-scrollbar"
      role="log"
      aria-live="polite"
      aria-busy={isLoading}
    >
      {messages.length === 0 ? (
        <div className="flex flex-col items-center justify-center h-full text-center">
          <div className="text-6xl mb-4">🛡️</div>
          <h3 className="text-2xl font-bold text-bolivar-green mb-2">
            Bienvenido a Seguros Bolívar
          </h3>
          <p className="text-gray-600">
            Escribe tu pregunta para comenzar
          </p>
        </div>
      ) : (
        <>
          {messages.map((message) => (
            <MessageBubble key={message.id} message={message} />
          ))}
        </>
      )}

      {isLoading && (
        <div className="flex justify-start mb-4">
          <div className="bg-white border-2 border-bolivar-yellow rounded-2xl rounded-bl-sm p-4 max-w-[70%]">
            <div className="flex items-center gap-2">
              <span className="text-xl">🤖</span>
              <div className="flex gap-1">
                <span className="w-2 h-2 bg-bolivar-green rounded-full animate-bounce-subtle"></span>
                <span className="w-2 h-2 bg-bolivar-green rounded-full animate-bounce-subtle" style={{ animationDelay: '0.1s' }}></span>
                <span className="w-2 h-2 bg-bolivar-green rounded-full animate-bounce-subtle" style={{ animationDelay: '0.2s' }}></span>
              </div>
            </div>
          </div>
        </div>
      )}

      <div ref={bottomRef} />
    </div>
  );
}

