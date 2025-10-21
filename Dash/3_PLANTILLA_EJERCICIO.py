"""
PLANTILLA DEL EJERCICIO - Chat de Seguros Bolívar con Dash

Tu tarea: Completar esta aplicación para crear una interfaz de chat funcional
que se conecte con la API del agente de seguros.

PASOS A SEGUIR:
1. Implementar las funciones de API (verificar_api, enviar_mensaje_api, obtener_historial_api)
2. Completar las funciones de layout (crear_header, crear_area_mensajes, crear_area_input)
3. Ensamblar el layout principal
4. Implementar los callbacks (actualizar_estado_api, procesar_mensaje, actualizar_chat_display)
5. Probar la aplicación

AYUDA DISPONIBLE:
- 2_GUIA_EJERCICIO.md: Guía paso a paso con código de ejemplo
- 5_REFERENCIA_CODIGO.py: Snippets de código útiles
- 4_SOLUCION_COMPLETA.py: Solución completa (último recurso)

¡Buena suerte!
"""

from dash import Dash, html, dcc, callback, Input, Output, State, ctx
import dash_bootstrap_components as dbc
import requests
from datetime import datetime

# ============================================
# CONFIGURACIÓN
# ============================================

# URL base de la API del agente de seguros
API_URL = "http://localhost:8000"

# Generar un thread_id único para esta sesión
THREAD_ID = f"dash_user_{datetime.now().strftime('%Y%m%d_%H%M%S')}"

# ============================================
# FUNCIONES PARA LLAMAR A LA API
# ============================================

def verificar_api():
    """
    Verifica si la API está disponible.
    
    Returns:
        bool: True si la API está funcionando, False si no
    """
    # TODO: Implementar llamada al endpoint /health
    # Pistas:
    # - Usa requests.get(f"{API_URL}/health", timeout=3)
    # - Retorna True si response.status_code == 200
    # - Usa try/except para manejar errores
    # - Si hay cualquier error, retorna False
    
    pass  # Reemplaza esto con tu código


def enviar_mensaje_api(mensaje, thread_id):
    """
    Envía un mensaje al agente de seguros.
    
    Args:
        mensaje (str): Mensaje del usuario
        thread_id (str): ID del hilo de conversación
        
    Returns:
        dict: Respuesta de la API o dict con error
    """
    # TODO: Implementar llamada al endpoint POST /chat
    # Pistas:
    # - Usa requests.post(f"{API_URL}/chat", json={...}, timeout=30)
    # - El JSON debe incluir "message" y "thread_id"
    # - Usa response.raise_for_status() para verificar errores
    # - Maneja excepciones: Timeout, ConnectionError, Exception
    # - Retorna {"error": "mensaje"} si algo sale mal
    # - Retorna response.json() si todo sale bien
    
    pass  # Reemplaza esto con tu código


def obtener_historial_api(thread_id):
    """
    Obtiene el historial de conversación.
    
    Args:
        thread_id (str): ID del hilo de conversación
        
    Returns:
        list: Lista de mensajes del historial
    """
    # TODO: Implementar llamada al endpoint GET /history/{thread_id}
    # Pistas:
    # - Usa requests.get(f"{API_URL}/history/{thread_id}", timeout=5)
    # - Extrae el campo "history" del JSON: data.get("history", [])
    # - Si hay error, retorna lista vacía []
    
    pass  # Reemplaza esto con tu código


# ============================================
# CREAR LA APLICACIÓN DASH
# ============================================

# TODO: Crear la aplicación Dash con tema Bootstrap
# Pistas:
# - app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])
# - Puedes cambiar el tema: FLATLY, DARKLY, COSMO, etc.

app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])
app.title = "Seguros Bolívar Chat"

# ============================================
# COMPONENTES DE LA UI
# ============================================

def crear_header():
    """Crea el header de la aplicación con logo y estado de API."""
    # TODO: Crear un header atractivo
    # Debe incluir:
    # - Nombre de la empresa: "Seguros Bolívar"
    # - Lema: "Protegiendo lo que más valoras"
    # - Badge con id='estado-api' para mostrar el estado de conexión
    # 
    # Pistas:
    # - Usa dbc.Navbar con color="primary" y dark=True
    # - Usa dbc.NavbarBrand para el nombre
    # - Usa html.P para el lema
    # - Usa dbc.Badge con id="estado-api" para el indicador
    # 
    # Consulta 2_GUIA_EJERCICIO.md sección 3.1 para ver el código completo
    
    return html.Div([
        html.H1("🛡️ Seguros Bolívar"),
        html.P("TODO: Completa este header")
    ])


def crear_area_mensajes():
    """Crea el área donde se mostrarán los mensajes del chat."""
    # TODO: Crear contenedor para los mensajes
    # Debe incluir:
    # - Una dbc.Card con CardHeader y CardBody
    # - Un html.Div con id='chat-display' dentro del CardBody
    # - El div debe tener style con height='450px' y overflowY='auto'
    # - Envolver en dcc.Loading para mostrar spinner
    # 
    # Pistas:
    # - dbc.Card([dbc.CardHeader(...), dbc.CardBody(...)])
    # - dcc.Loading(children=[html.Div(...)])
    # - style={'height': '450px', 'overflowY': 'auto'}
    # 
    # Consulta 2_GUIA_EJERCICIO.md sección 3.2 para ver el código completo
    
    return html.Div([
        html.P("TODO: Aquí irán los mensajes del chat")
    ], id='chat-display')


