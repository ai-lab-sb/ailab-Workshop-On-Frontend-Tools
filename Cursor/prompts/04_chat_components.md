# 💬 Prompt 4: Chat Components

Prompts para crear los componentes de la interfaz de chat.

---

## Part A: MessageBubble Component

### 💬 Prompt para Cursor

```markdown
Create a MessageBubble component to display a single chat message.

File: src/components/chat/MessageBubble.tsx

This is a client component (add 'use client' directive).

Props:
- message: Message (import type from @file:src/types/chat.ts)

Visual Design:

For USER messages (type='human'):
- Background: Linear gradient from bolivar-green to bolivar-green-dark
- Text color: white
- Alignment: Right side (use ml-auto to push right)
- Border radius: rounded-2xl rounded-br-sm (speech bubble effect)
- Max width: 70% of container
- Icon: Display "👤" emoji before message content
- Padding: p-4
- Shadow: subtle shadow

For AI messages (type='ai'):
- Background: white
- Border: 2px solid bolivar-yellow
- Text color: gray-800
- Alignment: Left side (use mr-auto)
- Border radius: rounded-2xl rounded-bl-sm (speech bubble effect)
- Max width: 70% of container  
- Icon: Display "🤖" emoji before message content
- Padding: p-4
- Shadow: subtle shadow

For BOTH:
- Display timestamp at the bottom
- Timestamp format: Format time as "HH:MM" (use Intl.DateTimeFormat or date-fns)
- Timestamp style: text-xs, text-gray-500, mt-1
- Animation: Fade-in animation when component mounts
- Use Tailwind utility classes
- Responsive: Full width on very small screens

Structure:
<div className="message-container">
  <div className="message-bubble">
    <span>emoji</span>
    <p>content</p>
    <span className="timestamp">time</span>
  </div>
</div>

Use semantic HTML.
Export as default.
Add TypeScript types.
Add JSDoc comments.
```

### ✅ Checkpoint

Create a test page to see your MessageBubble:
```tsx
<MessageBubble message={{
  id: '1',
  type: 'human',
  content: 'Hola!',
  timestamp: new Date().toISOString()
}} />
```

---

## Part B: MessageList Component

### 💬 Prompt para Cursor

```markdown
Create a MessageList component to display all chat messages.

File: src/components/chat/MessageList.tsx

This is a client component (add 'use client' directive).

Props:
- messages: Message[] (import from @file:src/types/chat.ts)
- isLoading: boolean

Features:

1. Messages Display:
   - Map through messages array
   - Render MessageBubble for each message
   - Pass the message object as prop
   - Key: use message.id

2. Auto-scroll to bottom:
   - Use useRef to create a reference to bottom element
   - Use useEffect that triggers when messages change
   - Scroll to bottom smoothly: scrollIntoView({ behavior: 'smooth' })

3. Loading Indicator:
   - Show when isLoading === true
   - Display three dots that bounce (... animation)
   - Style similar to AI message bubble
   - Use CSS keyframe animation for bounce effect

4. Empty State (no messages):
   - Show welcome message when messages.length === 0
   - Centered content:
     * Large emoji: 🛡️
     * Title: "Bienvenido a Seguros Bolívar"
     * Subtitle: "Escribe tu pregunta para comenzar"
   - Use bolivar-green color for accent
   - Center vertically and horizontally in container

Container Styling:
- Height: h-[500px] fixed height
- Overflow: overflow-y-auto (scrollable)
- Padding: p-4
- Background: Subtle gradient (from gray-50 to white)
- Custom scrollbar:
  * Width: thin (8px)
  * Track: light gray
  * Thumb: bolivar-green color
  * Hover: bolivar-green-dark

Implementation Details:
- Create a ref element at the bottom for auto-scroll
- Structure:
  <div className="message-list-container" ref={containerRef}>
    {messages.length === 0 ? <WelcomeMessage /> : messages.map(...)}
    {isLoading && <LoadingDots />}
    <div ref={bottomRef} /> {/* Auto-scroll anchor */}
  </div>

Import MessageBubble from: ./MessageBubble
Use TypeScript types.
Add JSDoc comments.
Export as default.
```

### ✅ Checkpoint

Test with sample data:
```tsx
<MessageList 
  messages={[/* sample messages */]} 
  isLoading={false} 
/>
```

---

## Part C: InputArea Component

### 💬 Prompt para Cursor

