"""
PASO 2: Integración con API Real
=================================

En este paso aprenderás:
- Cómo conectarte al API del agente de seguros
- Cómo hacer POST requests a /chat
- Cómo procesar las respuestas del agente real
- Manejo de errores de conexión

REQUISITO: El agente debe estar corriendo en http://localhost:8000
"""

import streamlit as st
import requests
import time

# ========================================
# CONFIGURACIÓN
# ========================================

st.set_page_config(
    page_title="Chat SegurosVida+ - Paso 2",
    page_icon="💬",
    layout="wide"
)

# URL del API del agente
API_URL = "http://localhost:8000"

# ========================================
# INICIALIZAR SESSION STATE
# ========================================

if "messages" not in st.session_state:
    st.session_state.messages = []

# Thread ID para esta conversación
# Por ahora usamos un ID fijo, en el Paso 3 lo haremos dinámico
if "thread_id" not in st.session_state:
    st.session_state.thread_id = "conversacion_demo"

# ========================================
# FUNCIÓN PARA VERIFICAR CONEXIÓN CON EL API
# ========================================

def verificar_conexion_api() -> bool:
    """Verifica si el API está disponible"""
    try:
        response = requests.get(f"{API_URL}/health", timeout=5)
        return response.status_code == 200
    except requests.exceptions.RequestException:
        return False

# ========================================
# FUNCIÓN PARA ENVIAR MENSAJE AL AGENTE
# ========================================

def enviar_mensaje_al_agente(mensaje: str, thread_id: str) -> dict:
    """
    Envía un mensaje al agente y retorna la respuesta.
    
    Args:
        mensaje: El mensaje del usuario
        thread_id: ID del hilo de conversación
        
    Returns:
        dict con 'success', 'response', y opcionalmente 'error'
    """
    try:
        response = requests.post(
            f"{API_URL}/chat",
            json={
                "message": mensaje,
                "thread_id": thread_id
            },
            timeout=30  # 30 segundos de timeout
        )
        
        if response.status_code == 200:
            data = response.json()
            return {
                "success": True,
                "response": data["response"],
                "thread_id": data["thread_id"]
            }
        else:
            return {
                "success": False,
                "error": f"Error del servidor: {response.status_code}"
            }
            
    except requests.exceptions.Timeout:
        return {
            "success": False,
            "error": "El agente tardó demasiado en responder. Intenta de nuevo."
        }
    except requests.exceptions.ConnectionError:
        return {
            "success": False,
            "error": "No se pudo conectar al agente. Verifica que esté corriendo en http://localhost:8000"
        }
    except requests.exceptions.RequestException as e:
        return {
            "success": False,
            "error": f"Error en la solicitud: {str(e)}"
        }

# ========================================
# HEADER
# ========================================

st.title("💬 Chat con SegurosVida+")
st.caption("🚀 Paso 2: Integración con API real")

# ========================================
# SIDEBAR
# ========================================

with st.sidebar:
    st.header("ℹ️ Información")
    
    # Verificar conexión con el API
    api_conectado = verificar_conexion_api()
    
    if api_conectado:
        st.success("✅ Conectado al agente")
    else:
        st.error("❌ Agente no disponible")
        st.warning("""
        **Asegúrate de iniciar el agente:**
        
        ```bash
        cd insurance_agent_api/app
        python main.py
        ```
        
        Debe estar corriendo en:
        http://localhost:8000
        """)
    
    st.divider()
    
    st.write("""
    **Paso 2 de 4**
    
    En este paso estamos:
    - ✅ Conectados al API real
    - ✅ Obteniendo respuestas del agente
    - ✅ Manejando errores de conexión
    - ❌ **NO** gestionando múltiples conversaciones aún
    
    **Siguiente paso**: Historial y múltiples threads
    """)
    
    st.divider()
    
    # Información de debug
    with st.expander("🔧 Debug Info"):
        st.write(f"API URL: {API_URL}")
        st.write(f"Thread ID: {st.session_state.thread_id}")
        st.write(f"Mensajes: {len(st.session_state.messages)}")
        st.write(f"Conectado: {api_conectado}")
    
    st.divider()
    
    # Botón para limpiar el chat
    if st.button("🗑️ Limpiar conversación"):
        st.session_state.messages = []
        st.rerun()

