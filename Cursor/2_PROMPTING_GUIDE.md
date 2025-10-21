# 2️⃣ Prompting Guide - El Arte de Hablar con IA

Aprender a escribir buenos prompts es la skill más importante cuando trabajas con IA. Este módulo te enseña cómo.

---

## 🎯 ¿Por Qué Importa el Prompting?

### La Realidad
```
Mismo dev + Prompt malo = Código mediocre en 30 minutos
Mismo dev + Prompt bueno = Código excelente en 5 minutos
```

El prompting efectivo es como saber hacer las preguntas correctas a un ingeniero senior.

### Analogía
```
Prompt malo: "Dame comida"
   → IA confundida, resultado aleatorio

Prompt bueno: "Prepara pasta carbonara para 2 personas, 
              con panceta, sin crema, al estilo italiano tradicional"
   → IA sabe exactamente qué hacer
```

---

## 📐 Anatomía de un Buen Prompt

### Formula BASE

```
[CONTEXTO] + [TAREA] + [ESPECIFICACIONES] + [RESTRICCIONES]
```

### Ejemplo Desglosado

```markdown
[CONTEXTO]
Estoy construyendo un chat app con Next.js 14 y TypeScript.

[TAREA]
Crea un componente MessageBubble

[ESPECIFICACIONES]
- Acepta props: content (string), isUser (boolean), timestamp (Date)
- Si isUser=true: fondo verde, alineado a la derecha
- Si isUser=false: fondo blanco con borde amarillo, alineado a la izquierda
- Muestra timestamp en formato HH:MM
- Usa Tailwind CSS

[RESTRICCIONES]
- No uses librerías externas adicionales
- Debe ser un Server Component de Next.js
```

---

## ✅ Principios de Prompts Efectivos

### 1. Sé Específico, No Vago

#### ❌ Malo
```
"make a button"
```
**Problema**: Demasiado vago. ¿Qué tipo? ¿Qué hace? ¿Qué estilo?

#### ✅ Bueno
```
"Create a primary CTA button with:
- Text 'Enviar Mensaje'
- Green background (#00A651)
- White text
- Rounded corners (8px)
- onClick handler that calls submitMessage()
- Disabled state when isLoading is true
- Use Tailwind CSS classes"
```

### 2. Da Contexto del Proyecto

#### ❌ Malo
```
"create an API call"
```

#### ✅ Bueno
```
"Create an API call to POST http://localhost:8000/chat
In this Next.js 14 app, using fetch with:
- JSON body: { message: string, thread_id: string }
- Headers: Content-Type application/json
- Error handling for network errors
- TypeScript types based on types/api.ts
- Follow the pattern used in lib/api.ts for other endpoints"
```

### 3. Proporciona Ejemplos

#### ❌ Malo
```
"style this component"
```

#### ✅ Bueno
```
"Style this LoginForm component similar to the RegisterForm 
in @file:components/auth/RegisterForm.tsx
Use the same:
- Card layout
- Input styling
- Button colors
- Error message display
But adapt it for email/password instead of full registration"
```

### 4. Define Comportamiento Esperado

#### ❌ Malo
```
"add validation"
```

#### ✅ Bueno
```
"Add form validation that:
1. Shows error messages below each field
2. Prevents submit if any field is invalid
3. Email must be valid format (user@domain.com)
4. Password must be 8+ characters
5. Errors only show after user touches the field
6. Submit button is disabled while invalid
Use Zod for validation schema"
```

### 5. Itera y Refina

No esperes perfección en el primer intento. Construye incrementalmente:

```
Prompt 1: "Create a basic chat message component"
→ Cursor genera versión básica

Prompt 2: "Add timestamp display at the bottom"
→ Cursor añade timestamps

Prompt 3: "Make timestamps show only on hover"
→ Cursor refina el comportamiento

Prompt 4: "Add fade-in animation when message appears"
→ Cursor añade animación
```

---

## 🎨 Patrones de Prompts Útiles

### Pattern 1: "Como X pero con Y"

Reutiliza patrones existentes:

```
"Create a UserCard component like PostCard in @file:components/PostCard.tsx
but display user info (name, avatar, bio) instead of post content"
```

**Cuándo usar**: Cuando quieres mantener consistencia de diseño.

### Pattern 2: "Implementa X según Y estándar"

Usa convenciones conocidas:

```
"Implement error handling following the React Error Boundary pattern.
Show a fallback UI and log errors to console.
Allow users to retry the failed operation."
```

**Cuándo usar**: Para seguir best practices establecidas.

