# 🔌 Prompt 3: API Integration

Prompts para crear el cliente API y tipos TypeScript.

---

## Part A: TypeScript Types

### 💬 Prompt para Cursor

```markdown
Create TypeScript types for our chat application.

File: src/types/chat.ts

Define these types:
1. Message
   - id: string (unique identifier)
   - type: 'human' | 'ai'  (who sent it)
   - content: string (message text)
   - timestamp: string (ISO format)

2. ChatState
   - messages: Message[]
   - isLoading: boolean
   - error: string | null

3. ApiResponse
   - response: string
   - thread_id?: string

4. ApiError
   - error: string

Export all types.
Add comprehensive JSDoc comments explaining each type and field.
```

### ✅ Checkpoint

File created: `src/types/chat.ts` with all types exported.

---

## Part B: API Client

### 💬 Prompt para Cursor

```markdown
Create an API client module for communicating with the insurance agent backend.

File: src/lib/api.ts

Backend API URL: Get from environment variable process.env.NEXT_PUBLIC_API_URL
Backend endpoints:
- Health check: GET /health
- Send message: POST /chat

Functions to implement:

1. generateThreadId(): string
   - Format: "nextjs_{timestamp}_{random}"
   - Use Date.now() for timestamp
   - Use Math.random() for random part
   - Return the unique ID

2. sendMessage(message: string, threadId: string): Promise<ApiResponse>
   - POST to {API_URL}/chat
   - Body: JSON with { message, thread_id }
   - Headers: Content-Type application/json
   - Timeout: 30 seconds
   - Error handling:
     * Network errors: "No se pudo conectar con el servidor"
     * Timeout: "La solicitud tardó demasiado tiempo"
     * Server errors: Parse error message from response
   - Return type: ApiResponse from @file:src/types/chat.ts
   - On error: return { error: "message" } in ApiError format

3. checkHealth(): Promise<boolean>
   - GET to {API_URL}/health
   - Return true if status 200
   - Return false on any error
   - Timeout: 5 seconds

Use fetch API (no axios).
Add proper TypeScript types.
Add JSDoc comments for each function.
Export all functions.
```

### ✅ Checkpoint

Test the API client:
```typescript
import { checkHealth, sendMessage, generateThreadId } from '@/lib/api';

// Should work if backend is running
const healthy = await checkHealth();
const threadId = generateThreadId();
const response = await sendMessage("Hola", threadId);
```

---

## Part C: Custom Hook useChat

### 💬 Prompt para Cursor

```markdown
Create a custom React hook useChat for managing chat state and interactions.

File: src/hooks/useChat.ts

This hook encapsulates all chat logic.

Hook signature:
export function useChat(threadId: string)

Return object:
{
  messages: Message[],
  isLoading: boolean,
  error: string | null,
  sendMessage: (content: string) => Promise<void>,
  clearError: () => void
}

Implementation requirements:

1. State management:
   - messages: useState<Message[]>([])
   - isLoading: useState<boolean>(false)
   - error: useState<string | null>(null)

2. sendMessage function:
   - Create user message object:
     * id: use Date.now() + Math.random()
     * type: 'human'
     * content: the message text
     * timestamp: new Date().toISOString()
   - Add user message to messages array immediately (optimistic UI)
   - Set isLoading = true
   - Call sendMessage API from @file:src/lib/api.ts
   - If success:
     * Create AI message object with response
     * Add to messages array
   - If error:
     * Set error state with message
     * Remove the optimistic user message
     * Clear error after 5 seconds using setTimeout
   - Finally: set isLoading = false
   - Use try/catch/finally for error handling

3. clearError function:
   - Simply set error to null

4. Use useCallback for sendMessage to prevent unnecessary re-renders

5. Clean up timeouts on unmount (useEffect cleanup)

Import types from @file:src/types/chat.ts
Import API functions from @file:src/lib/api.ts
Add comprehensive JSDoc comments.
Use proper TypeScript types throughout.
```

### ✅ Checkpoint

Test the hook:
```typescript
const { messages, isLoading, error, sendMessage } = useChat("test-thread");
// Should work in a React component
```

---

## 🎯 Expected Files

After completing all prompts:
```
src/
├── types/
│   └── chat.ts          ✅ TypeScript types
├── lib/
│   └── api.ts           ✅ API client
└── hooks/
    └── useChat.ts       ✅ Custom hook
```

---

## ➡️ Next Steps

Now you have the foundation! Time to build the UI components.

Continue to **Prompt 4: Chat Components**

