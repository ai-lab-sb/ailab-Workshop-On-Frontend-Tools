# 1️⃣ Cursor Basics - Introducción a la Herramienta

Bienvenido a Cursor, el IDE que revoluciona la forma en que escribimos código.

---

## 🤔 ¿Qué es Cursor?

**Cursor** es un editor de código construido sobre Visual Studio Code, pero con **superpoderes de IA** integrados nativamente.

### La Diferencia Clave
- **VS Code + Copilot**: Autocompletado inteligente
- **Cursor**: Autocompletado + Chat contextual + Edición multi-archivo + Comprensión del codebase completo

### Analogía Simple
```
VS Code + Copilot = Calculadora inteligente
Cursor = Ingeniero de software junior trabajando contigo
```

---

## 🚀 ¿Por Qué Usar Cursor?

### Para Principiantes
- ✅ Aprende mientras construyes
- ✅ Menos sintaxis que memorizar
- ✅ Explica código que no entiendes
- ✅ Sugiere mejores prácticas
- ✅ Menos tiempo en Stack Overflow

### Para Desarrolladores Experimentados
- ⚡ 3-10x más rápido
- 🧠 Menos contexto switching
- 🐛 Debugging asistido
- 📚 No memorizar APIs nuevas
- 🎯 Más tiempo en lógica de negocio

### Casos de Uso Reales
```
❌ Antes: "¿Cómo hago X en React? *googlea 20 minutos*"
✅ Con Cursor: Cmd+K "Add a loading spinner when fetching data"

❌ Antes: *Copia código de Stack Overflow y adapta 30 min*
✅ Con Cursor: Chat "Create a custom hook for API calls with retry logic"

❌ Antes: *Lee documentación de librería nueva 1 hora*
✅ Con Cursor: "Use the Shadcn dialog component here"
```

---

## 🛠️ Instalación y Setup

### Paso 1: Descargar Cursor

