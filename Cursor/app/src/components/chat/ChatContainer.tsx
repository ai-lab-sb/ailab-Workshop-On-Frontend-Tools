'use client';

import { useState, useEffect } from 'react';
import { generateThreadId } from '@/lib/api';
import { useChat } from '@/hooks/useChat';
import MessageList from './MessageList';
import InputArea from './InputArea';

/**
 * ChatContainer Component
 * 
 * Main container that orchestrates the entire chat interface.
 */
export default function ChatContainer() {
  const [threadId, setThreadId] = useState<string>('');

  // Generate thread ID on mount
  useEffect(() => {
    setThreadId(generateThreadId());
  }, []);

  // Use chat hook
  const { messages, isLoading, error, sendMessage } = useChat(threadId);

  return (
    <div className="max-w-4xl mx-auto my-8">
      <div className="bg-white rounded-xl shadow-2xl overflow-hidden">
        {/* Header */}
        <div className="bg-gradient-to-r from-bolivar-green to-bolivar-green-dark text-white p-6 border-b-4 border-bolivar-yellow sticky top-0 z-10">
          <div className="flex items-center gap-3">
            <span className="text-4xl">🛡️</span>
            <div>
              <h1 className="text-2xl font-bold">Seguros Bolívar</h1>
              <p className="text-sm opacity-90">Asistente Virtual</p>
            </div>
          </div>
        </div>

        {/* Message List */}
        <MessageList messages={messages} isLoading={isLoading} />

        {/* Input Area */}
        <InputArea
          onSendMessage={sendMessage}
          isLoading={isLoading}
          error={error}
        />
      </div>
    </div>
  );
}

