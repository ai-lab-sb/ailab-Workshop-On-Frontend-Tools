"""
PASO 4: Aplicación Completa y Pulida
=====================================

Esta es la versión final del chat con el agente de seguros.
Incluye todas las funcionalidades y una interfaz pulida.

REQUISITO: El agente debe estar corriendo en http://localhost:8000

Características:
- ✅ Chat conversacional completo
- ✅ Múltiples conversaciones con gestión de threads
- ✅ Historial persistente del servidor
- ✅ Interfaz pulida y profesional
- ✅ Manejo robusto de errores
- ✅ Indicadores de estado
- ✅ Opciones avanzadas
"""

import streamlit as st
import requests
from datetime import datetime
import uuid
import time

# ========================================
# CONFIGURACIÓN DE LA PÁGINA
# ========================================

st.set_page_config(
    page_title="SegurosVida+ - Chat con IA",
    page_icon="🏥",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Configuración personalizada
API_URL = "http://localhost:8000"

# ========================================
# ESTILOS PERSONALIZADOS (CSS)
# ========================================

st.markdown("""
<style>
    /* Mejorar el aspecto del chat */
    .stChatMessage {
        padding: 1rem;
        border-radius: 0.5rem;
    }
    
    /* Sidebar más estético */
    [data-testid="stSidebar"] {
        background-color: #f0f2f6;
    }
    
    /* Botones más modernos */
    .stButton > button {
        width: 100%;
        border-radius: 0.5rem;
        transition: all 0.3s;
    }
    
    .stButton > button:hover {
        transform: translateY(-2px);
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
    }
</style>
""", unsafe_allow_html=True)

# ========================================
# FUNCIONES DE API
# ========================================

@st.cache_data(ttl=10)
def verificar_conexion_api() -> bool:
    """Verifica si el API está disponible (con cache de 10 segundos)"""
    try:
        response = requests.get(f"{API_URL}/health", timeout=5)
        return response.status_code == 200
    except:
        return False

def enviar_mensaje_al_agente(mensaje: str, thread_id: str) -> dict:
    """Envía un mensaje al agente y retorna la respuesta"""
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
            return {"success": False, "error": f"Error del servidor: {response.status_code}"}
            
    except requests.exceptions.Timeout:
        return {"success": False, "error": "El agente tardó demasiado en responder"}
    except requests.exceptions.ConnectionError:
        return {"success": False, "error": "No se pudo conectar. Verifica que el agente esté corriendo"}
    except Exception as e:
        return {"success": False, "error": f"Error inesperado: {str(e)}"}

def obtener_historial(thread_id: str) -> dict:
    """Obtiene el historial de mensajes del servidor"""
    try:
        response = requests.get(f"{API_URL}/history/{thread_id}", timeout=10)
        
        if response.status_code == 200:
            data = response.json()
            return {"success": True, "history": data["history"]}
        else:
            return {"success": False, "error": f"Error: {response.status_code}"}
            
    except Exception as e:
        return {"success": False, "error": str(e)}

# ========================================
# FUNCIONES AUXILIARES
# ========================================

def crear_nueva_conversacion() -> str:
    """Crea una nueva conversación y retorna el thread_id"""
    thread_id = f"conv_{uuid.uuid4().hex[:8]}"
    numero = len(st.session_state.threads) + 1
    
    st.session_state.threads.append({
        "id": thread_id,
        "nombre": f"Conversación {numero}",
        "creado": datetime.now().strftime("%d/%m/%Y %H:%M"),
        "ultimo_mensaje": None
    })
    
    return thread_id

def cambiar_conversacion(thread_id: str):
    """Cambia a una conversación diferente"""
    st.session_state.current_thread_id = thread_id
    st.session_state.messages = []
    st.session_state.historial_cargado = False
    cargar_historial_desde_servidor()

def cargar_historial_desde_servidor():
    """Carga el historial de la conversación actual desde el servidor"""
    if not st.session_state.historial_cargado:
        resultado = obtener_historial(st.session_state.current_thread_id)
        
        if resultado["success"] and resultado["history"]:
            st.session_state.messages = []
            for msg in resultado["history"]:
                role = "user" if msg["type"] == "human" else "assistant"
                st.session_state.messages.append({
                    "role": role,
                    "content": msg["content"]
                })
        
        st.session_state.historial_cargado = True

def actualizar_ultimo_mensaje(thread_id: str, mensaje: str):
    """Actualiza el último mensaje de un thread en el sidebar"""
    for thread in st.session_state.threads:
        if thread["id"] == thread_id:
            # Truncar mensaje si es muy largo
            preview = mensaje[:50] + "..." if len(mensaje) > 50 else mensaje
            thread["ultimo_mensaje"] = preview
            break

# ========================================
# INICIALIZAR SESSION STATE
# ========================================

if "threads" not in st.session_state:
    st.session_state.threads = []

if "current_thread_id" not in st.session_state:
    thread_id = crear_nueva_conversacion()
    st.session_state.current_thread_id = thread_id

if "messages" not in st.session_state:
    st.session_state.messages = []

if "historial_cargado" not in st.session_state:
    st.session_state.historial_cargado = False

if "mostrar_opciones" not in st.session_state:
    st.session_state.mostrar_opciones = False

# Cargar historial al iniciar
api_conectado = verificar_conexion_api()
if api_conectado and not st.session_state.historial_cargado:
    cargar_historial_desde_servidor()

# ========================================
# HEADER PRINCIPAL
# ========================================

col1, col2, col3 = st.columns([1, 3, 1])

with col1:
    st.image("https://img.icons8.com/fluency/96/000000/security-shield-green.png", width=80)

with col2:
    st.title("🏥 SegurosVida+")
    st.caption("Tu asistente inteligente de seguros | Powered by IA")

with col3:
    if api_conectado:
        st.success("🟢 En línea")
    else:
        st.error("🔴 Desconectado")

st.divider()

# ========================================
# SIDEBAR - GESTIÓN DE CONVERSACIONES
# ========================================

with st.sidebar:
    st.header("💬 Mis Conversaciones")
    
    # Botón para nueva conversación
    if st.button("➕ Nueva Conversación", type="primary", use_container_width=True):
        thread_id = crear_nueva_conversacion()
        cambiar_conversacion(thread_id)
        st.rerun()
    
    st.divider()
    
    # Lista de conversaciones
    if st.session_state.threads:
        for idx, thread in enumerate(st.session_state.threads):
            is_current = thread["id"] == st.session_state.current_thread_id
            
            # Container para cada conversación
            with st.container():
                col1, col2 = st.columns([4, 1])
                
                with col1:
                    button_type = "primary" if is_current else "secondary"
                    icon = "📍" if is_current else "💬"
                    
                    if st.button(
                        f"{icon} {thread['nombre']}",
                        key=f"thread_{thread['id']}",
                        use_container_width=True,
                        type=button_type if is_current else "secondary"
                    ):
                        if not is_current:
                            cambiar_conversacion(thread["id"])
                            st.rerun()
                
                with col2:
                    if st.button("🗑️", key=f"delete_{thread['id']}", help="Eliminar"):
                        # Eliminar conversación
                        st.session_state.threads.pop(idx)
                        
                        # Si eliminamos la actual, cambiar a otra o crear nueva
                        if is_current:
                            if st.session_state.threads:
                                cambiar_conversacion(st.session_state.threads[0]["id"])
                            else:
                                thread_id = crear_nueva_conversacion()
                                cambiar_conversacion(thread_id)
                        st.rerun()
                
                # Mostrar preview del último mensaje
                st.caption(f"📅 {thread['creado']}")
                if thread.get("ultimo_mensaje"):
                    st.caption(f"💬 {thread['ultimo_mensaje']}")
                
                st.divider()
    else:
        st.info("No hay conversaciones aún")
    
    # Opciones avanzadas
    with st.expander("⚙️ Opciones"):
        if st.button("🔄 Recargar historial", use_container_width=True):
            st.session_state.historial_cargado = False
            cargar_historial_desde_servidor()
            st.rerun()
        
        if st.button("🗑️ Limpiar esta conversación", use_container_width=True):
            st.session_state.messages = []
            st.session_state.historial_cargado = True
            st.rerun()
    
    # Información
    with st.expander("ℹ️ Información"):
        st.write(f"""
        **Thread ID:**  
        `{st.session_state.current_thread_id}`
        
        **Mensajes:**  
        {len(st.session_state.messages)}
        
        **Conversaciones:**  
        {len(st.session_state.threads)}
        
        **Estado API:**  
        {'✅ Conectado' if api_conectado else '❌ Desconectado'}
        """)
    
    st.divider()
    st.caption("© 2025 SegurosVida+")
    st.caption("v1.0.0 - Workshop Frontend")

# ========================================
# ÁREA PRINCIPAL DEL CHAT
# ========================================

# Nombre de la conversación actual
thread_actual = next((t for t in st.session_state.threads if t["id"] == st.session_state.current_thread_id), None)
if thread_actual:
    st.subheader(f"📍 {thread_actual['nombre']}")
else:
    st.subheader("📍 Conversación")

# Mostrar mensajes
if st.session_state.messages:
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.write(message["content"])
else:
    # Mensaje de bienvenida
    st.info("""
    👋 **¡Bienvenido a SegurosVida+!**
    
    Soy tu asistente virtual especializado en seguros. Puedo ayudarte con:
    
    - 🏥 **Seguros de Vida**: Protege a tu familia
    - 🚗 **Seguros de Auto**: Tu vehículo seguro
    - 🏠 **Seguros de Hogar**: Protege tu casa
    - 💊 **Seguros de Salud**: Tu salud es primero
    - ✈️ **Seguros de Viaje**: Viaja tranquilo
    
    ¿En qué puedo ayudarte hoy?
    """)

# ========================================
# INPUT DEL USUARIO
# ========================================

if not api_conectado:
    st.warning("""
    ⚠️ **El agente no está disponible**
    
    Por favor asegúrate de iniciar el agente:
    ```bash
    cd insurance_agent_api/app
    python main.py
    ```
    """)

if prompt := st.chat_input(
    "Escribe tu mensaje aquí...",
    disabled=not api_conectado,
    key="chat_input"
):
    # Agregar mensaje del usuario
    st.session_state.messages.append({"role": "user", "content": prompt})
    
    # Actualizar preview en sidebar
    actualizar_ultimo_mensaje(st.session_state.current_thread_id, prompt)
    
    # Mostrar mensaje del usuario
    with st.chat_message("user"):
        st.write(prompt)
    
    # Obtener respuesta del agente
    with st.chat_message("assistant"):
        message_placeholder = st.empty()
        
        with st.spinner("El agente está pensando..."):
            resultado = enviar_mensaje_al_agente(
                mensaje=prompt,
                thread_id=st.session_state.current_thread_id
            )
            
            if resultado["success"]:
                respuesta = resultado["response"]
                
                # Efecto de escritura (opcional)
                # message_placeholder.write(respuesta)
                st.write(respuesta)
                
                # Agregar al historial
                st.session_state.messages.append({
                    "role": "assistant",
                    "content": respuesta
                })
                
                # Actualizar preview
                actualizar_ultimo_mensaje(st.session_state.current_thread_id, respuesta)
            else:
                error_msg = f"❌ {resultado['error']}"
                st.error(error_msg)
                
                st.session_state.messages.append({
                    "role": "assistant",
                    "content": error_msg
                })

# ========================================
# FOOTER CON SUGERENCIAS
# ========================================

if len(st.session_state.messages) == 0:
    st.divider()
    st.subheader("💡 Preguntas sugeridas:")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        if st.button("¿Qué tipos de seguros ofrecen?", use_container_width=True):
            st.session_state.messages.append({
                "role": "user",
                "content": "¿Qué tipos de seguros ofrecen?"
            })
            st.rerun()
    
    with col2:
        if st.button("¿Cuánto cuesta el seguro de auto?", use_container_width=True):
            st.session_state.messages.append({
                "role": "user",
                "content": "¿Cuánto cuesta el seguro de auto?"
            })
            st.rerun()
    
    with col3:
        if st.button("¿Cómo puedo contactarlos?", use_container_width=True):
            st.session_state.messages.append({
                "role": "user",
                "content": "¿Cómo puedo contactarlos?"
            })
            st.rerun()

# ========================================
# MÉTRICAS Y ESTADÍSTICAS (OPCIONAL)
# ========================================

with st.expander("📊 Estadísticas de la conversación"):
    if st.session_state.messages:
        total_mensajes = len(st.session_state.messages)
        mensajes_usuario = sum(1 for m in st.session_state.messages if m["role"] == "user")
        mensajes_agente = sum(1 for m in st.session_state.messages if m["role"] == "assistant")
        
        col1, col2, col3 = st.columns(3)
        
        with col1:
            st.metric("Total de mensajes", total_mensajes)
        with col2:
            st.metric("Tus mensajes", mensajes_usuario)
        with col3:
            st.metric("Respuestas del agente", mensajes_agente)
    else:
        st.info("Aún no hay mensajes en esta conversación")