def crear_area_input():
    """Crea el área de input para enviar mensajes."""
    # TODO: Crear el input y botón de enviar
    # Debe incluir:
    # - Una dbc.Card con CardBody
    # - dcc.Textarea con id='mensaje-input'
    # - dbc.Button con id='enviar-btn' y n_clicks=0
    # - Layout con dbc.Row y dbc.Col para organizar
    # 
    # Pistas:
    # - dcc.Textarea(..., id='mensaje-input', style={'height': '100px'})
    # - dbc.Button("Enviar", id='enviar-btn', color='primary', n_clicks=0)
    # 
    # Consulta 2_GUIA_EJERCICIO.md sección 3.3 para ver el código completo
    
    return dbc.Row([
        dbc.Col([
            html.P("TODO: Área de input - implementar")
        ])
    ])


# ============================================
# LAYOUT PRINCIPAL
# ============================================

# TODO: Ensamblar el layout completo
# Estructura requerida:
# - dbc.Container([...], fluid=True)
#   - crear_header()
#   - dbc.Row([dbc.Col([...], lg=8, className="mx-auto")])
#     - crear_area_mensajes()
#     - crear_area_input()
#   - dcc.Store(id='historial-store', data=[])
#   - dcc.Interval(id='api-check-interval', interval=5000)
# 
# Consulta 2_GUIA_EJERCICIO.md sección 3.4 para ver el código completo

app.layout = dbc.Container([
    html.H1("PLANTILLA DEL EJERCICIO"),
    html.P("TODO: Completa el layout siguiendo la guía"),
    
    # TODO: Agregar los componentes aquí
    # crear_header(),
    # crear_area_mensajes(),
    # crear_area_input(),
    # dcc.Store(id='historial-store', data=[]),
    # dcc.Interval(id='api-check-interval', interval=5000)
], fluid=True, className="py-4", style={"backgroundColor": "#FFFFFF", "minHeight": "100vh"})

# ============================================
# CALLBACKS
# ============================================

# TODO: Callback 1 - Verificar estado de la API
# Debe ejecutarse cada 5 segundos y actualizar el badge de estado
# 
# Input: 'api-check-interval', 'n_intervals'
# Output: 'estado-api', 'children' y 'estado-api', 'color'
# 
# Consulta 2_GUIA_EJERCICIO.md sección 4.1 para ver el código completo


# TODO: Callback 2 - Enviar mensaje
# Debe ejecutarse cuando se presiona el botón de enviar
# Debe agregar el mensaje al historial, llamar a la API, y agregar la respuesta
# 
# Input: 'enviar-btn', 'n_clicks'
# State: 'mensaje-input', 'value' y 'historial-store', 'data'
# Output: 'historial-store', 'data' y 'mensaje-input', 'value'
# 
# Estructura del historial:
# [
#   {"type": "human", "content": "mensaje", "timestamp": "14:30:45"},
#   {"type": "ai", "content": "respuesta", "timestamp": "14:30:47"}
# ]
# 
# Consulta 2_GUIA_EJERCICIO.md sección 4.2 para ver el código completo


# TODO: Callback 3 - Renderizar historial de mensajes
# Debe convertir el historial (lista de dicts) en componentes visuales
# Diferentes estilos para mensajes del usuario vs agente
# 
# Input: 'historial-store', 'data'
# Output: 'chat-display', 'children'
# 
# Pistas:
# - Itera sobre el historial
# - Para tipo "human": dbc.Alert color="primary" alineado a la derecha
# - Para tipo "ai": dbc.Alert color="light" alineado a la izquierda
# - Para tipo "error": dbc.Alert color="danger" centrado
# 
# Consulta 2_GUIA_EJERCICIO.md sección 4.3 para ver el código completo


# ============================================
# FUNCIÓN PRINCIPAL
# ============================================

if __name__ == '__main__':
    print("=" * 60)
    print("🚀 Iniciando aplicación Dash - Seguros Bolívar Chat")
    print("=" * 60)
    print(f"📱 URL: http://localhost:8050")
    print(f"🔗 API: {API_URL}")
    print(f"🆔 Thread ID: {THREAD_ID}")
    print("=" * 60)
    
    # Verificar si la API está disponible
    if verificar_api():
        print("✅ API conectada correctamente")
    else:
        print("⚠️  ADVERTENCIA: No se pudo conectar con la API")
        print("   Asegúrate de que la API esté corriendo en http://localhost:8000")
        print("   Comando: cd insurance_agent_api/app && python main.py")
    
    print("=" * 60)
    print("💡 Presiona Ctrl+C para detener el servidor")
    print("=" * 60)
    
    # Iniciar servidor
    app.run(debug=True, host='127.0.0.1', port=8050)

