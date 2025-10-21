# 3️⃣ Build Guide - Construyendo con Cursor

Guía paso a paso para construir la aplicación **Seguros Bolívar Chat** usando Cursor AI.

---

## 🎯 Objetivo del Módulo

Construirás una aplicación de chat moderna que se conecta con el agente de IA de seguros.

### Lo que construirás:
- ✅ Chat interactivo en tiempo real
- ✅ UI moderna con Tailwind CSS
- ✅ Integración con API REST
- ✅ Manejo de estados (loading, errors)
- ✅ TypeScript para type safety
- ✅ Diseño responsive
- ✅ Colores corporativos Seguros Bolívar

### Tech Stack:
```
- Next.js 14 (App Router)
- React + TypeScript
- Tailwind CSS
- Shadcn/ui components
```

---

## 📋 Prerequisitos

Antes de empezar:

```bash
✅ Node.js 18+ instalado
✅ Cursor IDE instalado y configurado
✅ Backend API corriendo en http://localhost:8000
✅ Leíste 1_CURSOR_BASICS.md
✅ Leíste 2_PROMPTING_GUIDE.md
```

Verifica el backend:
```bash
curl http://localhost:8000/health
# Debe retornar: {"status":"healthy"}
```

---

## 🏗️ Arquitectura del Proyecto

```
app/
├── src/
│   ├── app/                    # Next.js App Router
│   │   ├── page.tsx           # Página principal (chat)
│   │   ├── layout.tsx         # Layout global
│   │   └── globals.css        # Estilos globales
│   │
│   ├── components/            # Componentes React
│   │   ├── chat/
│   │   │   ├── ChatContainer.tsx
│   │   │   ├── MessageList.tsx
│   │   │   ├── MessageBubble.tsx
│   │   │   └── InputArea.tsx
│   │   │
│   │   └── ui/                # Componentes UI base (Shadcn)
│   │       ├── button.tsx
│   │       ├── card.tsx
│   │       └── input.tsx
│   │
│   ├── hooks/                 # Custom React hooks
│   │   └── useChat.ts         # Hook para manejar chat
│   │
│   ├── lib/                   # Utilidades
│   │   ├── api.ts             # Cliente API
│   │   └── utils.ts           # Helper functions
│   │
│   └── types/                 # TypeScript definitions
│       └── chat.ts            # Tipos del chat
│
├── public/                    # Assets estáticos
├── .env.local                 # Variables de entorno
├── tailwind.config.ts         # Config de Tailwind
├── tsconfig.json              # Config de TypeScript
└── package.json               # Dependencies
```

---

## 🚀 Fase 1: Setup Inicial del Proyecto

### Step 1.1: Crear Proyecto Next.js

**Objetivo**: Crear el proyecto base con todas las dependencias.

**Prompt para Cursor**:
```markdown
Create a new Next.js 14 project with the following setup:

- Use App Router (not Pages Router)
- Enable TypeScript
- Include Tailwind CSS
- Use src/ directory structure
- Include ESLint
- Do NOT use the default Next.js font optimization

Run this command and show me what to do:
npx create-next-app@latest seguros-chat --typescript --tailwind --eslint --app --src-dir --no-git

Then explain the project structure created.
```

**Ejecuta en tu terminal**:
```bash
cd Cursor
npx create-next-app@latest app --typescript --tailwind --eslint --app --src-dir
```

