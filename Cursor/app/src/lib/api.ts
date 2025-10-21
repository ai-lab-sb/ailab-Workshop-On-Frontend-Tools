/**
 * API Client for Insurance Agent Backend
 * 
 * This module handles all communication with the insurance agent API.
 */

import type { ApiResponse, ApiError } from '@/types/chat';

const API_URL = process.env.NEXT_PUBLIC_API_URL || 'http://localhost:8000';

/**
 * Generates a unique thread ID for a conversation
 * @returns Unique thread ID in format "nextjs_{timestamp}_{random}"
 */
export function generateThreadId(): string {
  const timestamp = Date.now();
  const random = Math.random().toString(36).substring(7);
  return `nextjs_${timestamp}_${random}`;
}

/**
 * Sends a message to the AI agent and returns the response
 * 
 * @param message - The user's message
 * @param threadId - Unique conversation thread ID
 * @returns Promise resolving to API response or error
 */
export async function sendMessage(
  message: string,
  threadId: string
): Promise<ApiResponse | ApiError> {
  try {
    const controller = new AbortController();
    const timeoutId = setTimeout(() => controller.abort(), 30000);

    const response = await fetch(`${API_URL}/chat`, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({
        message,
        thread_id: threadId,
      }),
      signal: controller.signal,
    });

    clearTimeout(timeoutId);

    if (!response.ok) {
      const errorData = await response.json().catch(() => ({}));
      return {
        error: errorData.error || `Error del servidor: ${response.status}`,
      };
    }

    const data = await response.json();
    return data;
  } catch (error) {
    if (error instanceof Error) {
      if (error.name === 'AbortError') {
        return { error: 'La solicitud tardó demasiado tiempo. Intenta nuevamente.' };
      }
      if (error.message.includes('fetch')) {
        return { error: 'No se pudo conectar con el servidor. Verifica tu conexión.' };
      }
      return { error: error.message };
    }
    return { error: 'Error desconocido al enviar mensaje' };
  }
}

/**
 * Checks if the API is healthy and responding
 * 
 * @returns Promise resolving to true if healthy, false otherwise
 */
export async function checkHealth(): Promise<boolean> {
  try {
    const controller = new AbortController();
    const timeoutId = setTimeout(() => controller.abort(), 5000);

    const response = await fetch(`${API_URL}/health`, {
      signal: controller.signal,
    });

    clearTimeout(timeoutId);
    return response.ok;
  } catch {
    return false;
  }
}

