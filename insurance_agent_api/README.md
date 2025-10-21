# 🏥 SegurosVida+ - Agente de Seguros con IA

API de un agente conversacional con memoria especializado en seguros, construido con **LangGraph**, **FastAPI** y **Gemini 2.5 Flash**.

## 📋 Descripción

Este agente representa a **SegurosVida+**, una empresa ficticia de seguros creada para el workshop de herramientas frontend con IA. El agente puede:

- ✅ Responder preguntas sobre productos de seguros (vida, auto, hogar, salud, viaje)
- ✅ Mantener memoria de conversaciones por thread_id
- ✅ Proporcionar información detallada sobre coberturas y precios
- ✅ Dar recomendaciones personalizadas
- ✅ Recordar contexto previo en la conversación

## 🏢 Sobre SegurosVida+

**SegurosVida+** es una empresa ficticia de seguros con las siguientes características:

- **Lema**: "Tu tranquilidad, nuestra prioridad"
- **Experiencia**: 25 años en el mercado
- **Productos**: Seguros de vida, auto, hogar, salud y viaje
- **Cobertura**: Nacional e internacional
- **Calificación**: 4.8/5 estrellas

## 🚀 Instalación y Configuración

### 1. Requisitos Previos

- Python 3.10 o superior
- Una API Key de Google Gemini ([Obtener aquí](https://makersuite.google.com/app/apikey))

### 2. Instalación

```bash
# Navegar a la carpeta del agente
cd insurance_agent_api

# Instalar dependencias
pip install -r requirements.txt
```

### 3. Configuración de API Key

Crear un archivo `.env` en la raíz del proyecto:

```bash
GOOGLE_API_KEY=tu_api_key_de_gemini_aqui
```

**⚠️ IMPORTANTE**: Nunca subas tu archivo `.env` a repositorios públicos.

## ▶️ Ejecutar el Agente

```bash
# Desde la carpeta insurance_agent_api/app
cd app
python main.py
```

O usando uvicorn directamente:

```bash
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

El servidor estará disponible en: `http://localhost:8000`

## 📡 Endpoints de la API

### 1. **POST /chat** - Conversar con el agente

Envía un mensaje al agente y recibe una respuesta.

**Request:**
```json
{
  "message": "Hola, ¿qué tipos de seguros ofrecen?",
  "thread_id": "usuario_123"
}
```

**Response:**
```json
{
  "response": "¡Hola! En SegurosVida+ ofrecemos 5 tipos de seguros principales...",
  "thread_id": "usuario_123"
}
```

**Ejemplo con curl:**
```bash
curl -X POST "http://localhost:8000/chat" \
  -H "Content-Type: application/json" \
  -d '{"message": "Hola, ¿qué seguros ofrecen?", "thread_id": "test_001"}'
```

**Ejemplo con JavaScript (fetch):**
```javascript
const response = await fetch('http://localhost:8000/chat', {
  method: 'POST',
  headers: { 'Content-Type': 'application/json' },
  body: JSON.stringify({
    message: '¿Cuánto cuesta el seguro de auto?',
    thread_id: 'user_123'
  })
});
const data = await response.json();
console.log(data.response);
```

### 2. **GET /history/{thread_id}** - Obtener historial

Recupera todas las conversaciones de un thread_id específico.

**Response:**
```json
{
  "history": [
    {
      "type": "human",
      "content": "Hola, ¿qué seguros ofrecen?"
    },
    {
      "type": "ai",
      "content": "¡Hola! En SegurosVida+ ofrecemos 5 tipos de seguros..."
    }
  ]
}
```

**Ejemplo con curl:**
```bash
curl "http://localhost:8000/history/test_001"
```

### 3. **GET /health** - Verificar estado

Verifica que el servicio esté funcionando correctamente.

**Response:**
```json
{
  "status": "healthy",
  "service": "SegurosVida+ Insurance Agent API",
  "agent_ready": true
}
```

### 4. **GET /** - Información de la API

Devuelve información general y lista de endpoints disponibles.

## 🧠 Memoria del Agente

El agente utiliza **thread_id** para mantener conversaciones separadas:

- Cada `thread_id` representa una conversación independiente
- El agente recuerda todo el contexto de la conversación
- Puedes tener múltiples conversaciones simultáneas con diferentes thread_ids
- Si no especificas thread_id, se usa "default"

**Ejemplo de uso de memoria:**

```javascript
// Primera pregunta
await chat("¿Cuánto cuesta el seguro de vida?", "user_maria");
// Respuesta: "El seguro de vida desde $25/mes..."

// Segunda pregunta (recuerda el contexto)
await chat("¿Y el de auto?", "user_maria");
// Respuesta: "El seguro de auto desde $45/mes..."

// El agente recuerda que ya hablamos de seguros
```

## 📚 Documentación Interactiva

Una vez que el servidor esté corriendo, puedes acceder a:

- **Swagger UI**: http://localhost:8000/docs
- **ReDoc**: http://localhost:8000/redoc

Estas interfaces te permiten probar los endpoints directamente desde el navegador.

## 🎯 Uso en el Workshop

Este agente está diseñado para ser consumido por diferentes frontends:

1. **Cursor**: Frontend con código generado por IA
2. **Dash**: Dashboard interactivo en Python
3. **Lovable**: Interfaz moderna con IA
4. **Streamlit**: Aplicación web rápida en Python

**Los participantes del workshop NO modificarán este agente**, solo consumirán sus endpoints para crear diferentes interfaces de usuario.

## 🔧 Tecnologías Utilizadas

- **LangGraph**: Framework para agentes con estado y memoria
- **FastAPI**: Framework web moderno y rápido
- **Gemini 2.5 Flash**: Modelo de IA de Google
- **LangChain**: Herramientas para aplicaciones con LLMs
- **Pydantic**: Validación de datos

## 💡 Ejemplos de Preguntas

Prueba el agente con preguntas como:

- "¿Qué tipos de seguros ofrecen?"
- "¿Cuánto cuesta el seguro de salud?"
- "¿El seguro de auto incluye asistencia en carretera?"
- "Quiero un seguro para mi casa, ¿qué me recomiendan?"
- "¿Tienen cobertura internacional?"
- "¿Cómo puedo hacer una reclamación?"

## ⚠️ Notas Importantes

- Este es un **proyecto educativo** con una empresa ficticia
- La información de productos y precios es **completamente ficticia**
- El agente mantiene la memoria solo mientras el servidor está corriendo (usa MemorySaver en memoria)
- Si detienes el servidor, las conversaciones se pierden
- Para producción, considera usar un checkpointer persistente (PostgreSQL, Redis, etc.)

