# Prompt 4: Múltiples Conversaciones

## 🎯 Objetivo
Permitir al usuario gestionar múltiples conversaciones simultáneas.

---

## 📝 Prompt para Lovable

```
Agrega un sidebar para gestionar múltiples conversaciones:

Sidebar (izquierda):
- Ancho: 300px en desktop
- Fondo blanco con borde derecho gris
- Botón "+ Nueva Conversación" en la parte superior:
  - Ancho completo
  - Fondo azul (#3b82f6)
  - Texto blanco
  - Padding 3
  - Bordes redondeados

Lista de conversaciones:
- Cada conversación muestra:
  - Nombre: "Conversación 1", "Conversación 2", etc.
  - Preview del último mensaje (máximo 50 caracteres + "...")
  - Fecha/hora de creación (formato: "DD/MM HH:MM")
  - Indicador de conversación activa (borde izquierdo azul grueso o fondo azul claro)
- Click en una conversación: cambia a esa conversación
- Hover: fondo gris claro

Estructura de datos:
- Array de conversaciones en el estado
- Cada conversación tiene:
  {
    id: "thread_id único",
    nombre: "Conversación N",
    mensajes: [],
    creado: timestamp,
    ultimoMensaje: "texto preview"
  }

Funcionalidad:
1. Al hacer click en "+ Nueva Conversación":
   - Genera nuevo thread_id
   - Crea nueva conversación en el array
   - Cambia a esa conversación (mensajes vacíos)
   - Incrementa contador (Conversación 2, 3, etc.)

2. Al hacer click en una conversación existente:
   - Carga los mensajes de esa conversación
   - Actualiza el thread_id activo
   - Resalta como activa

3. Al enviar mensaje:
   - Actualiza ultimoMensaje de la conversación activa
   - Guarda mensajes en la conversación correcta

Persistencia:
- Guarda todo el array de conversaciones en localStorage
- Al cargar la app, recupera conversaciones guardadas
- Si no hay conversaciones guardadas, crea una inicial

Responsive:
- En mobile (< 768px):
  - Sidebar oculto por defecto
  - Botón hamburger en el header para mostrar/ocultar
  - Sidebar aparece como overlay con fondo oscuro
  - Click fuera del sidebar lo cierra
```

---

## ✅ Checkpoint

Verifica:
- ✅ Sidebar visible a la izquierda
- ✅ Botón "+ Nueva Conversación" funciona
- ✅ Lista muestra todas las conversaciones
- ✅ Click en conversación cambia el contexto
- ✅ Mensajes se guardan en conversación correcta
- ✅ LocalStorage persiste datos (recarga y verifica)
- ✅ Responsive funciona en mobile

---

## 🔄 Ajustes Comunes

### Sidebar muy ancho
```
Reduce el ancho del sidebar a 280px
```

### Conversaciones no cambian
```
Al hacer click en una conversación, asegúrate de:
1. Actualizar el thread_id activo
2. Cargar los mensajes de esa conversación
3. Limpiar el área de mensajes primero
4. Aplicar estilo de "activa" a la conversación seleccionada
```

### Preview del último mensaje no se actualiza
```
Cada vez que se envía o recibe un mensaje, 
actualiza el campo ultimoMensaje de la conversación 
activa con el contenido del último mensaje
```

### localStorage no funciona
```
Guarda las conversaciones en localStorage:
- Al crear nueva conversación
- Al enviar/recibir mensaje
- Usa la key "seguros_conversaciones"

Al cargar la app:
- Lee de localStorage
- Si existe, carga las conversaciones
- Si no existe, crea una conversación inicial
```

### Sidebar no se cierra en mobile
```
En mobile, cuando el usuario hace click en:
1. Una conversación → mostrar chat y cerrar sidebar
2. Fuera del sidebar → cerrar sidebar
3. Botón X o hamburger → toggle sidebar
```

---

## 💡 Mejoras Opcionales

Si quieres mejorar aún más:

```
Agrega en cada item de conversación:
- Botón eliminar (🗑️) que:
  - Muestra confirmación "¿Eliminar esta conversación?"
  - Si confirma, elimina del array y localStorage
  - Si es la activa, cambia a otra conversación
```

---

## 📸 Resultado Esperado - Desktop

```
┌─────────────┬───────────────────────────────┐
│+ Nueva Conv │ 🏥 SegurosVida+              │
├─────────────┤                               │
│📍 Conv. 1   │  🤖 ¡Bienvenido!             │
│  "¿Qué..."  │                               │
│  21/10 14:30│            ¿Qué seguros? 🟦   │
│             │                               │
│💬 Conv. 2   │  🤖 Ofrecemos 5 tipos...     │
│  "¿Cuán..." │                               │
│  21/10 15:00│                               │
│             │ [Pregunta sobre seguros...] →│
├─────────────┴───────────────────────────────┤
```

---

## 📸 Resultado Esperado - Mobile

```
≡ Menú Hamburger    🏥 SegurosVida+

[Al hacer click en ≡]

┌─────────────┐
│+ Nueva Conv │← Sidebar overlay
│             │
│📍 Conv. 1   │
│  "¿Qué..."  │
│             │
│💬 Conv. 2   │
│  "¿Cuán..." │
│             │
│     [X]     │← Botón cerrar
└─────────────┘
```

---

## 🧪 Testing

1. Crea 3 conversaciones nuevas
2. Envía mensajes en cada una
3. Cambia entre conversaciones → verifica que mensajes persisten
4. Recarga la página → verifica que todo se mantiene
5. Prueba en mobile (DevTools → responsive mode)

---

**[← Prompt 3](./03_api_integration.md)** | **[Prompt 5 →](./05_final_polish.md)**
