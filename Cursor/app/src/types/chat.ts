/**
 * Chat Type Definitions
 * 
 * This file contains all TypeScript types used in the chat application.
 */

/**
 * Represents a single chat message
 */
export interface Message {
  /** Unique identifier for the message */
  id: string;
  /** Type of message - from user or AI */
  type: 'human' | 'ai';
  /** The actual message content */
  content: string;
  /** ISO timestamp when message was created */
  timestamp: string;
}

/**
 * State of the chat interface
 */
export interface ChatState {
  /** Array of all messages in the conversation */
  messages: Message[];
  /** Whether a message is currently being sent/received */
  isLoading: boolean;
  /** Error message if something went wrong */
  error: string | null;
}

/**
 * Successful response from the chat API
 */
export interface ApiResponse {
  /** The AI's response message */
  response: string;
  /** Optional thread ID for the conversation */
  thread_id?: string;
}

/**
 * Error response from the API
 */
export interface ApiError {
  /** Error message describing what went wrong */
  error: string;
}

