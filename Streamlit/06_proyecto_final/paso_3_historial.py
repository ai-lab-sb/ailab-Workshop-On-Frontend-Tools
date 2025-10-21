"""
PASO 3: Gestión de Historial y Múltiples Conversaciones
========================================================

En este paso aprenderás:
- Cómo obtener el historial desde el servidor
- Cómo usar thread_id para múltiples conversaciones
- Cómo cargar conversaciones previas
- Gestión básica de threads

REQUISITO: El agente debe estar corriendo en http://localhost:8000
"""

import streamlit as st
import requests
from datetime import datetime
import uuid

# ========================================
# CONFIGURACIÓN
# ========================================

st.set_page_config(
    page_title="Chat SegurosVida+ - Paso 3",
    page_icon="💬",
    layout="wide"
)

API_URL = "http://localhost:8000"

# ========================================
# FUNCIONES DE API
# ========================================

def verificar_conexion_api() -> bool:
    """Verifica si el API está disponible"""
    try:
        response = requests.get(f"{API_URL}/health", timeout=5)
        return response.status_code == 200
    except:
        return False

def enviar_mensaje_al_agente(mensaje: str, thread_id: str) -> dict:
    """Envía un mensaje al agente"""
    try:
        response = requests.post(
            f"{API_URL}/chat",
            json={"message": mensaje, "thread_id": thread_id},
            timeout=30
        )
        
        if response.status_code == 200:
            data = response.json()
            return {"success": True, "response": data["response"]}
        else:
            return {"success": False, "error": f"Error: {response.status_code}"}
            
    except requests.exceptions.Timeout:
        return {"success": False, "error": "Timeout - El agente tardó mucho"}
    except requests.exceptions.ConnectionError:
        return {"success": False, "error": "No se pudo conectar al agente"}
    except Exception as e:
        return {"success": False, "error": str(e)}

def obtener_historial(thread_id: str) -> dict:
    """
    Obtiene el historial de una conversación desde el servidor.
    
    Returns:
        dict con 'success', 'history', y opcionalmente 'error'
    """
    try:
        response = requests.get(
            f"{API_URL}/history/{thread_id}",
            timeout=10
        )
        
        if response.status_code == 200:
            data = response.json()
            return {
                "success": True,
                "history": data["history"]
            }
        else:
            return {
                "success": False,
                "error": f"Error: {response.status_code}"
            }
            
    except Exception as e:
        return {
            "success": False,
            "error": str(e)
        }

# ========================================
# INICIALIZAR SESSION STATE
# ========================================

# Lista de threads disponibles (cada thread es una conversación diferente)
if "threads" not in st.session_state:
    st.session_state.threads = []

# Thread ID actual
if "current_thread_id" not in st.session_state:
    # Crear primera conversación automáticamente
    thread_id = f"conv_{uuid.uuid4().hex[:8]}"
    st.session_state.current_thread_id = thread_id
    st.session_state.threads.append({
        "id": thread_id,
        "nombre": "Conversación 1",
        "creado": datetime.now().strftime("%Y-%m-%d %H:%M")
    })

# Mensajes de la conversación actual
if "messages" not in st.session_state:
    st.session_state.messages = []

# Flag para saber si ya cargamos el historial del servidor
if "historial_cargado" not in st.session_state:
    st.session_state.historial_cargado = False

# ========================================
# CARGAR HISTORIAL DEL SERVIDOR AL INICIAR
# ========================================

def cargar_historial_desde_servidor():
    """Carga el historial de la conversación actual desde el servidor"""
    if not st.session_state.historial_cargado:
        resultado = obtener_historial(st.session_state.current_thread_id)
        
        if resultado["success"] and resultado["history"]:
            # Convertir el formato del servidor al formato de Streamlit
            st.session_state.messages = []
            for msg in resultado["history"]:
                role = "user" if msg["type"] == "human" else "assistant"
                st.session_state.messages.append({
                    "role": role,
                    "content": msg["content"]
                })
            st.session_state.historial_cargado = True

# Intentar cargar historial si aún no se ha hecho
if verificar_conexion_api():
    cargar_historial_desde_servidor()

# ========================================
# HEADER
# ========================================

st.title("💬 Chat con SegurosVida+")
st.caption("🚀 Paso 3: Gestión de historial y múltiples conversaciones")

# ========================================
# SIDEBAR - GESTIÓN DE CONVERSACIONES
# ========================================