### Pattern 3: "Refactoriza X para Y"

Mejora código existente:

```
"Refactor this component to:
1. Extract the fetch logic into a custom hook
2. Use React Query for caching
3. Add optimistic updates
4. Maintain the same UI behavior"
```

**Cuándo usar**: Para mejorar código que ya funciona.

### Pattern 4: "Explícame X y luego implementa Y"

Aprende mientras construyes:

```
"Explain how React.memo works and when to use it.
Then apply it to the MessageList component to prevent 
unnecessary re-renders when new messages arrive."
```

**Cuándo usar**: Cuando quieres aprender y aplicar.

### Pattern 5: "Usando X librería, crea Y"

Especifica tecnologías:

```
"Using Shadcn/ui Dialog component, create a confirmation modal that:
- Shows a title and message
- Has Cancel and Confirm buttons
- Accepts onConfirm callback
- Can be triggered from parent component
Follow Shadcn/ui patterns from @docs"
```

**Cuándo usar**: Cuando quieres usar herramientas específicas.

---

## 🔧 Técnicas Avanzadas

### 1. Chain of Thought Prompting

Pide que Cursor "piense en voz alta":

```
"Before implementing, first explain:
1. What data structures we'll need
2. How the component will manage state
3. What edge cases we should handle
4. Then implement the solution"
```

**Beneficio**: Código más pensado y robusto.

### 2. Few-Shot Examples

Proporciona ejemplos múltiples:

```
"Create API functions following these patterns:

Example 1:
export async function getUsers() {
  const res = await fetch(`${API_URL}/users`);
  return res.json();
}

Example 2:
export async function getUser(id: string) {
  const res = await fetch(`${API_URL}/users/${id}`);
  return res.json();
}

Now create: deleteUser(id: string) and updateUser(id, data)"
```

### 3. Negative Instructions

Dile qué NO hacer:

```
"Create a loading spinner component.
DO NOT use external libraries like react-spinners.
DO NOT use gifs or images.
Use only CSS animations with Tailwind classes."
```

### 4. Conditional Logic in Prompts

Maneja casos complejos:

```
"Create a notification system where:
- If type='success': green background, checkmark icon
- If type='error': red background, X icon
- If type='warning': yellow background, exclamation icon
- If dismissible=true: show close button
- If autoHide=true: fade out after 3 seconds"
```

### 5. Reference Multiple Files

Construye sobre código existente:

```
"Create a new ChatMessage component that combines:
- Layout structure from @file:components/ui/card.tsx
- Animation patterns from @file:components/animations.ts
- Type definitions from @file:types/chat.ts
- Styling approach from @file:app/globals.css"
```

---

## 📊 Ejercicios Prácticos

### Ejercicio 1: Reescribe el Malo

Convierte prompts vagos en específicos:

#### Prompt Malo #1
```
"create a form"
```

**Tu turno**: Reescribe para crear un contact form específico.

<details>
<summary>Solución sugerida</summary>

```
"Create a contact form component with:
- Fields: name (text), email (email), message (textarea)
- Client-side validation (all required, email format)
- Submit button that calls onSubmit prop
- Loading state during submission
- Success/error message display
- Styled with Tailwind, responsive design
- TypeScript types for form data
- Use controlled inputs with React state"
```
</details>

#### Prompt Malo #2
```
"fix the bug"
```

**Tu turno**: Reescribe para describir específicamente qué bug.

<details>
<summary>Solución sugerida</summary>

```
"Fix the bug in MessageList component where:
- Issue: Messages don't auto-scroll to bottom when new ones arrive
- Expected: Container should scroll to show latest message
- Current behavior: User must manually scroll
- File: components/MessageList.tsx
- Likely solution: Use useEffect with ref to scrollIntoView"
```
</details>

### Ejercicio 2: Prompt Progressive Refinement

Practica la iteración. Empieza con:

```
"Create a button"
```

Ahora refina 3 veces, cada vez añadiendo más detalles:

**Iteración 1**:
```
"Create a button component that accepts label and onClick props"
```

**Iteración 2**:
```
"Create a reusable button component that accepts:
- label (string)
- onClick (function)
- variant ('primary' | 'secondary' | 'danger')
- disabled (boolean)"
```

**Iteración 3**:
```
"Create a reusable button component with:
Props:
- label: string
- onClick: () => void
- variant: 'primary' | 'secondary' | 'danger'
- disabled: boolean
- isLoading: boolean (shows spinner)
- fullWidth: boolean

Styling:
- Primary: green bg, white text
- Secondary: white bg, green border
- Danger: red bg, white text
- Rounded corners, shadow on hover
- Disabled: gray bg, cursor not-allowed
- Loading: show spinner, disable clicks

Use Tailwind CSS and TypeScript"
```

