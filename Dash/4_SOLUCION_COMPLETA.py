"""
SOLUCIÓN COMPLETA - Chat de Seguros Bolívar con Dash

Esta es una implementación de referencia que muestra cómo construir
una interfaz de chat completa que se conecta con la API del agente de seguros.

CARACTERÍSTICAS IMPLEMENTADAS:
✅ Chat interactivo con el agente de seguros
✅ Historial de conversación persistente
✅ Indicador de estado de conexión con la API
✅ Loading spinners durante las llamadas a la API
✅ Diseño profesional y responsive
✅ Manejo de errores robusto
✅ Timestamps en los mensajes
✅ Formato markdown en respuestas del agente

NOTA: Esta es UNA forma de resolver el ejercicio.
Hay muchas otras formas válidas de implementarlo.
"""

from dash import Dash, html, dcc, callback, Input, Output, State, ctx
import dash_bootstrap_components as dbc
import requests
from datetime import datetime

# ============================================
# CONFIGURACIÓN
# ============================================

API_URL = "http://localhost:8000"
THREAD_ID = f"dash_user_{datetime.now().strftime('%Y%m%d_%H%M%S')}"

# ============================================
# FUNCIONES PARA LLAMAR A LA API
# ============================================

def verificar_api():
    """
    Verifica si la API está disponible haciendo una llamada al endpoint /health.
    
    Returns:
        bool: True si la API responde correctamente, False en caso contrario
    """
    try:
        response = requests.get(f"{API_URL}/health", timeout=3)
        return response.status_code == 200
    except:
        return False


def enviar_mensaje_api(mensaje, thread_id):
    """
    Envía un mensaje al agente de seguros y obtiene la respuesta.
    
    Args:
        mensaje (str): El mensaje del usuario
        thread_id (str): ID único de la conversación
        
    Returns:
        dict: Respuesta de la API con formato {"response": "...", "thread_id": "..."}
              o {"error": "..."} si hay algún error
    """
    try:
        response = requests.post(
            f"{API_URL}/chat",
            json={"message": mensaje, "thread_id": thread_id},
            timeout=30  # 30 segundos porque las respuestas de IA pueden tardar
        )
        response.raise_for_status()
        return response.json()
    except requests.exceptions.Timeout:
        return {"error": "La solicitud tomó demasiado tiempo. Intenta nuevamente."}
    except requests.exceptions.ConnectionError:
        return {"error": "No se pudo conectar con la API. Verifica que esté corriendo."}
    except Exception as e:
        return {"error": f"Error: {str(e)}"}


def obtener_historial_api(thread_id):
    """
    Obtiene el historial completo de conversación para un thread_id.
    (No se usa en esta implementación porque manejamos el historial localmente,
     pero es útil si quieres sincronizar con el servidor)
    
    Args:
        thread_id (str): ID de la conversación
        
    Returns:
        list: Lista de mensajes del historial
    """
    try:
        response = requests.get(f"{API_URL}/history/{thread_id}", timeout=5)
        response.raise_for_status()
        data = response.json()
        return data.get("history", [])
    except:
        return []


# ============================================
# CREAR LA APLICACIÓN DASH
# ============================================

app = Dash(
    __name__,
    external_stylesheets=[dbc.themes.BOOTSTRAP],  # Tema base de Bootstrap
    suppress_callback_exceptions=True
)

app.title = "Seguros Bolívar Chat"

# ============================================
# COMPONENTES DE LA UI
# ============================================

def crear_header():
    """
    Crea la barra de navegación superior con el logo y estado de la API.
    
    Componentes:
    - Nombre de la empresa
    - Lema
    - Badge que muestra el estado de conexión (se actualiza con callback)
    """
    return dbc.Navbar(
        dbc.Container([
            dbc.Row([
                # Columna izquierda: Logo y lema
                dbc.Col([
                    html.Div([
                        dbc.NavbarBrand(
                            "🛡️ Seguros Bolívar",
                            className="ms-2",
                            style={"fontSize": "24px", "fontWeight": "bold"}
                        ),
                        html.P(
                            "Protegiendo lo que más valoras",
                            className="mb-0 text-muted",
                            style={"fontSize": "14px", "marginLeft": "10px"}
                        )
                    ])
                ], width="auto"),
                
                # Columna derecha: Indicador de estado
                dbc.Col([
                    dbc.Badge(
                        [html.I(className="bi bi-circle-fill me-2"), ""],
                        id="estado-api",
                        color="secondary",
                        className="ms-auto",
                        pill=True
                    )
                ], width="auto", className="ms-auto")
            ], align="center", className="w-100")
        ], fluid=True),
        color="success",  # Verde de Bootstrap
        dark=True,
        className="mb-4",
        style={"background": "linear-gradient(135deg, #00A651 0%, #008040 100%)"}  # Colores Bolívar
    )


