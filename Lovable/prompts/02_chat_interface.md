# Prompt 2: Mejorar Interfaz del Chat

## 🎯 Objetivo
Hacer que los mensajes se vean profesionales y diferenciados.

---

## 📝 Prompt para Lovable

```
Mejora la interfaz de los mensajes del chat:

Mensajes del usuario (derecha):
- Alineados a la derecha
- Fondo azul (#3b82f6)
- Texto blanco
- Bordes redondeados (rounded-2xl)
- Máximo ancho 70% de la pantalla
- Padding de 3
- Sombra sutil
- Muestra la hora abajo del mensaje (text-xs, color azul más claro)

Mensajes del agente/sistema (izquierda):
- Alineados a la izquierda
- Fondo gris (#e5e7eb)
- Texto negro (#1f2937)
- Mismo estilo de bordes y padding que usuario
- Máximo ancho 70%
- Agrega un pequeño avatar o icono 🤖 antes del mensaje
- Muestra la hora abajo (text-xs, gris)

Mejoras generales:
- Espacio entre mensajes (gap-3)
- Scroll automático al último mensaje cuando llega uno nuevo
- Animación fade-in suave cuando aparece un mensaje nuevo
- Placeholder del input más descriptivo: "Pregunta sobre seguros de vida, auto, hogar..."
- Botón enviar con ícono de avión de papel (→) o similar

Empty state:
- Si no hay mensajes (además de bienvenida), muestra:
  "Inicia una conversación preguntando sobre nuestros productos"
```

---

## ✅ Checkpoint

Verifica:
- ✅ Mensajes de usuario en azul a la derecha
- ✅ Mensajes del agente en gris a la izquierda
- ✅ Se ven las horas en cada mensaje
- ✅ Avatar del agente visible
- ✅ Animación al aparecer mensajes
- ✅ Scroll automático funciona

---

## 🔄 Ajustes Comunes

### Mensajes muy anchos en desktop
```
Limita el ancho máximo de los mensajes a 600px además del 70%
```

### Hora muy grande o mal posicionada
```
La hora debe estar abajo del texto del mensaje, 
text-xs, alineada a la derecha para mensajes del usuario
y a la izquierda para mensajes del agente
```

### Avatar muy grande
```
El avatar debe ser pequeño (16x16px o 20x20px), 
solo un emoji o ícono simple
```

### No hace scroll automático
```
Cuando se agrega un nuevo mensaje, 
usa scrollIntoView o scroll automático al final del contenedor
```

---

## 📸 Resultado Esperado

```
┌──────────────────────────────────────────┐
│ 🏥 SegurosVida+                          │
├──────────────────────────────────────────┤
│                                          │
│ 🤖 ¡Bienvenido! ¿En qué puedo           │
│    ayudarte hoy?                  14:30  │
│                                          │
│           Hola, quisiera información 🟦  │
│                                   14:31  │
│                                          │
│ 🤖 ¡Claro! Ofrecemos seguros de:        │
│    • Vida                         14:31  │
│    • Auto                                │
│    • Hogar...                            │
│                                          │
├──────────────────────────────────────────┤
│ [Pregunta sobre seguros de vida...] [→] │
└──────────────────────────────────────────┘
```

---

**[← Prompt 1](./01_initial_project.md)** | **[Prompt 3 →](./03_api_integration.md)**