### Ejercicio 3: Prompt con Contexto

**Escenario**: Tienes un proyecto de e-commerce. Necesitas un ProductCard.

Escribe un prompt que incluya:
1. Contexto del proyecto
2. Diseño específico que quieres
3. Interacciones necesarias
4. Tecnologías a usar

<details>
<summary>Solución sugerida</summary>

```
"Context: I'm building an e-commerce app with Next.js 14, TypeScript, and Tailwind.

Create a ProductCard component that:

Data displayed:
- Product image (use Next.js Image component)
- Product name (h3)
- Price (formatted as $XX.XX)
- Rating (1-5 stars)
- 'Add to Cart' button

Behavior:
- Image hover: slight zoom effect
- Click card: navigate to /products/[id]
- Click 'Add to Cart': call addToCart(productId)
- Show loading spinner on button when adding

Styling:
- White card with shadow
- Hover: lift effect (translateY)
- Rounded corners (12px)
- Responsive: full width on mobile, fixed width on desktop
- Use our brand colors: primary #00A651

Types:
Create TypeScript interface for Product with:
id, name, price, imageUrl, rating

Follow the component pattern from @file:components/ui/card.tsx"
```
</details>

---

## 🚫 Errores Comunes y Cómo Evitarlos

### Error #1: Prompts Demasiado Largos

#### ❌ Problema
```
"Create a full authentication system with login, register, forgot password,
email verification, 2FA, social login with Google and GitHub, JWT tokens,
refresh tokens, role-based access control, user profiles, password strength
checker, rate limiting, CSRF protection... [continúa 300 palabras más]"
```

**Por qué es malo**: Cursor se abruma, el resultado es incompleto o mal estructurado.

#### ✅ Solución
Divide en pasos:
```
Step 1: "Create basic login form with email/password"
Step 2: "Add form validation with Zod"
Step 3: "Implement JWT authentication flow"
Step 4: "Add refresh token logic"
...etc
```

### Error #2: Asumir Conocimiento Implícito

#### ❌ Problema
```
"Use our standard pattern"
```

**Por qué es malo**: Cursor no sabe cuál es "el patrón estándar".

#### ✅ Solución
```
"Follow the API call pattern from @file:lib/api.ts where we:
1. Wrap calls in try-catch
2. Use custom ApiError class
3. Log errors to console.error
4. Return { data, error } object"
```

### Error #3: No Especificar el Output Deseado

#### ❌ Problema
```
"improve this code"
```

**Por qué es malo**: "Mejor" es subjetivo.

#### ✅ Solución
```
"Refactor this code to:
1. Reduce from 50 to <30 lines
2. Extract repeated logic into helper functions
3. Add TypeScript types for all parameters
4. Improve variable names for clarity
5. Add JSDoc comments for public functions"
```

### Error #4: Ignorar el Contexto del Proyecto

#### ❌ Problema
```
"Create a modal component"
```

**Por qué es malo**: Cursor podría usar una librería diferente a las que ya tienes.

#### ✅ Solución
```
"Create a modal using the Shadcn/ui Dialog component (already installed).
Follow the pattern from @file:components/ui/dialog.tsx.
Make it work with our existing theme variables from globals.css."
```

### Error #5: Pedir Soluciones Mágicas

#### ❌ Problema
```
"make the app 10x faster"
```

**Por qué es malo**: Demasiado vago, no actionable.

#### ✅ Solución
```
"Optimize performance of MessageList component:
1. Implement React.memo to prevent unnecessary re-renders
2. Use virtualization (react-window) for long message lists
3. Lazy load images with Next.js Image
4. Debounce scroll event handlers
5. Move expensive computations to useMemo"
```

---

## 🎯 Templates de Prompts Listos para Usar

### Template: Nuevo Componente

```markdown
Create a [COMPONENT_NAME] component for [PURPOSE].

Tech stack:
- [Framework/Library]
- [Styling approach]
- [State management]

Props:
- [prop1]: [type] - [description]
- [prop2]: [type] - [description]

Behavior:
- [User interaction 1] → [Result]
- [User interaction 2] → [Result]

Styling:
- [Visual aspect 1]
- [Visual aspect 2]
- [Responsive behavior]

Follow patterns from: @file:[reference-file]
```

### Template: Refactoring