```markdown
Create an InputArea component for sending chat messages.

File: src/components/chat/InputArea.tsx

This is a client component (add 'use client' directive).

Props:
- onSendMessage: (message: string) => Promise<void>
- isLoading: boolean
- error: string | null

Features:

1. Textarea Input:
   - Use Shadcn Textarea component
   - Placeholder: "Escribe tu pregunta sobre seguros..."
   - Auto-resize as user types (up to max height)
   - Max height: 150px
   - Disabled when isLoading === true
   - Value: controlled by local state (value, setValue)
   - onChange: update state
   - onKeyDown: Submit on Cmd+Enter or Ctrl+Enter

2. Send Button:
   - Use Shadcn Button component
   - Icon: Display "➤" or use a send icon
   - Text: "Enviar"
   - Background: bolivar-green
   - Hover: bolivar-green-dark
   - Disabled when:
     * Input is empty (value.trim() === '')
     * OR isLoading === true
   - Loading state: Show spinner icon when isLoading
   - onClick: call handleSubmit

3. Character Counter:
   - Display: "{current}/500" 
   - Show at bottom right of textarea
   - Warning style (yellow) when count > 450
   - Error style (red) when count >= 500
   - Block sending if >= 500 characters

4. Error Display:
   - Show error message when props.error is not null
   - Red background, white text
   - Display below textarea
   - Include "X" button to dismiss (call onClearError)
   - Animation: Shake animation when error appears

Behavior:

- handleSubmit function:
  1. Prevent default if form submission
  2. Trim the message
  3. If empty, return early
  4. If > 500 chars, return early
  5. Call await onSendMessage(message)
  6. If successful, clear the textarea (setValue(''))
  7. Focus back on textarea

Layout:
- Use Shadcn Card component as wrapper
- Textarea and Button in a flex row
- Counter below textarea
- Error message below everything
- Padding and spacing with Tailwind
- Responsive: Stack vertically on very small screens

Import from Shadcn:
- Card, CardContent
- Textarea
- Button

Use TypeScript types.
Add JSDoc comments.
Export as default.
```

### ✅ Checkpoint

Test InputArea with mock function:
```tsx
<InputArea 
  onSendMessage={async (msg) => console.log(msg)}
  isLoading={false}
  error={null}
/>
```

---

## Part D: ChatContainer Component

### 💬 Prompt para Cursor

```markdown
Create a ChatContainer component that brings everything together.

File: src/components/chat/ChatContainer.tsx

This is a client component (add 'use client' directive).

This is the main component that orchestrates the entire chat interface.

No props needed (manages its own state).

Implementation:

1. Generate unique thread ID:
   - Use generateThreadId from @file:src/lib/api.ts
   - Generate once on component mount
   - Store in useState

2. Use the useChat hook:
   - Import from @file:src/hooks/useChat.ts
   - Pass the threadId
   - Destructure: { messages, isLoading, error, sendMessage, clearError }

3. Component Structure:

   Header Section:
   - Background: Linear gradient bolivar-green to bolivar-green-dark
   - Text color: white
   - Padding: p-6
   - Content:
     * Icon: 🛡️ emoji (large)
     * Title: "Seguros Bolívar" (text-2xl font-bold)
     * Subtitle: "Asistente Virtual" (text-sm opacity-90)
   - Sticky to top when scrolling (sticky top-0 z-10)
   - Border bottom: 4px bolivar-yellow

   MessageList Section:
   - Import MessageList from ./MessageList
   - Pass props: messages and isLoading
   - This takes most of the vertical space

   InputArea Section:
   - Import InputArea from ./InputArea
   - Pass props: onSendMessage={sendMessage}, isLoading, error
   - Sticky to bottom (sticky bottom-0)
   - Shadow above for visual separation

Container Styling:
- Max width: max-w-4xl
- Centered: mx-auto
- Vertical margin: my-8
- Padding: responsive padding
- Background: white
- Shadow: Large shadow for elevation
- Border radius: rounded-xl
- Min height to look good

Responsive Design:
- Full width on mobile (px-4)
- Fixed width on desktop (max-w-4xl)
- Adjust padding for different screen sizes

Import components:
- MessageList from './MessageList'
- InputArea from './InputArea'
- useChat from '@/hooks/useChat'
- generateThreadId from '@/lib/api'

Use TypeScript types.
Add JSDoc comments explaining the component structure.
Export as default.
```

### ✅ Checkpoint

Test the complete ChatContainer:
```tsx
// In a page or test component:
<ChatContainer />
```

Should show:
- ✅ Header with logo
- ✅ Welcome message (empty state)
- ✅ Input area at bottom

---

## 🎯 Expected Files

After completing all prompts:
```
src/components/chat/
├── MessageBubble.tsx    ✅ Individual message
├── MessageList.tsx      ✅ List of messages
├── InputArea.tsx        ✅ Input + send button
└── ChatContainer.tsx    ✅ Main orchestrator
```

---

## ➡️ Next Steps

Your chat interface is complete! Now integrate it into the main page.

Continue to **Prompt 5: Page Integration & Polish**