# ========================================
# MOSTRAR HISTORIAL DE MENSAJES
# ========================================

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])

# ========================================
# INPUT DEL USUARIO
# ========================================

if prompt := st.chat_input("Escribe tu mensaje aquí...", disabled=not api_conectado):
    
    # Agregar mensaje del usuario al historial
    st.session_state.messages.append({
        "role": "user",
        "content": prompt
    })
    
    # Mostrar mensaje del usuario
    with st.chat_message("user"):
        st.write(prompt)
    
    # Obtener respuesta del agente
    with st.chat_message("assistant"):
        with st.spinner("El agente está pensando..."):
            
            # LLAMADA AL API REAL
            resultado = enviar_mensaje_al_agente(
                mensaje=prompt,
                thread_id=st.session_state.thread_id
            )
            
            if resultado["success"]:
                # Mostrar respuesta del agente
                respuesta = resultado["response"]
                st.write(respuesta)
                
                # Agregar al historial
                st.session_state.messages.append({
                    "role": "assistant",
                    "content": respuesta
                })
            else:
                # Mostrar error
                error_msg = resultado["error"]
                st.error(f"Error: {error_msg}")
                
                # También agregar el error al historial para que persista
                st.session_state.messages.append({
                    "role": "assistant",
                    "content": f"❌ {error_msg}"
                })

# ========================================
# MENSAJE INICIAL SI NO HAY CONVERSACIÓN
# ========================================

if len(st.session_state.messages) == 0:
    st.info("""
    👋 **¡Bienvenido a SegurosVida+!**
    
    Soy tu asistente virtual. Puedo ayudarte con:
    - Información sobre nuestros seguros (vida, auto, hogar, salud, viaje)
    - Precios y coberturas
    - Información de contacto
    
    ¿En qué puedo ayudarte hoy?
    """)

# ========================================
# EXPLICACIÓN DEL CÓDIGO
# ========================================

with st.expander("💡 Explicación del código - Paso 2"):
    st.markdown("""
    ### Cambios principales respecto al Paso 1
    
    **1. Verificar conexión con el API**
    ```python
    def verificar_conexion_api() -> bool:
        try:
            response = requests.get(f"{API_URL}/health", timeout=5)
            return response.status_code == 200
        except:
            return False
    ```
    
    **2. Enviar mensaje al agente real**
    ```python
    response = requests.post(
        f"{API_URL}/chat",
        json={
            "message": mensaje,
            "thread_id": thread_id
        },
        timeout=30
    )
    
    data = response.json()
    respuesta = data["response"]
    ```
    
    **3. Manejo de errores**
    - `Timeout`: El agente tardó mucho
    - `ConnectionError`: El agente no está corriendo
    - `RequestException`: Otros errores HTTP
    
    **4. Thread ID**
    Por ahora usamos un thread_id fijo: `"conversacion_demo"`
    
    En el Paso 3 aprenderemos a manejar múltiples threads.
    
    ### ⏭️ Siguiente paso
    En el Paso 3 agregaremos:
    - Múltiples conversaciones (threads)
    - Obtener historial del servidor
    - Gestión de threads en el sidebar
    """)

# ========================================
# TESTING RÁPIDO
# ========================================

with st.expander("🧪 Probar conexión con el API"):
    st.write("**Endpoints disponibles:**")
    
    col1, col2 = st.columns(2)
    
    with col1:
        if st.button("Test GET /health"):
            try:
                response = requests.get(f"{API_URL}/health", timeout=5)
                st.json(response.json())
            except Exception as e:
                st.error(f"Error: {e}")
    
    with col2:
        if st.button("Test GET /"):
            try:
                response = requests.get(f"{API_URL}/", timeout=5)
                st.json(response.json())
            except Exception as e:
                st.error(f"Error: {e}")