def crear_area_mensajes():
    """
    Crea el área principal donde se muestran los mensajes del chat.
    
    Características:
    - Scroll automático cuando hay muchos mensajes
    - Loading spinner mientras se espera respuesta
    - Altura fija de 450px
    """
    return dbc.Card([
        dbc.CardHeader([
            html.I(className="bi bi-chat-dots me-2"),
            "Conversación"
        ]),
        dbc.CardBody([
            dcc.Loading(
                id="loading-chat",
                type="circle",
                children=[
                    html.Div(
                        id='chat-display',
                        style={
                            'height': '450px',
                            'overflowY': 'auto',
                            'padding': '10px'
                        }
                    )
                ]
            )
        ])
    ], className="mb-3")


def crear_area_input():
    """
    Crea el área de input donde el usuario escribe mensajes.
    
    Componentes:
    - Textarea para escribir mensajes multilínea
    - Botón de enviar
    """
    return dbc.Card([
        dbc.CardBody([
            dbc.Row([
                dbc.Col([
                    dcc.Textarea(
                        id='mensaje-input',
                        placeholder='Escribe tu pregunta sobre seguros aquí...',
                        style={
                            'width': '100%',
                            'height': '100px',
                            'resize': 'none',
                            'borderRadius': '5px',
                            'padding': '10px'
                        },
                        className="form-control"
                    )
                ], width=12, className="mb-2"),
            ]),
            dbc.Row([
                dbc.Col([
                    dbc.Button(
                        [html.I(className="bi bi-send me-2"), "Enviar"],
                        id='enviar-btn',
                        color='primary',
                        size='lg',
                        className="w-100",
                        n_clicks=0
                    )
                ], width=12)
            ])
        ])
    ])


# ============================================
# LAYOUT PRINCIPAL
# ============================================

app.layout = dbc.Container([
    # Header con logo y estado
    crear_header(),
    
    # Contenido principal - centrado y responsive
    dbc.Row([
        dbc.Col([
            # Área de mensajes
            crear_area_mensajes(),
            
            # Área de input
            crear_area_input(),
            
            # Info del sistema (opcional - útil para debugging)
            html.Div([
                html.Small([
                    html.I(className="bi bi-info-circle me-2"),
                    f"Thread ID: {THREAD_ID}"
                ], className="text-muted")
            ], className="mt-3 text-center")
        ], lg=8, md=10, sm=12, className="mx-auto")
        # lg=8: 8 columnas en pantallas grandes (66% del ancho)
        # md=10: 10 columnas en tablets (83% del ancho)
        # sm=12: 12 columnas en móviles (100% del ancho)
    ]),
    
    # Store para mantener el historial de mensajes en el navegador
    dcc.Store(id='historial-store', data=[], storage_type='session'),
    
    # Interval para verificar estado de API cada 5 segundos
    dcc.Interval(
        id='api-check-interval',
        interval=5000,  # milisegundos
        n_intervals=0
    )
], fluid=True, className="py-4", style={"backgroundColor": "#FFFFFF", "minHeight": "100vh"})

# ============================================
# CALLBACKS
# ============================================

@callback(
    [Output('estado-api', 'children'),
     Output('estado-api', 'color')],
    Input('api-check-interval', 'n_intervals')
)
def actualizar_estado_api(n):
    """
    Callback que verifica el estado de la API cada 5 segundos.
    
    Args:
        n: Número de veces que se ha ejecutado el interval
        
    Returns:
        tuple: (texto del badge, color del badge)
    """
    if verificar_api():
        return [html.I(className="bi bi-circle-fill me-2"), "Conectado"], "success"
    else:
        return [html.I(className="bi bi-circle-fill me-2"), "Desconectado"], "danger"


