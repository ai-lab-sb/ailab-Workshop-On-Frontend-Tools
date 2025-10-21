# 3️⃣ Build Guide - SegurosVida+ Chat

Construcción paso a paso del chat usando Lovable. Cada fase tiene prompts específicos en la carpeta `prompts/`.

---

## 🎯 Objetivo Final

Crear un chat conversacional que:
- Consume API `insurance_agent_api` (localhost:8000)
- Múltiples conversaciones (threads)
- UI moderna responsive
- Manejo de errores y loading

---

## ⚙️ Preparación

### 1. Backend Corriendo

```bash
cd insurance_agent_api/app
python main.py
```

Verifica en `http://localhost:8000/health` que responda OK.

### 2. Crear Proyecto en Lovable

1. Ve a [lovable.dev](https://lovable.dev)
2. Click "+ New Project"
3. Nombre: "SegurosVida Plus Chat"

---

## 📝 Fase 1: Proyecto Inicial

**Usa:** `prompts/01_initial_project.md`

**Prompt clave:**
```
Crea una aplicación de chat para seguros con:

Layout:
- Header fijo arriba con "SegurosVida+" y logo azul
- Área central para mensajes (scrollable)
- Input fijo abajo para escribir mensajes

Colores:
- Header: azul oscuro (#1e40af), texto blanco
- Fondo mensajes: gris muy claro (#f9fafb)
- Input: fondo blanco, borde gris

Funcionalidad básica:
- Input controlado con estado
- Al enviar (Enter o botón), mostrar mensaje simulado
- Limpiar input después de enviar
```

**Checkpoint:**
- ✅ Layout base funcional
- ✅ Input funciona
- ✅ Mensajes se muestran (simulados)

---

## 📝 Fase 2: Mejorar UI del Chat

**Usa:** `prompts/02_chat_interface.md`

**Prompt clave:**
```
Mejora la interfaz del chat:

Mensajes del usuario:
- Alineados a la derecha
- Fondo azul (#3b82f6), texto blanco
- Bordes redondeados, máx ancho 70%
- Muestra hora abajo (text-xs, gris claro)

Mensajes del agente:
- Alineados a la izquierda
- Fondo gris (#e5e7eb), texto negro
- Mismo estilo que usuario pero invertido
- Icono/avatar del agente

Mejoras:
- Scroll automático al último mensaje
- Animación fade-in al aparecer mensajes
- Placeholder input: "Pregunta sobre seguros..."
- Botón enviar con ícono (→ o avión)
```

**Checkpoint:**
- ✅ Chat se ve profesional
- ✅ Mensajes bien diferenciados
- ✅ Animaciones suaves

---

## 📝 Fase 3: Integración con API

**Usa:** `prompts/03_api_integration.md`

**Prompt clave:**
```
Conecta con API real del agente:

Configuración:
- URL base: http://localhost:8000
- Endpoint: POST /chat
- Body: { "message": string, "thread_id": string }

Funcionalidad:
1. Genera thread_id único al iniciar (uuid)
2. Al enviar mensaje:
   - Muestra inmediatamente mensaje usuario
   - Envía POST con message y thread_id
   - Mientras espera: muestra "Escribiendo..." con puntos animados
   - Al recibir respuesta: muestra mensaje del agente
   - Si error: muestra mensaje error en rojo

Manejo errores:
- Connection refused: "No se puede conectar. ¿Está corriendo el agente?"
- Timeout: "El agente tardó demasiado en responder"
- Otros: "Error inesperado: [mensaje]"

Estados:
- Deshabilita input mientras espera respuesta
- Spinner en botón enviar durante loading
```

**Checkpoint:**
- ✅ Se conecta con API real
- ✅ Respuestas del agente aparecen
- ✅ Errores se manejan bien
- ✅ Loading states funcionan

**🧪 Testing:**
- Envía: "¿Qué tipos de seguros ofrecen?"
- Verifica que responda con info de SegurosVida+
- Apaga el backend y verifica mensaje de error

---

## 📝 Fase 4: Múltiples Conversaciones

**Usa:** `prompts/04_multiple_threads.md`

**Prompt clave:**
```
Agrega sidebar para gestionar conversaciones:

Sidebar (izquierda, 300px):
- Botón "+ Nueva Conversación" arriba
- Lista de conversaciones:
  - Nombre: "Conversación 1", "Conversación 2"...
  - Preview último mensaje (max 50 caracteres)
  - Fecha de creación
  - Resalta la conversación activa
- Click en conversación: cambia a ese thread

Funcionalidad:
- Array en estado con todas las conversaciones
- Cada una tiene: id, nombre, mensajes[], creado
- Al crear nueva: genera nuevo thread_id
- Al cambiar conversación: carga sus mensajes
- Guarda todo en localStorage para persistencia

Responsive:
- Desktop: sidebar siempre visible
- Mobile: sidebar colapsable con botón hamburger
```

**Checkpoint:**
- ✅ Sidebar con lista de conversaciones
- ✅ Crear nueva conversación funciona
- ✅ Cambiar entre conversaciones funciona
- ✅ LocalStorage persiste datos

---

## 📝 Fase 5: Pulido Final

**Usa:** `prompts/05_final_polish.md`

**Prompt clave:**
```
Mejoras finales y pulido:

Header mejorado:
- Logo más profesional o ícono
- Opciones: botón "Limpiar chat actual"
- Indicador de conexión (verde: conectado, rojo: error)

Sidebar mejorado:
- Botón eliminar (🗑️) en cada conversación con confirmación
- Renombrar conversación (doble click en nombre)
- Buscar conversaciones (input filtro)

Experiencia usuario:
- Empty state: mensaje bienvenida cuando no hay mensajes
- Sugerencias de preguntas iniciales (botones clickeables):
  - "¿Qué tipos de seguros ofrecen?"
  - "¿Cuánto cuesta el seguro de auto?"
  - "¿Cómo puedo contactarlos?"
- Mostrar "✓✓" cuando mensaje se envió exitosamente

Estilos finales:
- Sombras más sutiles
- Transiciones suaves en todos los hovers
- Scroll suave
- Focus states en inputs
```

**Checkpoint:**
- ✅ App se ve pulida y profesional
- ✅ UX amigable con empty states
- ✅ Todas las micro-interacciones funcionan

---

## 🎨 Colores Finales SegurosVida+

```css
Primario: #1e40af (azul oscuro)
Secundario: #3b82f6 (azul)
Fondo: #f9fafb (gris muy claro)
Mensajes usuario: #3b82f6
Mensajes agente: #e5e7eb
Texto: #1f2937
Error: #ef4444
Success: #10b981
```

---

## 🔍 Testing Final

### Funcionalidad
- ✅ Enviar mensajes funciona
- ✅ Respuestas del agente llegan correctamente
- ✅ Crear múltiples conversaciones funciona
- ✅ Cambiar entre conversaciones mantiene contexto
- ✅ Errores se manejan apropiadamente

### UI/UX
- ✅ Responsive en mobile, tablet, desktop
- ✅ Animaciones suaves
- ✅ Loading states claros
- ✅ Empty states informativos

### Edge Cases
- ✅ Backend apagado muestra error
- ✅ Mensajes muy largos se formatean bien
- ✅ LocalStorage funciona (recarga página y datos persisten)

---

## 📸 Screenshots Esperados

**Desktop:**
```
┌────────────────────────────────────────────────────┐
│ 🏥 SegurosVida+                        [Verde: ●] │
├─────────────┬──────────────────────────────────────┤
│ + Nueva     │  ¡Hola! ¿En qué puedo ayudarte?    │
│             │                                      │
│ 📍 Conv. 1  │  👤 ¿Qué seguros ofrecen?      15:30│
│   "¿Qué..." │                                      │
│             │  🤖 Ofrecemos 5 tipos...       15:30│
│ 💬 Conv. 2  │                                      │
│   "¿Cuán.."│  [Más mensajes...]                   │
│             │                                      │
│             │  ┌────────────────────────────────┐ │
│             │  │ Pregunta sobre seguros... [→] │ │
│             │  └────────────────────────────────┘ │
└─────────────┴──────────────────────────────────────┘
```

---

## 🚀 Siguiente Paso

Una vez completada la app en Lovable, aprende a exportarla y correrla localmente.

**[Continuar: 4. GitHub & Export →](./4_GITHUB_EXPORT.md)**

---

## 💡 Tips

- **Itera gradualmente**: No intentes hacer todo perfecto en un prompt
- **Prueba constantemente**: Usa la preview para verificar cada cambio
- **Pide correcciones**: Si algo no sale bien, simplemente pide que lo arregle
- **Screenshots de referencia**: Muéstrale a Lovable ejemplos visuales si ayuda

**[← Prompting Guide](./2_PROMPTING_GUIDE.md)** | **[GitHub Export →](./4_GITHUB_EXPORT.md)**
