/**
 * useChat Hook
 * 
 * Custom React hook for managing chat state and interactions with the AI agent.
 */

'use client';

import { useState, useCallback, useEffect } from 'react';
import type { Message } from '@/types/chat';
import { sendMessage as apiSendMessage } from '@/lib/api';

interface UseChatReturn {
  messages: Message[];
  isLoading: boolean;
  error: string | null;
  sendMessage: (content: string) => Promise<void>;
  clearError: () => void;
}

/**
 * Hook for managing chat functionality
 * 
 * @param threadId - Unique conversation thread ID
 * @returns Chat state and functions
 */
export function useChat(threadId: string): UseChatReturn {
  const [messages, setMessages] = useState<Message[]>([]);
  const [isLoading, setIsLoading] = useState(false);
  const [error, setError] = useState<string | null>(null);

  /**
   * Sends a message to the AI and updates state
   */
  const sendMessage = useCallback(async (content: string) => {
    // Create user message
    const userMessage: Message = {
      id: `${Date.now()}-${Math.random()}`,
      type: 'human',
      content,
      timestamp: new Date().toISOString(),
    };

    // Add user message immediately (optimistic UI)
    setMessages(prev => [...prev, userMessage]);
    setIsLoading(true);
    setError(null);

    try {
      // Call API
      const response = await apiSendMessage(content, threadId);

      if ('error' in response) {
        // Handle error response
        setError(response.error);
        // Remove optimistic user message
        setMessages(prev => prev.filter(msg => msg.id !== userMessage.id));
        
        // Clear error after 5 seconds
        setTimeout(() => setError(null), 5000);
      } else {
        // Create AI message
        const aiMessage: Message = {
          id: `${Date.now()}-${Math.random()}`,
          type: 'ai',
          content: response.response,
          timestamp: new Date().toISOString(),
        };
        
        // Add AI response
        setMessages(prev => [...prev, aiMessage]);
      }
    } catch (err) {
      const errorMessage = err instanceof Error ? err.message : 'Error desconocido';
      setError(errorMessage);
      // Remove optimistic user message
      setMessages(prev => prev.filter(msg => msg.id !== userMessage.id));
      
      // Clear error after 5 seconds
      setTimeout(() => setError(null), 5000);
    } finally {
      setIsLoading(false);
    }
  }, [threadId]);

  /**
   * Clears the current error message
   */
  const clearError = useCallback(() => {
    setError(null);
  }, []);

  return {
    messages,
    isLoading,
    error,
    sendMessage,
    clearError,
  };
}