with st.sidebar:
    st.header("💬 Conversaciones")
    
    # Estado de conexión
    api_conectado = verificar_conexion_api()
    if api_conectado:
        st.success("✅ Conectado")
    else:
        st.error("❌ Desconectado")
    
    st.divider()
    
    # Botón para nueva conversación
    if st.button("➕ Nueva Conversación", use_container_width=True):
        # Generar nuevo thread ID único
        thread_id = f"conv_{uuid.uuid4().hex[:8]}"
        numero = len(st.session_state.threads) + 1
        
        st.session_state.threads.append({
            "id": thread_id,
            "nombre": f"Conversación {numero}",
            "creado": datetime.now().strftime("%Y-%m-%d %H:%M")
        })
        
        # Cambiar a la nueva conversación
        st.session_state.current_thread_id = thread_id
        st.session_state.messages = []
        st.session_state.historial_cargado = False
        st.rerun()
    
    st.divider()
    
    # Lista de conversaciones
    st.subheader("Historial")
    
    for thread in st.session_state.threads:
        # Marcar la conversación actual
        is_current = thread["id"] == st.session_state.current_thread_id
        
        # Botón para seleccionar conversación
        button_label = f"{'📍' if is_current else '💬'} {thread['nombre']}"
        
        if st.button(button_label, key=thread["id"], use_container_width=True):
            if not is_current:
                # Cambiar a esta conversación
                st.session_state.current_thread_id = thread["id"]
                st.session_state.messages = []
                st.session_state.historial_cargado = False
                st.rerun()
        
        # Mostrar fecha de creación
        st.caption(f"Creado: {thread['creado']}")
    
    st.divider()
    
    # Información
    with st.expander("ℹ️ Info"):
        st.write(f"""
        **Paso 3 de 4**
        
        Thread actual: `{st.session_state.current_thread_id[:12]}...`
        
        Mensajes en esta conversación: {len(st.session_state.messages)}
        
        Total de conversaciones: {len(st.session_state.threads)}
        """)
    
    st.divider()
    
    # Botón para limpiar conversación actual
    if st.button("🗑️ Limpiar esta conversación"):
        st.session_state.messages = []
        st.session_state.historial_cargado = True  # No recargar del servidor
        st.rerun()

# ========================================
# MOSTRAR HISTORIAL DE MENSAJES
# ========================================

# Mostrar thread ID actual
st.caption(f"📍 Conversación actual: {st.session_state.current_thread_id}")

# Mostrar mensajes
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])

# ========================================
# INPUT DEL USUARIO
# ========================================

if prompt := st.chat_input("Escribe tu mensaje aquí...", disabled=not api_conectado):
    
    # Agregar mensaje del usuario
    st.session_state.messages.append({
        "role": "user",
        "content": prompt
    })
    
    with st.chat_message("user"):
        st.write(prompt)
    
    # Obtener respuesta del agente
    with st.chat_message("assistant"):
        with st.spinner("Pensando..."):
            resultado = enviar_mensaje_al_agente(
                mensaje=prompt,
                thread_id=st.session_state.current_thread_id
            )
            
            if resultado["success"]:
                respuesta = resultado["response"]
                st.write(respuesta)
                
                st.session_state.messages.append({
                    "role": "assistant",
                    "content": respuesta
                })
            else:
                error_msg = resultado["error"]
                st.error(f"Error: {error_msg}")
                
                st.session_state.messages.append({
                    "role": "assistant",
                    "content": f"❌ {error_msg}"
                })

# ========================================
# MENSAJE INICIAL
# ========================================

if len(st.session_state.messages) == 0:
    st.info("""
    👋 **¡Bienvenido a SegurosVida+!**
    
    Esta es una nueva conversación. Puedo ayudarte con:
    - 🏥 Información sobre seguros
    - 💰 Precios y cotizaciones
    - 📞 Contacto y soporte
    
    **Tip**: Usa el sidebar para crear o cambiar entre conversaciones
    """)

# ========================================
# EXPLICACIÓN
# ========================================

with st.expander("💡 Explicación del código - Paso 3"):
    st.markdown("""
    ### Nuevas funcionalidades
    
    **1. Obtener historial del servidor**
    ```python
    response = requests.get(f"{API_URL}/history/{thread_id}")
    data = response.json()
    history = data["history"]
    
    # Convertir formato
    for msg in history:
        role = "user" if msg["type"] == "human" else "assistant"
        messages.append({"role": role, "content": msg["content"]})
    ```
    
    **2. Múltiples conversaciones (threads)**
    ```python
    # Generar ID único
    thread_id = f"conv_{uuid.uuid4().hex[:8]}"
    
    # Guardar metadata
    st.session_state.threads.append({
        "id": thread_id,
        "nombre": "Conversación 1",
        "creado": datetime.now()
    })
    ```
    
    **3. Cambiar entre conversaciones**
    - Cada conversación tiene su propio thread_id
    - Al cambiar, se carga el historial del servidor
    - Los mensajes persisten en el servidor
    
    **4. Cargar historial automáticamente**
    - Al iniciar la app, se carga el historial
    - Permite continuar conversaciones previas
    - Solo se carga una vez por thread
    
    ### ⏭️ Siguiente paso
    En el Paso 4 (final) agregaremos:
    - Interfaz más pulida
    - Mejor gestión de threads
    - Opciones adicionales
    - Código optimizado y limpio
    """)

# ========================================
# DEBUG
# ========================================

with st.expander("🔧 Debug"):
    st.write("**Session State:**")
    st.json({
        "current_thread_id": st.session_state.current_thread_id,
        "num_messages": len(st.session_state.messages),
        "num_threads": len(st.session_state.threads),
        "historial_cargado": st.session_state.historial_cargado
    })
    
    if st.button("Ver todos los threads"):
        st.json(st.session_state.threads)