```markdown
Refactor [FILE/COMPONENT] to [GOAL].

Current issues:
- [Problem 1]
- [Problem 2]

Desired improvements:
- [Improvement 1]
- [Improvement 2]

Constraints:
- Don't change [what should stay the same]
- Maintain [existing behavior/API]
- Use [specific approach/pattern]
```

### Template: Bug Fix

```markdown
Fix bug in [COMPONENT/FILE]:

Symptoms:
- [What's going wrong]
- [When it happens]
- [Error messages if any]

Expected behavior:
- [What should happen instead]

Debugging info:
- [Relevant state/props values]
- [Console errors]

Potential cause:
- [Your hypothesis]
```

### Template: Feature Addition

```markdown
Add [FEATURE_NAME] to [EXISTING_COMPONENT/SYSTEM].

Current state:
- [How it works now]

Desired addition:
- [What you want to add]

Integration requirements:
- [How it should fit with existing code]
- [What shouldn't break]

Technical approach:
- [Preferred implementation method]
```

### Template: Learning + Building

```markdown
I need to understand [CONCEPT/PATTERN] and apply it.

Context:
- [What I'm building]
- [Current implementation]
- [Why I need this concept]

Please:
1. Explain [CONCEPT] briefly with an example
2. Show how it applies to my specific case
3. Implement it in [FILE/COMPONENT]

Keep explanation concise but clear.
```

---

## 🧪 Prueba Tus Skills

### Challenge: Escribe el Prompt Perfecto

**Escenario**:
Necesitas un custom hook para manejar chat messages que:
- Envía mensajes a la API
- Mantiene historial local
- Maneja loading y errors
- Usa TypeScript

**Tu turno**: Escribe el prompt antes de ver la solución.

<details>
<summary>Solución Experta</summary>

```markdown
Create a custom React hook useChat for managing chat interactions.

Context:
- Next.js 14 app with TypeScript
- API endpoint: POST http://localhost:8000/chat
- Using types from @file:types/chat.ts

Hook signature:
export function useChat(threadId: string)

Return object:
{
  messages: Message[],           // Chat history
  sendMessage: (text: string) => Promise<void>,
  isLoading: boolean,            // True when sending
  error: string | null,          // Error message if any
  clearError: () => void
}

Behavior:
1. Initialize with empty messages array
2. When sendMessage called:
   - Add user message to local state immediately
   - Set isLoading = true
   - POST to API with { message, thread_id }
   - On success: add AI response to messages
   - On error: set error message, remove user message
   - Finally: set isLoading = false
3. Store messages in local state (useState)

Error handling:
- Network errors: "No se pudo conectar con el servidor"
- Timeout: "La solicitud tardó demasiado"
- Other: Show error message from API

Types to use:
- Message: { type: 'human' | 'ai', content: string, timestamp: string }
- API response: { response: string }

Follow React hooks best practices:
- Use useCallback for sendMessage
- Proper dependency arrays
- Clean up on unmount if needed
```
</details>

---

## 📚 Recursos para Mejorar

### Documentación Oficial
- [Cursor Prompting Best Practices](https://docs.cursor.com/prompting)
- [OpenAI Prompt Engineering Guide](https://platform.openai.com/docs/guides/prompt-engineering)

### Comunidades
- [r/cursor subreddit](https://reddit.com/r/cursor)
- [Cursor Discord #prompting channel](https://discord.gg/cursor)

### Práctica
La mejor forma de mejorar es **practicar constantemente**:
1. Escribe un prompt
2. Ve el resultado
3. Analiza qué funcionó y qué no
4. Refina y prueba de nuevo
5. Repite

---

## ✅ Checklist de Dominio

Antes de continuar, asegúrate de poder:

```
✅ Escribir prompts con las 4 partes: Contexto, Tarea, Specs, Restricciones
✅ Usar @ mentions efectivamente (@file, @codebase, @docs)
✅ Iterar prompts para refinar resultados
✅ Proporcionar ejemplos en tus prompts
✅ Evitar los 5 errores comunes
✅ Adaptar templates para tus necesidades
✅ Dividir tareas complejas en prompts incrementales
```

---

## ⏭️ Siguiente Paso

Ya dominas el arte del prompting. Es hora de construir algo real.

**👉 Continúa con [`3_BUILD_GUIDE.md`](./3_BUILD_GUIDE.md)** para construir la aplicación completa paso a paso.

---

<div align="center">

**El prompting efectivo es un superpoder. Úsalo sabiamente. 🧙‍♂️✨**

</div>

