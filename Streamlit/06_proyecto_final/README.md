# 06 - Proyecto Final: Chat de Seguros con IA

## 🎯 Objetivo

Crear una aplicación de chat conversacional completa que se comunique con el agente de SegurosVida+ usando todo lo aprendido en el curso.

## 📋 ¿Qué vas a construir?

Una aplicación de chat que:
- ✅ Permite conversar con un agente de IA especializado en seguros
- ✅ Mantiene el historial de la conversación
- ✅ Gestiona múltiples conversaciones (threads)
- ✅ Tiene una interfaz pulida y profesional
- ✅ Consume el API del agente de seguros

## 🏗️ Construcción Paso a Paso

Este proyecto está dividido en 4 pasos progresivos. Cada paso agrega funcionalidad sobre el anterior:

### Paso 1: Chat Básico Sin API
**Archivo**: `paso_1_chat_basico.py`

Aprenderás:
- Crear la interfaz del chat
- Usar `st.chat_message()` y `st.chat_input()`
- Mantener historial con Session State
- Simular respuestas del agente

**Ejecutar:**
```bash
streamlit run paso_1_chat_basico.py
```

### Paso 2: Integración con API
**Archivo**: `paso_2_integracion_api.py`

Aprenderás:
- Conectar con el API real del agente
- Hacer POST requests a `/chat`
- Procesar respuestas del agente
- Manejo de errores de conexión

**Ejecutar:**
```bash
streamlit run paso_2_integracion_api.py
```

⚠️ **Requisito**: El agente debe estar corriendo en `http://localhost:8000`

### Paso 3: Gestión de Historial
**Archivo**: `paso_3_historial.py`

Aprenderás:
- Usar thread_id para múltiples conversaciones
- Obtener historial del servidor (GET `/history/{thread_id}`)
- Mostrar conversaciones previas
- Cargar conversación al iniciar

**Ejecutar:**
```bash
streamlit run paso_3_historial.py
```

### Paso 4: Aplicación Completa
**Archivo**: `paso_4_completo.py`

La versión final con:
- Sidebar con lista de conversaciones
- Crear nueva conversación
- Seleccionar conversación existente
- Interfaz pulida y profesional
- Todos los features integrados

**Ejecutar:**
```bash
streamlit run paso_4_completo.py
```

## 📚 Conceptos Aplicados

| Concepto | Lección | Uso en el Proyecto |
|----------|---------|-------------------|
| `st.chat_message()` | 01 | Mostrar burbujas de chat |
| `st.chat_input()` | 02 | Campo para escribir mensajes |
| `st.session_state` | 04 | Mantener historial y thread_id |
| `requests.post()` | 05 | Enviar mensajes al agente |
| `requests.get()` | 05 | Obtener historial |
| `st.sidebar` | 03 | Lista de conversaciones |

## 🚀 Preparación

### 1. Asegúrate de tener el agente corriendo

```bash
cd ../insurance_agent_api/app
python main.py
```

Verifica que esté corriendo en: `http://localhost:8000`

### 2. Instala las dependencias

```bash
pip install -r requirements.txt
```

### 3. Prueba la conexión

Abre en tu navegador: `http://localhost:8000/health`

Deberías ver:
```json
{
  "status": "healthy",
  "service": "SegurosVida+ Insurance Agent API",
  "agent_ready": true
}
```

## 📝 Endpoints del Agente

### POST /chat
Envía un mensaje al agente.

**Request:**
```json
{
  "message": "¿Qué tipos de seguros ofrecen?",
  "thread_id": "usuario_123"
}
```

**Response:**
```json
{
  "response": "¡Hola! En SegurosVida+ ofrecemos 5 tipos...",
  "thread_id": "usuario_123"
}
```

### GET /history/{thread_id}
Obtiene el historial de una conversación.

**Response:**
```json
{
  "history": [
    {
      "type": "human",
      "content": "Hola"
    },
    {
      "type": "ai",
      "content": "¡Hola! ¿En qué puedo ayudarte?"
    }
  ]
}
```

## 💡 Tips para el Desarrollo

### 1. Debugging
```python
# Ver el session_state completo
with st.expander("Debug"):
    st.write(st.session_state)
```

### 2. Manejo de errores
```python
try:
    response = requests.post(url, json=data, timeout=30)
    response.raise_for_status()
except requests.exceptions.RequestException as e:
    st.error(f"Error al conectar con el agente: {e}")
```

### 3. Loading states
```python
with st.spinner("El agente está pensando..."):
    response = requests.post(url, json=data)
```

## 🎨 Personalización

Una vez que completes los 4 pasos, puedes personalizar:

- 🎨 Colores y estilos
- 📱 Layout responsivo
- ✨ Animaciones y efectos
- 📊 Estadísticas de uso
- 💾 Exportar conversaciones
- 🔊 Text-to-speech
- 🖼️ Avatares personalizados

## 🎯 Objetivos de Aprendizaje

Al completar este proyecto habrás aprendido a:

1. ✅ Crear interfaces de chat con Streamlit
2. ✅ Gestionar estado complejo con Session State
3. ✅ Consumir APIs REST desde Streamlit
4. ✅ Manejar errores y casos edge
5. ✅ Crear una aplicación web completa y funcional

## 🚀 ¡Empecemos!

Comienza con **paso_1_chat_basico.py** y avanza paso a paso.

Cada archivo está completamente documentado y explicado.

**¡Buena suerte! 🎉**

---

## 📖 Recursos Adicionales

- [Documentación de st.chat_message](https://docs.streamlit.io/library/api-reference/chat/st.chat_message)
- [Documentación de st.chat_input](https://docs.streamlit.io/library/api-reference/chat/st.chat_input)
- [Build a basic LLM chat app](https://docs.streamlit.io/develop/tutorials/llms/build-conversational-apps)

## 🤝 Soporte

Si tienes dudas sobre el proyecto final, revisa:
1. El código comentado en cada paso
2. Los ejemplos de lecciones anteriores
3. La documentación del agente en `insurance_agent_api/README.md`
