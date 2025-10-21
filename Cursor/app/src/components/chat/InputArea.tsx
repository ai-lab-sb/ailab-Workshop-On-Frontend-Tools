'use client';

import { useState, KeyboardEvent } from 'react';

interface InputAreaProps {
  onSendMessage: (message: string) => Promise<void>;
  isLoading: boolean;
  error: string | null;
}

const MAX_LENGTH = 500;

/**
 * InputArea Component
 * 
 * Provides the input interface for sending chat messages.
 */
export default function InputArea({ onSendMessage, isLoading, error }: InputAreaProps) {
  const [value, setValue] = useState('');

  const handleSubmit = async () => {
    const trimmedValue = value.trim();
    if (!trimmedValue || trimmedValue.length > MAX_LENGTH) return;

    await onSendMessage(trimmedValue);
    setValue('');
  };

  const handleKeyDown = (e: KeyboardEvent<HTMLTextAreaElement>) => {
    if ((e.metaKey || e.ctrlKey) && e.key === 'Enter') {
      e.preventDefault();
      handleSubmit();
    }
  };

  const charCount = value.length;
  const isOverLimit = charCount >= MAX_LENGTH;
  const isNearLimit = charCount > 450;

  return (
    <div className="border-t border-gray-200 p-4 bg-white">
      <div className="flex flex-col gap-2">
        <div className="flex gap-2">
          <textarea
            value={value}
            onChange={(e) => setValue(e.target.value)}
            onKeyDown={handleKeyDown}
            placeholder="Escribe tu pregunta sobre seguros..."
            disabled={isLoading}
            className="flex-1 p-3 border-2 border-bolivar-yellow rounded-lg resize-none focus:outline-none focus:ring-2 focus:ring-bolivar-green disabled:opacity-50 disabled:cursor-not-allowed"
            rows={3}
            maxLength={MAX_LENGTH}
            aria-label="Mensaje de chat"
          />
          <button
            onClick={handleSubmit}
            disabled={isLoading || !value.trim() || isOverLimit}
            className="px-6 py-3 bg-gradient-to-r from-bolivar-green to-bolivar-green-dark text-white rounded-lg font-semibold hover:shadow-lg transition-all disabled:opacity-50 disabled:cursor-not-allowed disabled:hover:shadow-none"
            aria-label="Enviar mensaje"
          >
            {isLoading ? (
              <span className="inline-block animate-spin">⟳</span>
            ) : (
              <span>➤</span>
            )}
          </button>
        </div>

        <div className="flex justify-between items-center text-sm">
          <div>
            {error && (
              <div className="text-red-600 animate-shake">
                ⚠️ {error}
              </div>
            )}
          </div>
          <div className={`
            ${isOverLimit ? 'text-red-600 font-bold' : isNearLimit ? 'text-yellow-600' : 'text-gray-500'}
          `}>
            {charCount}/{MAX_LENGTH}
          </div>
        </div>
      </div>
    </div>
  );
}

