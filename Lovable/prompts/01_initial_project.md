# Prompt 1: Proyecto Inicial

## 🎯 Objetivo
Crear la estructura básica de la aplicación de chat.

---

## 📝 Prompt para Lovable

```
Crea una aplicación de chat para una empresa de seguros llamada "SegurosVida+".

Layout:
- Header fijo en la parte superior con:
  - Título "SegurosVida+" a la izquierda
  - Icono o emoji de seguros (🏥 o 🛡️)
  - Fondo azul oscuro (#1e40af)
  - Texto blanco
  - Altura de 64px

- Área central para mostrar mensajes:
  - Fondo gris muy claro (#f9fafb)
  - Scrollable verticalmente
  - Padding de 4

- Input fijo en la parte inferior:
  - Input de texto con placeholder "Escribe tu mensaje..."
  - Botón "Enviar" a la derecha
  - Fondo blanco
  - Borde superior gris claro
  - Padding de 4

Funcionalidad básica:
- El input debe ser controlado con estado de React
- Al presionar Enter o click en "Enviar":
  - Agregar mensaje a un array de mensajes
  - Mostrar el mensaje en el área central
  - Limpiar el input
  - Por ahora, simula una respuesta automática después de 1 segundo

Estado inicial:
- Muestra un mensaje de bienvenida del sistema: 
  "¡Bienvenido a SegurosVida+! ¿En qué puedo ayudarte hoy?"
```

---

## ✅ Checkpoint

Verifica que funcione:
- ✅ Layout se ve correcto (header, área mensajes, input)
- ✅ Puedes escribir en el input
- ✅ Al enviar, el mensaje aparece
- ✅ Input se limpia después de enviar
- ✅ Respuesta simulada aparece después de 1 segundo

---

## 🔄 Si Algo No Funciona

### Input no se limpia
```
Limpia el input después de enviar el mensaje
```

### No aparece respuesta automática
```
Después de que el usuario envía un mensaje, 
espera 1 segundo y muestra una respuesta simulada 
del agente que diga "Gracias por tu mensaje. 
¿Podrías darme más detalles?"
```

### Layout se ve mal en mobile
```
Asegura que el layout sea responsive:
- En mobile, reduce padding
- Header debe mantenerse fijo
- Input debe mantenerse fijo en la parte inferior
```

---

## 📸 Resultado Esperado

```
┌──────────────────────────────────────┐
│ 🏥 SegurosVida+                      │ ← Header azul
├──────────────────────────────────────┤
│                                      │
│  ¡Bienvenido a SegurosVida+!       │
│  ¿En qué puedo ayudarte hoy?       │
│                                      │
│  Usuario: Hola                14:30 │
│                                      │
│  Sistema: Gracias por...      14:30 │
│                                      │
├──────────────────────────────────────┤
│ [Escribe tu mensaje...]     [Enviar]│ ← Input fijo
└──────────────────────────────────────┘
```

---

**[Siguiente: Prompt 2 - Chat Interface →](./02_chat_interface.md)**
