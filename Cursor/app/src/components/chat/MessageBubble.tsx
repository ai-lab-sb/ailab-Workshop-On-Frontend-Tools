'use client';

import type { Message } from '@/types/chat';

interface MessageBubbleProps {
  message: Message;
}

/**
 * MessageBubble Component
 * 
 * Displays a single chat message with appropriate styling based on sender.
 */
export default function MessageBubble({ message }: MessageBubbleProps) {
  const isUser = message.type === 'human';
  
  // Format timestamp
  const time = new Date(message.timestamp).toLocaleTimeString('es-ES', {
    hour: '2-digit',
    minute: '2-digit',
  });

  return (
    <div className={`flex ${isUser ? 'justify-end' : 'justify-start'} mb-4 animate-fade-in ${isUser ? 'animate-slide-in-right' : 'animate-slide-in-left'}`}>
      <div className={`max-w-[70%] ${isUser ? 'ml-auto' : 'mr-auto'}`}>
        <div
          className={`
            p-4 rounded-2xl shadow-md
            ${isUser
              ? 'bg-gradient-to-r from-bolivar-green to-bolivar-green-dark text-white rounded-br-sm'
              : 'bg-white border-2 border-bolivar-yellow text-gray-800 rounded-bl-sm'
            }
          `}
        >
          <div className="flex items-start gap-2">
            <span className="text-xl">{isUser ? '👤' : '🤖'}</span>
            <div className="flex-1">
              <p className="whitespace-pre-wrap break-words">{message.content}</p>
              <p className={`text-xs mt-2 ${isUser ? 'text-white/80' : 'text-gray-500'}`}>
                {time}
              </p>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
}