1. Ve a [https://cursor.sh](https://cursor.sh)
2. Descarga para tu sistema operativo
3. Instala como cualquier aplicación

**Tiempo**: 5 minutos

### Paso 2: Configuración Inicial

Al abrir Cursor por primera vez:

```
1. Migrará automáticamente tu configuración de VS Code (si lo tienes)
2. Te pedirá login (opcional pero recomendado)
3. Ofrecerá tour guiado (tómalo si eres nuevo)
```

### Paso 3: Configurar AI Model

```
Settings → Cursor → AI Model
```

**Opciones**:
- **Claude-4.5** (recomendado): Más inteligente, más lento, requiere suscripción
- **GPT-3.5**: Más rápido, gratis en plan básico
- **Claude**: Bueno para código, alternativa


### Paso 4: Plan y Pricing

```
🆓 Free Tier
- 2,000 completions/mes
- GPT-3.5
- Features básicos
- Perfecto para aprender

💰 Pro ($20/mes)
- Unlimited completions
- GPT-4 access
- Prioridad en respuestas
- Recomendado para profesionales
```

**Para este workshop**: El tier gratuito es suficiente.

---

## 🎯 Features Principales

### 1. **Cmd+K (Ctrl+K en Windows)** - Edición Inline

La feature más poderosa de Cursor.

**Cómo funciona**:
```
1. Selecciona código (o no selecciones nada)
2. Presiona Cmd+K
3. Escribe qué quieres hacer
4. Cursor edita el código en el lugar
```

**Ejemplos prácticos**:

```typescript
// Tienes esto:
function getUserData() {
  // TODO: implementar
}

// 1. Selecciona la función
// 2. Cmd+K
// 3. Escribe: "fetch user data from /api/users with error handling"
// 4. Cursor genera:

async function getUserData() {
  try {
    const response = await fetch('/api/users');
    if (!response.ok) {
      throw new Error(`HTTP error! status: ${response.status}`);
    }
    const data = await response.json();
    return data;
  } catch (error) {
    console.error('Error fetching user data:', error);
    throw error;
  }
}
```

**Más ejemplos de Cmd+K**:
- "Add TypeScript types"
- "Extract this into a separate component"
- "Add error handling"
- "Make this responsive"
- "Add comments explaining this"

### 2. **Cursor Chat** - Conversación Contextual

Chat que entiende TODO tu proyecto.

**Cómo acceder**:
- Cmd+L (Ctrl+L en Windows)
- O click en el icono de chat

**Superpoder**: Puedes hacer @ mentions:
- `@codebase`: Busca en todo tu código
- `@file`: Referencias un archivo específico
- `@docs`: Busca en documentación
- `@web`: Busca en internet

**Ejemplos prácticos**:

```
Tú: @codebase where do we handle API errors?
Cursor: *Encuentra y muestra los 3 lugares donde manejas errores de API*

Tú: @file:api.ts how does authentication work here?
Cursor: *Explica el flujo de auth en ese archivo específico*

Tú: @docs How do I use React.memo?
Cursor: *Busca en docs de React y te explica con ejemplos*
```

### 3. **Composer** - Edición Multi-Archivo

Edita múltiples archivos a la vez.

**Cómo usar**:
```
1. Cmd+I (Ctrl+I en Windows)
2. Describe qué quieres construir
3. Cursor edita/crea múltiples archivos
```

**Ejemplo real**:
```
Tú: "Create a login form with email/password fields, 
validation, and submit handler. Use Shadcn form components."

Cursor crea:
- components/LoginForm.tsx (el formulario)
- lib/validation.ts (esquemas de validación)
- app/login/page.tsx (la página)
- Actualiza types/index.ts (añade tipos)
```

**Cuándo usar**:
- Crear features completas
- Refactorings grandes
- Añadir testing a múltiples archivos
- Reestructurar proyecto

### 4. **Codebase Indexing** - Búsqueda Inteligente

Cursor indexa tu proyecto completo.

**Qué significa**:
- Entiende la estructura de tu código
- Sabe qué funciones existen
- Conoce tus dependencias
- Recuerda patrones que usas

**Beneficio práctico**:
```
Tú: "Create a button like the one in Header.tsx but with danger style"

Cursor:
1. Busca Header.tsx
2. Ve cómo están los botones ahí
3. Replica el patrón con el estilo danger
4. Mantiene consistencia con tu código
```

### 5. **Tab Autocomplete** - Como Copilot pero Mejor

Autocompletado mientras escribes.

**Diferencia con Copilot**:
- Más contexto de tu proyecto
- Aprende de tu estilo
- Sugiere basado en lo que hiciste antes

**Ejemplo**:
```typescript
// Escribes:
const handleSubmit = async (

// Cursor sugiere (Tab para aceptar):
const handleSubmit = async (e: React.FormEvent) => {
  e.preventDefault();
  // Tu código específico del proyecto
}
```

---

## 🎮 Práctica Hands-On

### Ejercicio 1: Primera Experiencia con Cmd+K

```typescript
// 1. Crea un archivo test.ts
// 2. Escribe esto:

function calculate() {
  // TODO
}

// 3. Selecciona la función
// 4. Cmd+K
// 5. Escribe: "calculate fibonacci of n recursively"
// 6. Observa cómo Cursor genera el código
```

### Ejercicio 2: Usando el Chat

```
1. Abre Cursor Chat (Cmd+L)
2. Pregunta: "How do I create a React component with TypeScript?"
3. Sigue con: "Now make it accept a name prop"
4. Y luego: "Add a click handler"
```

### Ejercicio 3: Composer Multi-File

```
1. Cmd+I
2. Escribe: "Create a simple counter component with increment, 
   decrement, and reset buttons. Put the component in 
   components/ and create a page that uses it in app/."
3. Observa cómo crea múltiples archivos
```

---

## 💡 Tips y Mejores Prácticas

### 1. Sé Específico
```
❌ Malo: "make this better"
✅ Bueno: "add loading state, error handling, and TypeScript types"
```

### 2. Da Contexto
```
❌ Malo: "create a button"
✅ Bueno: "create a primary button using our existing Button component 
          pattern from components/ui/button.tsx"
```

### 3. Itera
```
Primer prompt: "Create a login form"
Cursor genera código básico

Segundo prompt: "Add email validation"
Cursor mejora el código

Tercer prompt: "Add loading spinner when submitting"
Cursor añade esa feature
```

### 4. Usa @ Mentions
```
❌ Malo: "how does the API work?"
✅ Bueno: "@file:api.ts explain the authentication flow"
```

### 5. Aprende del Código Generado
No solo copies, lee y entiende:
- ¿Qué patrones usa?
- ¿Qué librerías importa?
- ¿Por qué estructuró así el código?

---

## 🔧 Configuración Avanzada

### Customizar el AI Behavior

```
Settings → Cursor → AI Settings
```

**Opciones útiles**:
- `Max Tokens`: Cuánto código puede generar (default: 4000)
- `Temperature`: Creatividad vs precisión (default: 0.3)
- `Include Diagnostics`: Incluir errores de TypeScript en contexto

### Keyboard Shortcuts Esenciales

```
Cmd+K (Ctrl+K)     → Inline edit
Cmd+L (Ctrl+L)     → Open chat
Cmd+I (Ctrl+I)     → Composer
Cmd+Shift+L        → New chat
Tab                → Accept suggestion
Esc                → Dismiss suggestion
```

### Files to Include/Ignore

Cursor respeta tu `.gitignore` pero puedes customizar:

```
.cursorignore
```

Ejemplo:
```
node_modules
.next
dist
*.log
```

---

## ❌ Errores Comunes y Cómo Evitarlos

### 1. Prompts Vagos
```
Problema: "make this work"
Solución: "Fix the TypeScript error on line 42 by adding proper types"
```

### 2. No Dar Contexto del Proyecto
```
Problema: Cursor genera código que no sigue tus patrones
Solución: Usa @codebase o menciona archivos específicos como ejemplo
```

### 3. Aceptar Todo Sin Revisar
```
Problema: Código generado tiene bugs o no es óptimo
Solución: SIEMPRE revisa el código, entiende qué hace, prueba que funciona
```

### 4. No Iterar
```
Problema: Primera respuesta no es perfecta y te frustras
Solución: Da feedback, pide ajustes, refina paso a paso
```

### 5. Usar para TODO
```
Problema: Dependencia excesiva de la IA
Solución: Usa Cursor para boilerplate y tareas repetitivas, 
          TÚ decides la arquitectura y lógica de negocio
```

---

## 🆚 Cursor vs Otras Herramientas

### Cursor vs GitHub Copilot

| Feature | Copilot | Cursor |
|---------|---------|--------|
| Autocomplete | ✅ | ✅ |
| Chat | ❌ | ✅ |
| Multi-file edit | ❌ | ✅ |
| Codebase search | ❌ | ✅ |
| Inline edit | ❌ | ✅ |
| Composer | ❌ | ✅ |
| Price | $10/mes | $0-20/mes |

**Veredicto**: Cursor es más potente para proyectos grandes.

### Cursor vs ChatGPT

| Aspecto | ChatGPT | Cursor |
|---------|---------|--------|
| Contexto proyecto | ❌ | ✅ |
| Edita archivos | ❌ | ✅ |
| Code execution | ❌ | ✅ |
| Copy-paste | Mucho | Ninguno |
| Integración IDE | ❌ | ✅ |

**Veredicto**: Cursor = ChatGPT integrado en tu workflow.

---

## 🎯 Checklist de Setup Completo

Antes de continuar al siguiente módulo, verifica:

```
✅ Cursor instalado y funcionando
✅ Probaste Cmd+K con un ejemplo
✅ Abriste Cursor Chat (Cmd+L) y preguntaste algo
✅ Experimentaste con Composer (Cmd+I)
✅ Entiendes @ mentions (@file, @codebase, @docs)
✅ Configuraste tu AI model preferido
✅ Leíste tips de mejores prácticas
```

---

## 📚 Recursos Adicionales

### Videos Recomendados
- [Cursor in 100 seconds](https://www.youtube.com/watch?v=xxx)
- [10 Cursor tips that changed my life](https://www.youtube.com/watch?v=xxx)
- [Building an app in 30 minutes with Cursor](https://www.youtube.com/watch?v=xxx)

### Documentación Oficial
- [Cursor Docs](https://docs.cursor.com/)
- [Keyboard Shortcuts](https://docs.cursor.com/get-started/shortcuts)
- [AI Features](https://docs.cursor.com/get-started/features)

### Comunidad
- [Cursor Community Forum](https://forum.cursor.sh/)
- [Cursor Discord](https://discord.gg/cursor)
- [Twitter/X](https://x.com/cursor_ai)

---

## ⏭️ Siguiente Paso

Ahora que entiendes las bases de Cursor, es hora de aprender a escribir prompts efectivos.

**👉 Continúa con [`2_PROMPTING_GUIDE.md`](./2_PROMPTING_GUIDE.md)**

---

<div align="center">

**¡Cursor es tu copiloto, pero TÚ eres el piloto! 🚀**

</div>

