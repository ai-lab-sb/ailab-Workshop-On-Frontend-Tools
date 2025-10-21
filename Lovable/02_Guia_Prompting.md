# 2️⃣ Prompting Guide

## 🎯 Anatomía de un Buen Prompt

```
[QUÉ QUIERES] + [CÓMO DEBE VERSE] + [CÓMO DEBE FUNCIONAR]
```

### Ejemplo

```
Crea una barra de navegación [QUÉ]

Con logo a la izquierda, links en el centro 
(Inicio, Servicios, Contacto), y botón "Login" a la derecha [ESTRUCTURA]

Fondo azul oscuro (#1e3a8a), texto blanco, sombra inferior [ESTILOS]

Al hacer scroll, se vuelve transparente y reduce altura [COMPORTAMIENTO]
```

---

## ✅ Principios Clave

### 1. Sé Específico, No Vago

#### ❌ Vago
```
Haz una app de chat
```

#### ✅ Específico
```
Crea interfaz de chat con:
- Sidebar izquierdo (300px) lista de conversaciones
- Área central para mensajes
- Input inferior con botón enviar
- Sidebar gris (#f3f4f6), área chat blanco
```

### 2. Divide en Pasos Pequeños

#### ❌ Todo de una vez
```
Crea app completa con productos, carrito, checkout, 
pagos, auth, dashboard admin y analytics
```

#### ✅ Paso a paso
```
Paso 1: Crea grid de 8 productos con imagen, nombre y precio
```
→ Espera resultado →
```
Paso 2: Agrega header con logo y carrito
```

### 3. Especifica Números

❌ "Haz el sidebar más ancho"  
✅ "Cambia ancho del sidebar de 250px a 350px"

### 4. Describe Estados

```
El botón debe:
- Normal: fondo azul (#3b82f6)
- Hover: azul oscuro (#2563eb)
- Disabled: gris (#9ca3af), no clickeable
- Al click: mostrar spinner mientras carga
```

---

## 🎨 Prompts por Categoría

### Layout y Estructura

```
Cambia layout a 3 columnas:
- Sidebar izquierdo: 20% ancho
- Contenido central: 60% ancho  
- Panel derecho: 20% ancho
```

### Colores

```
Actualiza paleta:
- Primario: #10b981 (verde)
- Secundario: #3b82f6 (azul)
- Fondo: #f9fafb
- Texto: #1f2937
```

### Responsive

```
En mobile (max-width: 768px):
- Oculta sidebar
- Cambia a 1 columna
- Menú como hamburger
```

### Funcionalidad

```
Al hacer click en "Guardar":
1. Valida que campos estén llenos
2. Si falta algo: mensaje error rojo
3. Si ok: guarda en localStorage
4. Muestra éxito verde
5. Cierra modal después de 2 segundos
```

### API Integration

```
Crea función POST a:
http://localhost:8000/chat

Body JSON:
{
  "message": "texto del usuario",
  "thread_id": "id conversación"
}

Maneja: loading, success, error
```

---

## 🚫 Anti-Patrones (Evitar)

### ❌ 1. Ambiguos

```
Malo: "Mejora el diseño"
```
¿Qué significa "mejor"?

```
Bueno: "Aumenta contraste y espaciado (padding 6 en vez de 4)"
```

### ❌ 2. Demasiado en Uno

```
Malo: "Agrega navbar, sidebar, footer, 5 páginas, 
routing, auth, database y deploy"
```

```
Bueno: "Agrega navbar con logo y 3 links"
```

### ❌ 3. Sin Contexto

```
Malo: "Agrega el botón"
```
¿Qué botón? ¿Dónde?

```
Bueno: "Agrega botón azul 'Enviar' abajo del input, 
alineado a la derecha"
```

---

## 💡 Prompts Progresivos (Build Step-by-Step)

### Fase 1: Estructura

```
Crea estructura de app de chat:
- Header con título "SegurosVida+ Chat"
- Área mensajes al centro
- Input para escribir abajo
- Header azul (#1e40af), fondo gris claro
```

### Fase 2: Funcionalidad

```
Agrega funcionalidad:
- Al enviar, agrega mensaje a lista
- Limpia input
- Muestra hora en cada mensaje
- Usuario derecha (azul), respuestas izquierda (gris)
```

### Fase 3: Estado

```
Agrega estado:
- useState para array mensajes
- Guarda en localStorage
- Al cargar, recupera mensajes
- Botón "Limpiar historial" en header
```

### Fase 4: API

```
Conecta con API:
- POST a http://localhost:8000/chat
- Muestra respuesta como mensaje sistema
- Loading state con spinner
- Maneja errores
```

### Fase 5: Pulido

```
Mejoras finales:
- Animación fade in mensajes
- Auto-scroll al último
- Icono enviar en input
- Placeholder: "Pregunta sobre seguros..."
```

---

## 🎯 Ejercicio Práctico

### Perfecciona este Prompt Vago

**Prompt malo:**
```
Haz una card de producto
```

**Tu tarea:** Reescribe siendo específico sobre contenido, estilos e interacciones.

<details>
<summary>💡 Solución</summary>

```
Crea tarjeta de producto con:

Contenido:
- Imagen 300x300px
- Nombre (font-bold, text-lg)
- Descripción (text-sm, gray-600)
- Precio (text-2xl, verde)
- Botón "Agregar al Carrito"

Estilos:
- Fondo blanco
- Borde gris (border-gray-200)
- Redondeado (rounded-lg)
- Sombra sutil (shadow-sm)

Hover:
- Sombra grande (shadow-lg)
- Transición suave
```
</details>

---

## 📚 Template Reutilizable

```
Crea [COMPONENTE] con:

Contenido:
- [ELEMENTO 1]
- [ELEMENTO 2]

Estilos:
- Colores: [...]
- Tamaños: [...]

Comportamiento:
- Normal: [...]
- Hover: [...]
- Click: [...]
```

---

## ✅ Checklist de Buen Prompt

- [ ] ¿Es específico sobre QUÉ quiero?
- [ ] ¿Describe CÓMO debe verse?
- [ ] ¿Explica CÓMO debe funcionar?
- [ ] ¿Incluye colores/tamaños exactos?
- [ ] ¿Es un paso razonable?
- [ ] ¿Sería claro para un humano?

---

**[← Basics](./1_LOVABLE_BASICS.md)** | **[Build Guide →](./3_BUILD_GUIDE.md)**