Responde a las preguntas:
- TypeScript: Yes
- ESLint: Yes
- Tailwind: Yes
- `src/` directory: Yes
- App Router: Yes
- Import alias (@/*): Yes

**✅ Checkpoint 1**: Proyecto creado, puedes correr `npm run dev`

---

### Step 1.2: Instalar Shadcn/ui

**Objetivo**: Agregar componentes UI pre-construidos.

**Prompt para Cursor**:
```markdown
I need to add Shadcn/ui to this Next.js project.

Guide me through:
1. Running the Shadcn init command
2. Configuring it for Next.js App Router
3. Installing these components: button, card, input, textarea

Show me the exact commands to run.
```

**Ejecuta**:
```bash
cd app
npx shadcn@latest init
```

Configuración recomendada:
- Style: Default
- Base color: Slate
- CSS variables: Yes

Instala componentes:
```bash
npx shadcn@latest add button card input textarea
```

**✅ Checkpoint 2**: Shadcn configurado, componentes instalados

---

### Step 1.3: Configurar Variables de Entorno

**Objetivo**: Configurar la URL de la API.

**Usa Cursor** (Cmd+K en un archivo nuevo):
```markdown
Create a .env.local file with this content:
NEXT_PUBLIC_API_URL=http://localhost:8000

Also create a .env.example file as template for other developers.

Explain why we use NEXT_PUBLIC_ prefix.
```

**Crea manualmente**:
```bash
echo "NEXT_PUBLIC_API_URL=http://localhost:8000" > .env.local
```

**✅ Checkpoint 3**: Variables de entorno configuradas

---

## 🎨 Fase 2: Estilos y Tema

### Step 2.1: Configurar Colores Corporativos

**Objetivo**: Añadir colores de Seguros Bolívar al tema.

**Prompt para Cursor** (abre `tailwind.config.ts`):
```markdown
Update this Tailwind config to include Seguros Bolívar corporate colors:

Colors to add to theme.extend.colors:
- bolivar-green: #00A651
- bolivar-green-dark: #008040
- bolivar-yellow: #FFD100
- bolivar-yellow-dark: #E6BC00

Also add these custom classes in theme.extend:
- Animation for message fade-in
- Custom shadows for cards

Keep existing config, just extend it.
```

**✅ Checkpoint 4**: Tema personalizado configurado

---

### Step 2.2: Estilos Globales

**Objetivo**: Configurar estilos base.

**Prompt para Cursor** (abre `src/app/globals.css`):
```markdown
Update the globals.css file with:

1. Keep the existing Tailwind directives
2. Add custom styles for:
   - Body: white background, smooth scrolling
   - Custom scrollbar: thin, green/yellow theme
   - Chat container: max-width, centered
3. Add animation keyframes for:
   - fadeIn: opacity 0 to 1
   - slideIn: translateY 10px to 0

Use modern CSS with CSS variables where appropriate.
```

**✅ Checkpoint 5**: Estilos globales configurados

---

## 🧱 Fase 3: Componentes Base

### Step 3.1: TypeScript Types

**Objetivo**: Definir tipos para el chat.

**Prompt para Cursor** (crea `src/types/chat.ts`):
```markdown
Create TypeScript types for our chat application:

Types needed:
1. Message
   - id: string
   - type: 'human' | 'ai'
   - content: string
   - timestamp: string

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
Add JSDoc comments explaining each type.
```

**✅ Checkpoint 6**: Tipos definidos

---

### Step 3.2: API Client

**Objetivo**: Funciones para comunicarse con el backend.

**Prompt para Cursor** (crea `src/lib/api.ts`):
```markdown
Create an API client module for the insurance agent API.

Requirements:
1. Base URL from environment variable: process.env.NEXT_PUBLIC_API_URL
2. Generate unique thread_id (use timestamp + random)

Functions to create:
- sendMessage(message: string, threadId: string): Promise<ApiResponse>
  - POST to /chat endpoint
  - Send JSON: { message, thread_id }
  - Handle errors: timeout, network, server errors
  - Use fetch API
  - TypeScript types from @file:src/types/chat.ts

- checkHealth(): Promise<boolean>
  - GET to /health endpoint
  - Return true if healthy, false otherwise

Error handling:
- Timeout after 30 seconds
- Network errors: return custom error message
- Parse error responses from API

Add proper TypeScript types and JSDoc comments.
```

**✅ Checkpoint 7**: API client funcional

---

### Step 3.3: Custom Hook useChat

**Objetivo**: Hook para manejar lógica del chat.

**Prompt para Cursor** (crea `src/hooks/useChat.ts`):
```markdown
Create a custom React hook useChat for managing chat state and logic.

Hook signature:
export function useChat(threadId: string)

State to manage:
- messages: Message[]
- isLoading: boolean
- error: string | null

Functions to expose:
1. sendMessage(content: string): Promise<void>
   - Add user message to state immediately
   - Call API with sendMessage from @file:src/lib/api.ts
   - On success: add AI response to messages
   - On error: set error state, remove user message
   - Clear error after 5 seconds

2. clearError(): void
   - Reset error to null

Implementation details:
- Use useState for state management
- Use useCallback for sendMessage to prevent re-renders
- Each message needs unique id (use timestamp + random)
- User messages: type='human'
- AI responses: type='ai'
- Timestamp format: new Date().toISOString()

Import types from @file:src/types/chat.ts
Add comprehensive JSDoc comments.
```

**✅ Checkpoint 8**: Custom hook creado

---

## 🖼️ Fase 4: Componentes de UI

### Step 4.1: MessageBubble Component

**Objetivo**: Componente para mostrar un mensaje individual.

**Prompt para Cursor** (crea `src/components/chat/MessageBubble.tsx`):
```markdown
Create a MessageBubble component to display a single chat message.

Props:
- message: Message (from @file:src/types/chat.ts)

Visual design:
User messages (type='human'):
- Background: bolivar-green gradient
- Text: white
- Align: right (ml-auto)
- Rounded: rounded-2xl rounded-br-sm
- Max width: 80%
- Icon: 👤 before message

AI messages (type='ai'):
- Background: white
- Border: 2px bolivar-yellow
- Text: gray-800
- Align: left (mr-auto)
- Rounded: rounded-2xl rounded-bl-sm
- Max width: 80%
- Icon: 🤖 before message

Both:
- Show timestamp at bottom (small, gray)
- Format: HH:MM (use date-fns or Intl.DateTimeFormat)
- Fade-in animation when mounted
- Padding: p-4
- Shadow on hover

Use Tailwind CSS classes.
Make it a client component ('use client').
Export as default.
```

**✅ Checkpoint 9**: MessageBubble component creado

---

### Step 4.2: MessageList Component

**Objetivo**: Lista de mensajes con auto-scroll.

**Prompt para Cursor** (crea `src/components/chat/MessageList.tsx`):
```markdown
Create a MessageList component to display all chat messages.

Props:
- messages: Message[] (from @file:src/types/chat.ts)
- isLoading: boolean

Functionality:
1. Map through messages and render MessageBubble for each
2. Show loading indicator when isLoading=true (three dots animation)
3. Auto-scroll to bottom when new messages arrive
4. If messages empty: show welcome message with icon

Auto-scroll implementation:
- Use useRef for container
- Use useEffect that triggers on messages change
- Scroll to bottom smoothly

Container styling:
- Height: h-[500px]
- Overflow: overflow-y-auto
- Padding: p-4
- Background: gradient from gray-50 to white
- Custom scrollbar (thin, green)

Loading indicator:
- Three dots that bounce
- Green color
- At the bottom (AI side)

Welcome message (empty state):
- Centered vertically and horizontally
- Icon: 🛡️ (large)
- Title: "Bienvenido a Seguros Bolívar"
- Subtitle: "Escribe tu pregunta para comenzar"
- Green accent color

Import MessageBubble from same directory.
Use 'use client' directive.
Add TypeScript types and JSDoc.
```

**✅ Checkpoint 10**: MessageList component creado

---

### Step 4.3: InputArea Component

**Objetivo**: Input para enviar mensajes.

**Prompt para Cursor** (crea `src/components/chat/InputArea.tsx`):
```markdown
Create an InputArea component for sending chat messages.

Props:
- onSendMessage: (message: string) => Promise<void>
- isLoading: boolean
- error: string | null

Features:
1. Textarea for message input
   - Placeholder: "Escribe tu pregunta sobre seguros..."
   - Auto-resize (max 150px height)
   - Disabled when isLoading

2. Send button
   - Icon: ➤ (send arrow)
   - Text: "Enviar"
   - Disabled when: input empty OR isLoading
   - Loading state: show spinner instead of icon
   - Colors: bolivar-green background, white text

3. Character counter
   - Show: current/500
   - Warning if >450 (yellow text)
   - Error if >=500 (red text, block send)

4. Error display
   - Show error message if props.error exists
   - Red background, white text
   - Dismissible (X button)

Behavior:
- Submit on button click
- Submit on Cmd/Ctrl+Enter
- Clear input after successful send
- Focus input after send

Layout:
- Card component from Shadcn
- Input and button in a row
- Counter and error below
- Sticky to bottom on mobile

Use Shadcn components: Card, Textarea, Button
Use 'use client' directive.
Handle form submission properly (preventDefault).
TypeScript + JSDoc comments.
```

**✅ Checkpoint 11**: InputArea component creado

---

### Step 4.4: ChatContainer Component

**Objetivo**: Componente principal que ensambla todo.

**Prompt para Cursor** (crea `src/components/chat/ChatContainer.tsx`):
```markdown
Create a ChatContainer component that brings everything together.

No props needed (manages its own state).

Implementation:
1. Generate unique threadId on mount
   - Format: "nextjs_{timestamp}"
   - Use useState to store

2. Use the useChat hook from @file:src/hooks/useChat.ts
   - Pass the threadId
   - Destructure: messages, isLoading, error, sendMessage

3. Render structure:
   - Header section:
     * Logo/Icon: 🛡️
     * Title: "Seguros Bolívar Chat"
     * Subtitle: "Asistente Virtual"
     * Styled with bolivar-green background, white text
   
   - MessageList section:
     * Pass messages and isLoading
   
   - InputArea section:
     * Pass onSendMessage={sendMessage}, isLoading, error

Styling:
- Container: max-w-4xl, mx-auto, my-8
- Card wrapper with shadow
- Header: sticky top, z-10
- Responsive padding

Use components from:
- @file:src/components/chat/MessageList.tsx
- @file:src/components/chat/InputArea.tsx
- Shadcn Card component

Use 'use client' directive.
TypeScript + JSDoc.
Export as default.
```

**✅ Checkpoint 12**: ChatContainer component creado

---

## 📄 Fase 5: Páginas y Layout

### Step 5.1: Layout Principal

**Objetivo**: Configurar layout global de la app.

**Prompt para Cursor** (abre `src/app/layout.tsx`):
```markdown
Update the root layout with:

Metadata:
- title: "Seguros Bolívar - Chat con IA"
- description: "Asistente virtual de seguros powered by AI"

Body:
- Keep the children prop
- Add a simple footer:
  * Text: "© 2024 Seguros Bolívar - Powered by Cursor AI"
  * Centered, small text, gray
  * Padding top

Styling:
- Background: white
- Min height: 100vh
- Font: use system fonts (already configured)

Keep it clean and simple.
This should be a Server Component (no 'use client').
```

**✅ Checkpoint 13**: Layout configurado

---

### Step 5.2: Página Principal

**Objetivo**: Página principal con el chat.

**Prompt para Cursor** (abre `src/app/page.tsx`):
```markdown
Replace the entire content of this page with:

1. Import ChatContainer from @file:src/components/chat/ChatContainer.tsx
2. Simple layout:
   - Container: centered, padded
   - Title section (optional, can be part of ChatContainer header)
   - ChatContainer component

Keep it minimal - the ChatContainer has most of the UI.

This can be a Server Component (no 'use client').
The interactive parts are in ChatContainer which is a client component.

Add proper TypeScript types.
```

**✅ Checkpoint 14**: Página principal lista

---

## 🧪 Fase 6: Testing y Refinamiento

### Step 6.1: Probar Localmente

```bash
cd app
npm run dev
```

Abre http://localhost:3000

**Pruebas a realizar**:
1. ✅ App carga sin errores
2. ✅ UI se ve bien (colores, layout)
3. ✅ Puedes escribir en el textarea
4. ✅ Botón enviar funciona
5. ✅ Mensaje aparece en el chat
6. ✅ Loading indicator se muestra
7. ✅ Respuesta del AI aparece
8. ✅ Manejo de errores funciona
9. ✅ Responsive en móvil

**Si algo no funciona**: usa Cursor Chat para debuggear.

**Ejemplo de prompt de debugging**:
```markdown
I'm getting this error: [paste error]

In this file: [paste filename]

Help me understand what's wrong and how to fix it.
The app should [describe expected behavior].
```

---

### Step 6.2: Mejoras Opcionales

Si todo funciona y quieres mejorar:

#### Mejora 1: Markdown en Respuestas

**Prompt**:
```markdown
Update MessageBubble component to render AI responses with markdown formatting.

Install and use react-markdown library.
Support:
- Bold, italic
- Lists (bullets and numbered)
- Code blocks with syntax highlighting
- Links

Only for AI messages, not user messages.
```

#### Mejora 2: Indicador de Escritura

**Prompt**:
```markdown
Add a "typing indicator" that shows when AI is responding.

Show three animated dots in a message bubble.
Use the same styling as AI messages.
Show when isLoading=true in MessageList.
```

#### Mejora 3: Persistencia Local

**Prompt**:
```markdown
Add localStorage persistence for chat history.

Save messages to localStorage on every change.
Load messages on mount if they exist.
Key: `seguros-chat-${threadId}`
Clear on new session (new threadId).
```

#### Mejora 4: Sound Effects (Opcional)

**Prompt**:
```markdown
Add subtle sound effects:
- Soft "ding" when message sent
- Soft "pop" when AI responds

Use Web Audio API.
Make it toggleable with a button.
Keep sounds subtle and pleasant.
```

---

## 🎨 Fase 7: Polish UI/UX

### Step 7.1: Animaciones

**Prompt para Cursor**:
```markdown
Enhance the app with subtle animations:

1. Message bubbles: fade-in + slide-up when they appear
2. Send button: scale pulse effect on hover
3. Input focus: subtle glow effect
4. Loading dots: smooth bounce animation
5. Error messages: shake animation

Use Tailwind's animation utilities or Framer Motion (your choice).
Keep animations subtle and performant.
```

### Step 7.2: Accesibilidad

**Prompt para Cursor**:
```markdown
Improve accessibility across the app:

1. Add proper ARIA labels to buttons and inputs
2. Ensure keyboard navigation works (Tab, Enter, Esc)
3. Add focus indicators (visible outlines)
4. Ensure color contrast meets WCAG AA standards
5. Add loading announcements for screen readers

Test with keyboard-only navigation.
```

### Step 7.3: Responsive Mobile

**Prompt para Cursor**:
```markdown
Optimize for mobile devices:

1. Chat container: full width on mobile, fixed width on desktop
2. Input area: sticky to bottom on mobile
3. Messages: better spacing on small screens
4. Header: compact on mobile
5. Touch-friendly button sizes (min 44px)

Test on different viewport sizes.
Add proper viewport meta tag if missing.
```

---

## 🐛 Troubleshooting Común

### Error: "Module not found"

**Solución con Cursor**:
```markdown
I'm getting "Module not found" error for [module name].

Check:
1. Is it installed in package.json?
2. Is the import path correct?
3. Do I need to install it?

If it needs installation, show me the command.
```

### Error: TypeScript Types

**Solución con Cursor**:
```markdown
Fix TypeScript errors in this file.

Errors: [paste error messages]

Ensure proper types from @file:src/types/chat.ts are used.
```

### Error: API No Conecta

**Solución**:
1. Verifica backend corriendo: `curl http://localhost:8000/health`
2. Verifica .env.local tiene la URL correcta
3. Revisa CORS en el backend

**Prompt para Cursor**:
```markdown
Debug API connection issue.

Symptoms: [describe what's happening]
Expected: Should connect to http://localhost:8000/chat

Check @file:src/lib/api.ts for issues.
Add console.logs to debug the request.
```

### UI No Se Ve Bien

**Prompt para Cursor**:
```markdown
The UI doesn't look right: [describe issue]

Expected design:
- [what it should look like]

Current file: @file:[your-component]

Fix the Tailwind classes to match the design.
```

---

## ✅ Checklist Final

Antes de continuar a deployment:

```
✅ App corre sin errores (npm run dev)
✅ TypeScript compila sin errores (npm run build)
✅ Puedes enviar y recibir mensajes
✅ Loading states funcionan
✅ Error handling funciona
✅ UI se ve bien en desktop
✅ UI se ve bien en mobile
✅ Colores corporativos aplicados
✅ Animaciones sutiles presentes
✅ Código está comentado y limpio
```

---

## 📊 Comparación: Cursor vs Traditional Dev

### Tiempo Estimado

| Fase | Tradicional | Con Cursor | Ahorro |
|------|-------------|------------|--------|
| Setup | 30 min | 5 min | 83% |
| Components | 4 horas | 1 hora | 75% |
| Styling | 2 horas | 30 min | 75% |
| Debugging | 1 hora | 15 min | 75% |
| **Total** | **~7.5 horas** | **~2 horas** | **~73%** |

### Lines of Code Written Manually

| Método | Manual LOC | Porcentaje |
|--------|------------|------------|
| Traditional | 800-1000 | 100% |
| Con Cursor | 100-150 | ~15% |

**Conclusión**: Cursor te hace ~5x más productivo en este tipo de proyecto.

---

## 🎓 Lo Que Aprendiste

Ahora sabes cómo:

- ✅ Usar Cursor para generar código production-ready
- ✅ Iterar con prompts para refinar resultados
- ✅ Construir apps Next.js con TypeScript
- ✅ Implementar custom hooks en React
- ✅ Integrar APIs REST
- ✅ Manejar estados complejos (loading, errors, data)
- ✅ Diseñar UIs modernas con Tailwind
- ✅ Debuggear con asistencia de IA

---

## 🚀 Próximo Paso

Tu app está funcionando localmente. Es hora de llevarla a producción.

**👉 Continúa con [`4_DEPLOYMENT_GUIDE.md`](./4_DEPLOYMENT_GUIDE.md)** para containerizar y deployar tu aplicación.

---

<div align="center">

**¡Felicidades! Has construido una app real con Cursor AI 🎉**

*Ahora toca compartirla con el mundo 🌍*

</div>

