"""
PASO 1: Chat Básico Sin API
============================

En este primer paso aprenderás:
- Cómo crear la interfaz de chat usando st.chat_message()
- Cómo capturar mensajes del usuario con st.chat_input()
- Cómo mantener el historial con Session State
- Cómo simular respuestas del agente

Este paso NO se conecta al API todavía, solo simula las respuestas.
"""

import streamlit as st
import time

# ========================================
# CONFIGURACIÓN DE LA PÁGINA
# ========================================

st.set_page_config(
    page_title="Chat SegurosVida+ - Paso 1",
    page_icon="💬",
    layout="wide"
)

# ========================================
# INICIALIZAR SESSION STATE
# ========================================

# Lista para almacenar los mensajes del chat
# Cada mensaje es un diccionario con 'role' y 'content'
if "messages" not in st.session_state:
    st.session_state.messages = []

# ========================================
# HEADER
# ========================================

st.title("💬 Chat con SegurosVida+")
st.caption("🚀 Paso 1: Chat básico sin API - Respuestas simuladas")

# ========================================
# SIDEBAR CON INFORMACIÓN
# ========================================

with st.sidebar:
    st.header("ℹ️ Información")
    
    st.write("""
    **Paso 1 de 4**
    
    En este paso estamos:
    - ✅ Mostrando mensajes en el chat
    - ✅ Capturando input del usuario
    - ✅ Manteniendo historial con Session State
    - ❌ **NO** conectados al API (respuestas simuladas)
    
    **Siguiente paso**: Conectar con el API real
    """)
    
    st.divider()
    
    # Botón para limpiar el chat
    if st.button("🗑️ Limpiar conversación"):
        st.session_state.messages = []
        st.rerun()
    
    st.divider()
    
    # Mostrar cantidad de mensajes
    st.metric("Mensajes en el chat", len(st.session_state.messages))

# ========================================
# MOSTRAR HISTORIAL DE MENSAJES
# ========================================

# Recorremos todos los mensajes guardados en session_state
for message in st.session_state.messages:
    # Cada mensaje tiene un 'role' (user o assistant) y 'content' (texto)
    with st.chat_message(message["role"]):
        st.write(message["content"])

# ========================================
# INPUT DEL USUARIO
# ========================================

# st.chat_input() muestra un campo de entrada en la parte inferior
# Retorna el texto cuando el usuario presiona Enter
if prompt := st.chat_input("Escribe tu mensaje aquí..."):
    
    # Agregar el mensaje del usuario al historial
    st.session_state.messages.append({
        "role": "user",
        "content": prompt
    })
    
    # Mostrar el mensaje del usuario inmediatamente
    with st.chat_message("user"):
        st.write(prompt)
    
    # Simular que el agente está "pensando"
    with st.chat_message("assistant"):
        with st.spinner("Pensando..."):
            time.sleep(1)  # Simular delay de procesamiento
            
            # RESPUESTA SIMULADA
            # En el siguiente paso, esto será reemplazado por una llamada al API
            respuesta = simular_respuesta_agente(prompt)
            
            st.write(respuesta)
    
    # Agregar la respuesta del agente al historial
    st.session_state.messages.append({
        "role": "assistant",
        "content": respuesta
    })

# ========================================
# FUNCIÓN PARA SIMULAR RESPUESTAS
# ========================================

def simular_respuesta_agente(mensaje: str) -> str:
    """
    Simula respuestas del agente basadas en palabras clave.
    En el paso 2 esto será reemplazado por llamadas reales al API.
    """
    mensaje_lower = mensaje.lower()
    
    # Saludos
    if any(palabra in mensaje_lower for palabra in ["hola", "buenos días", "buenas tardes", "hey"]):
        return "¡Hola! Bienvenido a SegurosVida+. ¿En qué puedo ayudarte hoy?"
    
    # Tipos de seguros
    elif "tipos" in mensaje_lower or "qué seguros" in mensaje_lower:
        return """En SegurosVida+ ofrecemos 5 tipos de seguros:
        
1. **Seguro de Vida** - Desde $25/mes
2. **Seguro de Auto** - Desde $45/mes
3. **Seguro de Hogar** - Desde $35/mes
4. **Seguro de Salud** - Desde $80/mes
5. **Seguro de Viaje** - Desde $15/viaje

¿Sobre cuál te gustaría saber más?"""
    
    # Seguro de auto
    elif "auto" in mensaje_lower or "carro" in mensaje_lower or "vehículo" in mensaje_lower:
        return """**Seguro de Auto**

Desde $45/mes, incluye:
- ✅ Todo riesgo con franquicia desde $500
- ✅ Asistencia en carretera 24/7
- ✅ Auto de reemplazo
- ✅ Cobertura a terceros

¿Te gustaría una cotización?"""
    
    # Seguro de vida
    elif "vida" in mensaje_lower:
        return """**Seguro de Vida**

Desde $25/mes, incluye:
- ✅ Cobertura desde $50,000 hasta $1,000,000
- ✅ Beneficiarios ilimitados
- ✅ Cobertura por muerte natural o accidental
- ✅ Opciones de pago flexibles

¿Necesitas más información?"""
    
    # Precios
    elif "precio" in mensaje_lower or "cuánto" in mensaje_lower or "cuesta" in mensaje_lower:
        return """Nuestros precios varían según el tipo de seguro:

- Seguro de Vida: desde $25/mes
- Seguro de Auto: desde $45/mes
- Seguro de Hogar: desde $35/mes
- Seguro de Salud: desde $80/mes
- Seguro de Viaje: desde $15/viaje

¿Sobre cuál quieres saber más detalles?"""
    
    # Contacto
    elif "contacto" in mensaje_lower or "teléfono" in mensaje_lower or "llamar" in mensaje_lower:
        return """Puedes contactarnos por:

📞 Teléfono: 1-800-SEGVIDA (1-800-734-8432)
📧 Email: contacto@segurosvida.com
📱 WhatsApp: +57 300 123 4567

Nuestro horario es de Lunes a Viernes, 8AM - 6PM"""
    
    # Respuesta por defecto
    else:
        return """Entiendo tu consulta. 

Soy un asistente especializado en seguros de SegurosVida+. Puedo ayudarte con información sobre:
- Tipos de seguros disponibles
- Precios y coberturas
- Información de contacto

¿Sobre qué te gustaría saber más?

**Nota**: Este es el Paso 1, estoy usando respuestas simuladas. En el siguiente paso me conectaré al agente real."""

# ========================================
# INFORMACIÓN ADICIONAL AL FINAL
# ========================================

with st.expander("💡 Explicación del código - Paso 1"):
    st.markdown("""
    ### ¿Cómo funciona este chat?
    
    **1. Session State para el historial**
    ```python
    if "messages" not in st.session_state:
        st.session_state.messages = []
    ```
    Guardamos todos los mensajes en una lista. Cada mensaje es un dict con `role` y `content`.
    
    **2. Mostrar mensajes existentes**
    ```python
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.write(message["content"])
    ```
    
    **3. Capturar nuevo mensaje**
    ```python
    if prompt := st.chat_input("Escribe..."):
        # Agregar al historial
        st.session_state.messages.append({
            "role": "user",
            "content": prompt
        })
    ```
    
    **4. Simular respuesta del agente**
    ```python
    respuesta = simular_respuesta_agente(prompt)
    st.session_state.messages.append({
        "role": "assistant",
        "content": respuesta
    })
    ```
    
    ### ⏭️ Siguiente paso
    En el Paso 2 reemplazaremos `simular_respuesta_agente()` con una llamada real al API del agente.
    """)
