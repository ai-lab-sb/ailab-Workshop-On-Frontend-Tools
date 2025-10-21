# Prompt 3: Integración con API

## 🎯 Objetivo
Conectar con el backend real del agente de seguros.

---

## 📝 Prompt para Lovable

```
Conecta la aplicación con la API real del agente de seguros:

Configuración de la API:
- URL base: http://localhost:8000
- Endpoint: POST /chat
- Body JSON: {
    "message": "texto del mensaje del usuario",
    "thread_id": "identificador único de la conversación"
  }
- Respuesta JSON: {
    "response": "respuesta del agente",
    "thread_id": "mismo id"
  }

Funcionalidad:
1. Al iniciar la app, genera un thread_id único usando crypto.randomUUID() o similar

2. Cuando el usuario envía un mensaje:
   - Muestra inmediatamente el mensaje del usuario en el chat
   - Muestra indicador "Escribiendo..." con puntos animados del lado del agente
   - Deshabilita el input y botón de enviar
   - Envía POST request a la API con el mensaje y thread_id

3. Cuando llega la respuesta:
   - Elimina el indicador "Escribiendo..."
   - Muestra el mensaje del agente con la respuesta
   - Habilita nuevamente el input y botón

4. Manejo de errores:
   - Si falla la conexión: mostrar mensaje en rojo 
     "❌ No se pudo conectar con el agente. ¿Está corriendo el servidor?"
   - Si timeout (más de 30 segundos): 
     "⏱️ El agente tardó demasiado en responder. Intenta de nuevo."
   - Si otro error:
     "❌ Error inesperado: [descripción del error]"
   - Agregar botón "Reintentar" en mensajes de error

Estados visuales:
- Input deshabilitado: cursor not-allowed, fondo gris claro
- Botón enviar con spinner durante loading
- "Escribiendo..." con tres puntos que se animan (. .. ...)
```

---

## ✅ Checkpoint

Verifica:
- ✅ Se genera thread_id al iniciar
- ✅ Mensajes se envían al API
- ✅ Respuestas del agente aparecen correctamente
- ✅ "Escribiendo..." se muestra mientras espera
- ✅ Input se deshabilita durante loading
- ✅ Errores se manejan apropiadamente

---

## 🧪 Testing

### Test 1: Funcionalidad Normal

1. Asegúrate de que el backend esté corriendo:
   ```bash
   cd insurance_agent_api/app
   python main.py
   ```

2. En Lovable, envía: "¿Qué tipos de seguros ofrecen?"

3. Deberías recibir respuesta real del agente sobre SegurosVida+

### Test 2: Manejo de Errores

1. **Apaga el backend** (Ctrl+C en la terminal)

2. Intenta enviar un mensaje

3. Deberías ver mensaje de error: "No se pudo conectar con el agente..."

4. Prende el backend de nuevo

5. Click en "Reintentar" → debería funcionar

---

## 🔄 Ajustes Comunes

### Error de CORS
Si ves error de CORS en la consola:

```
El backend debe tener CORS habilitado. 
Verifica que el archivo main.py del backend incluya:

from fastapi.middleware.cors import CORSMiddleware

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)
```

*Nota: El backend ya debería tenerlo configurado.*

### No aparece "Escribiendo..."
```
Agrega un mensaje temporal del agente con el texto 
"Escribiendo..." que se muestra inmediatamente al enviar 
y se remueve cuando llega la respuesta real
```

### Thread ID se pierde
```
Guarda el thread_id en el estado de React y úsalo 
consistentemente en todas las llamadas a la API
```

### Timeout muy corto/largo
```
Ajusta el timeout del fetch a 30 segundos:
fetch(url, { 
  method: 'POST',
  headers: { 'Content-Type': 'application/json' },
  body: JSON.stringify(data),
  signal: AbortSignal.timeout(30000) // 30 segundos
})
```

---

## 💡 Tips

### Ver Requests en Consola

Abre DevTools (F12) → Network tab → filtra por "chat"

Podrás ver:
- Request payload
- Response data
- Status codes
- Timing

### Verificar Backend

En el navegador, ve a: `http://localhost:8000/health`

Debería responder:
```json
{
  "status": "healthy",
  "service": "SegurosVida+ Insurance Agent API",
  "agent_ready": true
}
```

---

## 📸 Resultado Esperado

```
Usuario envía: "¿Qué seguros ofrecen?"

Chat muestra:
┌────────────────────────────────────┐
│           ¿Qué seguros ofrecen? 🟦│
│                            15:45   │
│                                    │
│ 🤖 Escribiendo...                  │ ← Loading
│                                    │
└────────────────────────────────────┘

Después de ~2 segundos:
┌────────────────────────────────────┐
│           ¿Qué seguros ofrecen? 🟦│
│                            15:45   │
│                                    │
│ 🤖 ¡Hola! En SegurosVida+         │
│    ofrecemos 5 tipos de seguros:  │
│    • Seguros de Vida              │
│    • Seguros de Auto              │
│    • Seguros de Hogar      15:45  │
│    • Seguros de Salud             │
│    • Seguros de Viaje             │
│                                    │
└────────────────────────────────────┘
```

---

**[← Prompt 2](./02_chat_interface.md)** | **[Prompt 4 →](./04_multiple_threads.md)**