@callback(
    [Output('historial-store', 'data'),
     Output('mensaje-input', 'value')],
    Input('enviar-btn', 'n_clicks'),
    [State('mensaje-input', 'value'),
     State('historial-store', 'data')],
    prevent_initial_call=True  # No ejecutar al cargar la página
)
def procesar_mensaje(n_clicks, mensaje, historial_actual):
    """
    Callback principal que procesa el envío de mensajes.
    
    Flujo:
    1. Validar que hay mensaje
    2. Agregar mensaje del usuario al historial
    3. Llamar a la API
    4. Agregar respuesta del agente al historial
    5. Retornar historial actualizado y limpiar input
    
    Args:
        n_clicks: Número de clicks en el botón
        mensaje: Texto del mensaje actual
        historial_actual: Lista de mensajes previos
        
    Returns:
        tuple: (historial actualizado, texto del input limpio)
    """
    # Validar que haya un mensaje
    if not mensaje or not mensaje.strip():
        return historial_actual, ''
    
    # Crear nuevo historial con el mensaje del usuario
    historial_nuevo = historial_actual.copy() if historial_actual else []
    historial_nuevo.append({
        "type": "human",
        "content": mensaje.strip(),
        "timestamp": datetime.now().strftime("%H:%M:%S")
    })
    
    # Enviar mensaje a la API del agente
    respuesta = enviar_mensaje_api(mensaje.strip(), THREAD_ID)
    
    # Agregar respuesta al historial
    if "error" in respuesta:
        # Si hay error, agregarlo como mensaje de error
        historial_nuevo.append({
            "type": "error",
            "content": respuesta["error"],
            "timestamp": datetime.now().strftime("%H:%M:%S")
        })
    else:
        # Si todo salió bien, agregar respuesta del agente
        historial_nuevo.append({
            "type": "ai",
            "content": respuesta.get("response", "Sin respuesta"),
            "timestamp": datetime.now().strftime("%H:%M:%S")
        })
    
    # Retornar historial actualizado y limpiar el campo de texto
    return historial_nuevo, ''


@callback(
    Output('chat-display', 'children'),
    Input('historial-store', 'data')
)
def actualizar_chat_display(historial):
    """
    Callback que renderiza el historial de mensajes en la interfaz.
    
    Convierte la lista de mensajes (dicts) en componentes visuales de Dash.
    Diferentes estilos para cada tipo de mensaje:
    - human: Alert azul alineado a la derecha
    - ai: Alert gris alineado a la izquierda con Markdown
    - error: Alert rojo centrado
    
    Args:
        historial: Lista de diccionarios con los mensajes
        
    Returns:
        list: Lista de componentes de Dash para renderizar
    """
    # Si no hay mensajes, mostrar mensaje de bienvenida
    if not historial:
        return html.Div([
            html.Div([
                html.I(className="bi bi-chat-text", 
                       style={"fontSize": "48px", "color": "#FFD100"}),  # Amarillo Bolívar
                html.P(
                    "¡Bienvenido a Seguros Bolívar!",
                    className="mt-3",
                    style={"fontSize": "18px", "color": "#00A651", "fontWeight": "600"}  # Verde Bolívar
                ),
                html.P(
                    "Escribe tu pregunta sobre seguros para comenzar.",
                    style={"color": "#666"}
                )
            ], className="text-center", style={"marginTop": "100px"})
        ])
    
    # Convertir cada mensaje en un componente visual
    mensajes = []
    for msg in historial:
        tipo = msg.get("type")
        contenido = msg.get("content", "")
        timestamp = msg.get("timestamp", "")
        
        if tipo == "human":
            # Mensaje del usuario (derecha, azul)
            mensajes.append(
                html.Div([
                    html.Div([
                        html.Small(timestamp, className="text-muted d-block mb-1"),
                        dbc.Alert([
                            html.I(className="bi bi-person-circle me-2"),
                            contenido
                        ], color="primary", className="mb-0")
                    ], style={"maxWidth": "70%", "marginLeft": "auto"})
                ], className="mb-3")
            )
        
        elif tipo == "ai":
            # Mensaje del agente (izquierda, gris)
            # Usamos Markdown para formatear las respuestas
            mensajes.append(
                html.Div([
                    html.Div([
                        html.Small(timestamp, className="text-muted d-block mb-1"),
                        dbc.Alert([
                            html.I(className="bi bi-robot me-2"),
                            dcc.Markdown(contenido)
                        ], color="light", className="mb-0")
                    ], style={"maxWidth": "70%"})
                ], className="mb-3")
            )
        
        elif tipo == "error":
            # Mensaje de error (centrado, rojo)
            mensajes.append(
                html.Div([
                    dbc.Alert([
                        html.I(className="bi bi-exclamation-triangle me-2"),
                        contenido
                    ], color="danger", className="mb-3")
                ])
            )
    
    return mensajes


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
    
    # Verificar si la API está disponible antes de iniciar
    if verificar_api():
        print("✅ API conectada correctamente")
    else:
        print("⚠️  ADVERTENCIA: No se pudo conectar con la API")
        print("   Asegúrate de que la API esté corriendo en http://localhost:8000")
        print("   Comando: cd insurance_agent_api/app && python main.py")
    
    print("=" * 60)
    print("💡 Presiona Ctrl+C para detener el servidor")
    print("=" * 60)
    
    # Iniciar el servidor de desarrollo
    app.run(debug=True, host='127.0.0.1', port=8050)
