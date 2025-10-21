"""
REFERENCIA DE CÓDIGO - Snippets Útiles para Dash

Este archivo contiene ejemplos de código que puedes copiar y adaptar
para tu aplicación. Todos los ejemplos están comentados en español.

CÓMO USAR ESTE ARCHIVO:
1. Busca el componente o patrón que necesitas
2. Copia el código de ejemplo
3. Ad aptalo a tu aplicación
4. Modifica los IDs y textos según necesites

SECCIONES:
1. Componentes HTML Básicos
2. Componentes Core (dcc)
3. Componentes Bootstrap (dbc)
4. Patrones de Callbacks
5. Manejo de APIs
6. Estilos y Layout
"""

# ============================================
# 1. COMPONENTES HTML BÁSICOS
# ============================================

"""
Los componentes html.* representan etiquetas HTML estándar.
Todos tienen las propiedades:
- id: identificador único
- className: clases CSS
- style: estilos inline (diccionario)
- children: contenido interno
"""

# Contenedores
from dash import html

contenedor_simple = html.Div([
    html.H1("Título Principal"),
    html.P("Esto es un párrafo")
])

# Textos y formato
textos = html.Div([
    html.H1("Título 1"),
    html.H2("Título 2"),
    html.H3("Título 3"),
    html.P("Párrafo normal"),
    html.Strong("Texto en negrita"),
    html.Em("Texto en cursiva"),
    html.Small("Texto pequeño")
])

# Listas
lista_desordenada = html.Ul([
    html.Li("Item 1"),
    html.Li("Item 2"),
    html.Li("Item 3")
])

lista_ordenada = html.Ol([
    html.Li("Primero"),
    html.Li("Segundo"),
    html.Li("Tercero")
])

# Enlaces e imágenes
enlace = html.A("Click aquí", href="https://dash.plotly.com/")
imagen = html.Img(src="/assets/logo.png", alt="Logo", style={'width': '100px'})

# ============================================
# 2. COMPONENTES CORE (dcc)
# ============================================

"""
Los componentes dcc.* son específicos de Dash y proporcionan
funcionalidad interactiva avanzada.
"""

from dash import dcc

# Input de texto simple
input_texto = dcc.Input(
    id='mi-input',
    type='text',  # text, number, email, password, search
    placeholder='Escribe algo...',
    value='',  # Valor inicial
    debounce=True,  # Espera a que el usuario termine de escribir
    style={'width': '100%'}
)

# Textarea (multilínea)
textarea = dcc.Textarea(
    id='mi-textarea',
    placeholder='Escribe un mensaje largo...',
    value='',
    style={
        'width': '100%',
        'height': '150px',
        'resize': 'none'  # Deshabilitar redimensionamiento
    }
)

# Dropdown (menú desplegable)
dropdown = dcc.Dropdown(
    id='mi-dropdown',
    options=[
        {'label': 'Opción 1', 'value': '1'},
        {'label': 'Opción 2', 'value': '2'},
        {'label': 'Opción 3', 'value': '3'}
    ],
    value='1',  # Valor seleccionado por defecto
    multi=False,  # True para selección múltiple
    searchable=True,
    clearable=True
)

# Loading (spinner de carga)
loading = dcc.Loading(
    id="loading-1",
    type="circle",  # circle, default, graph, cube, dot
    children=[
        html.Div(id="contenido-que-carga")
    ]
)

# Store (almacenamiento en el navegador)
store = dcc.Store(
    id='mi-store',
    storage_type='session',  # memory, local, session
    data={'clave': 'valor'}  # Datos iniciales
)

# Interval (timer)
interval = dcc.Interval(
    id='mi-interval',
    interval=5000,  # milisegundos (5000 = 5 segundos)
    n_intervals=0,  # Contador de ejecuciones
    max_intervals=100,  # Máximo de ejecuciones (-1 = infinito)
    disabled=False  # True para pausar
)

# Markdown
markdown = dcc.Markdown('''
# Título en Markdown
Este texto está en **negrita** y esto en *cursiva*.

- Lista item 1
- Lista item 2
- Lista item 3

[Enlace a Dash](https://dash.plotly.com/)
''')

# ============================================
# 3. COMPONENTES BOOTSTRAP (dbc)
# ============================================

"""
Los componentes dbc.* proporcionan componentes de Bootstrap
con estilos modernos y profesionales.
"""

import dash_bootstrap_components as dbc

# Container (contenedor responsive)
container = dbc.Container([
    html.H1("Contenido dentro del container")
], fluid=False)  # fluid=True para ancho completo

# Grid System (filas y columnas)
grid = dbc.Container([
    dbc.Row([
        dbc.Col([
            html.Div("Columna 1")
        ], width=6, lg=4, md=6, sm=12),  # Responsive
        
        dbc.Col([
            html.Div("Columna 2")
        ], width=6, lg=8, md=6, sm=12)
    ])
])

# Card (tarjeta)
card = dbc.Card([
    dbc.CardHeader("Encabezado de la Card"),
    dbc.CardBody([
        html.H5("Título", className="card-title"),
        html.P("Contenido de la card"),
        dbc.Button("Acción", color="primary")
    ]),
    dbc.CardFooter("Pie de la card")
], color="light", outline=True)

# Button (botón)
boton = dbc.Button(
    "Click aquí",
    id="mi-boton",
    color="primary",  # primary, secondary, success, danger, warning, info
    size="lg",  # sm, md, lg
    outline=False,  # True para botón con borde
    disabled=False,
    n_clicks=0  # Contador de clicks
)

# Alert (alerta/notificación)
alert = dbc.Alert(
    "Este es un mensaje de alerta",
    color="success",  # success, info, warning, danger
    dismissable=True,  # True para permitir cerrar
    is_open=True
)

# Badge (etiqueta)
badge = dbc.Badge(
    "Nuevo",
    color="primary",
    pill=True,  # True para redondeado
    className="ms-2"
)

# Navbar (barra de navegación)
navbar = dbc.Navbar(
    dbc.Container([
        dbc.NavbarBrand("Mi App", href="#"),
        dbc.Nav([
            dbc.NavItem(dbc.NavLink("Inicio", href="#")),
            dbc.NavItem(dbc.NavLink("Acerca", href="#"))
        ])
    ]),
    color="dark",
    dark=True,
    className="mb-4"
)

# Spinner (indicador de carga)
spinner = dbc.Spinner(
    color="primary",
    type="border",  # border, grow
    size="lg"  # sm, md, lg
)

# ============================================
# 4. PATRONES DE CALLBACKS
# ============================================

"""
Los callbacks son funciones que se ejecutan cuando cambia
algo en la interfaz. Son el corazón de la interactividad en Dash.
"""

from dash import callback, Input, Output, State, ctx
from dash.exceptions import PreventUpdate

# Callback básico (1 input, 1 output)
@callback(
    Output('output-id', 'children'),
    Input('input-id', 'value')
)
def actualizar_output(valor_input):
    """Se ejecuta cada vez que cambia el input"""
    return f'Escribiste: {valor_input}'


# Callback con múltiples inputs
@callback(
    Output('resultado', 'children'),
    [Input('input-1', 'value'),
     Input('input-2', 'value')]
)
def combinar_inputs(val1, val2):
    """Se ejecuta cuando cambia cualquiera de los inputs"""
    return f'{val1} + {val2} = {val1 + val2}'


# Callback con State (no dispara el callback)
@callback(
    Output('resultado', 'children'),
    Input('boton', 'n_clicks'),
    State('input', 'value')
)
def procesar_al_hacer_click(n_clicks, valor_input):
    """Se ejecuta solo cuando se hace click en el botón"""
    if n_clicks:
        return f'Valor capturado: {valor_input}'
    return 'Presiona el botón'


# Callback con múltiples outputs
@callback(
    [Output('output-1', 'children'),
     Output('output-2', 'children'),
     Output('output-3', 'style')],
    Input('input', 'value')
)
def actualizar_multiples_outputs(valor):
    """Actualiza varios componentes a la vez"""
    return f'Output 1: {valor}', f'Output 2: {valor.upper()}', {'color': 'red'}


# Callback que previene actualizaciones innecesarias
@callback(
    Output('output', 'children'),
    Input('input', 'value'),
    prevent_initial_call=True  # No ejecuta al cargar la página
)
def solo_cuando_cambia(valor):
    """Solo se ejecuta cuando el usuario cambia el input"""
    if not valor:
        raise PreventUpdate  # No actualizar si está vacío
    return valor


# Callback con contexto (saber qué lo disparó)
@callback(
    Output('resultado', 'children'),
    [Input('boton-1', 'n_clicks'),
     Input('boton-2', 'n_clicks'),
     Input('boton-3', 'n_clicks')]
)
def cual_boton_se_presiono(btn1, btn2, btn3):
    """Determina cuál botón disparó el callback"""
    if not ctx.triggered:
        return "Ningún botón presionado"
    
    boton_id = ctx.triggered_id
    
    if boton_id == 'boton-1':
        return "Se presionó el botón 1"
    elif boton_id == 'boton-2':
        return "Se presionó el botón 2"
    elif boton_id == 'boton-3':
        return "Se presionó el botón 3"


# Callback con botones dinámicos (pattern-matching)
@callback(
    Output('resultado', 'children'),
    Input({'type': 'boton-dinamico', 'index': dbc.ALL}, 'n_clicks')
)
def botones_dinamicos(lista_clicks):
    """Funciona con cualquier número de botones con el mismo patrón"""
    if not ctx.triggered:
        return "Ningún botón presionado"
    
    boton_id = ctx.triggered_id
    indice = boton_id['index']
    
    return f"Se presionó el botón índice: {indice}"


# ============================================
# 5. MANEJO DE APIs
# ============================================

"""
Ejemplos de cómo hacer llamadas a APIs REST usando requests.
"""

import requests

# GET request simple
def hacer_get_request():
    """Ejemplo de GET request básico"""
    try:
        response = requests.get(
            'http://localhost:8000/api/datos',
            timeout=5  # Timeout en segundos
        )
        response.raise_for_status()  # Lanza excepción si status != 200
        datos = response.json()
        return datos
    except requests.exceptions.Timeout:
        return {"error": "Timeout: el servidor no respondió"}
    except requests.exceptions.ConnectionError:
        return {"error": "Error de conexión"}
    except Exception as e:
        return {"error": f"Error: {str(e)}"}


# POST request con JSON
def hacer_post_request(datos):
    """Ejemplo de POST request enviando JSON"""
    try:
        response = requests.post(
            'http://localhost:8000/api/procesar',
            json=datos,  # Se convierte automáticamente a JSON
            headers={'Content-Type': 'application/json'},
            timeout=30
        )
        response.raise_for_status()
        resultado = response.json()
        return resultado
    except Exception as e:
        return {"error": str(e)}


# GET con parámetros de query
def get_con_parametros():
    """Ejemplo de GET con query parameters"""
    response = requests.get(
        'http://localhost:8000/api/buscar',
        params={'q': 'seguros', 'limite': 10}
    )
    # URL final: http://localhost:8000/api/buscar?q=seguros&limite=10
    return response.json()


# Usar en un callback
@callback(
    Output('respuesta-api', 'children'),
    Input('boton-enviar', 'n_clicks'),
    State('input-mensaje', 'value')
)
def llamar_api_en_callback(n_clicks, mensaje):
    """Ejemplo de cómo usar API calls dentro de callbacks"""
    if not n_clicks or not mensaje:
        raise PreventUpdate
    
    # Hacer la llamada a la API
    resultado = hacer_post_request({"mensaje": mensaje})
    
    # Manejar la respuesta
    if "error" in resultado:
        return dbc.Alert(resultado["error"], color="danger")
    else:
        return dbc.Alert(resultado["respuesta"], color="success")


# ============================================
# 6. ESTILOS Y LAYOUT
# ============================================

"""
Ejemplos de cómo aplicar estilos y crear layouts responsivos.
"""

# Estilos inline (diccionarios Python)
componente_con_estilo = html.Div(
    "Texto con estilo",
    style={
        'color': 'blue',
        'fontSize': '20px',  # Nota: camelCase, no kebab-case
        'textAlign': 'center',
        'backgroundColor': '#f0f0f0',
        'padding': '10px 20px',
        'margin': '5px',
        'border': '1px solid #ccc',
        'borderRadius': '5px',
        'boxShadow': '0 2px 4px rgba(0,0,0,0.1)'
    }
)

# Clases CSS de Bootstrap
componente_con_clases = html.Div(
    "Texto",
    className='text-center mt-3 mb-2 p-4 bg-light border rounded'
)

# Layout responsive completo
layout_responsive = dbc.Container([
    # Header
    dbc.Row([
        dbc.Col([
            html.H1("Mi Aplicación", className="text-center")
        ])
    ], className="mb-4"),
    
    # Contenido principal
    dbc.Row([
        # Sidebar (solo visible en pantallas grandes)
        dbc.Col([
            dbc.Card([
                dbc.CardBody([
                    html.H5("Menú"),
                    html.Hr(),
                    html.P("Opción 1"),
                    html.P("Opción 2")
                ])
            ])
        ], width=12, lg=3, className="mb-3"),  # 100% en móvil, 25% en desktop
        
        # Área principal
        dbc.Col([
            dbc.Card([
                dbc.CardBody([
                    html.H5("Contenido Principal"),
                    html.P("Aquí va el contenido...")
                ])
            ])
        ], width=12, lg=9)  # 100% en móvil, 75% en desktop
    ])
], fluid=False)

# Utilidades de spacing de Bootstrap:
# Margin: m-1, mt-2, mb-3, ms-4, me-5 (start/end = left/right)
# Padding: p-1, pt-2, pb-3, ps-4, pe-5
# Tamaños: 0, 1, 2, 3, 4, 5, auto

# ============================================
# 7. EJEMPLO COMPLETO: CHAT SIMPLE
# ============================================

"""
Ejemplo completo de una aplicación de chat simple.
Este es un patrón común que puedes adaptar.
"""

from dash import Dash
import dash_bootstrap_components as dbc
from dash import html, dcc, callback, Input, Output, State
from datetime import datetime

# Crear aplicación
app_ejemplo = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

# Layout
app_ejemplo.layout = dbc.Container([
    # Título
    html.H1("Chat Simple", className="text-center my-4"),
    
    # Área de mensajes
    dbc.Card([
        dbc.CardBody([
            html.Div(
                id='mensajes-display',
                style={'height': '400px', 'overflowY': 'auto'}
            )
        ])
    ], className="mb-3"),
    
    # Input
    dbc.Row([
        dbc.Col([
            dcc.Textarea(
                id='mensaje-input',
                placeholder='Escribe un mensaje...',
                style={'width': '100%', 'height': '80px'}
            )
        ], width=9),
        dbc.Col([
            dbc.Button(
                "Enviar",
                id='enviar-btn',
                color='primary',
                className="w-100 h-100",
                n_clicks=0
            )
        ], width=3)
    ]),
    
    # Store para guardar mensajes
    dcc.Store(id='mensajes-store', data=[])
], className="py-4", style={'maxWidth': '800px'})

# Callback para enviar mensajes
@callback(
    [Output('mensajes-store', 'data'),
     Output('mensaje-input', 'value')],
    Input('enviar-btn', 'n_clicks'),
    [State('mensaje-input', 'value'),
     State('mensajes-store', 'data')],
    prevent_initial_call=True
)
def agregar_mensaje(n_clicks, mensaje, mensajes_actuales):
    """Agrega un nuevo mensaje a la lista"""
    if not mensaje or not mensaje.strip():
        return mensajes_actuales, ''
    
    mensajes_actuales.append({
        'texto': mensaje.strip(),
        'hora': datetime.now().strftime("%H:%M:%S")
    })
    
    return mensajes_actuales, ''  # Retorna lista actualizada y limpia input

# Callback para renderizar mensajes
@callback(
    Output('mensajes-display', 'children'),
    Input('mensajes-store', 'data')
)
def mostrar_mensajes(mensajes):
    """Convierte la lista de mensajes en componentes visuales"""
    if not mensajes:
        return html.P("No hay mensajes aún", className="text-muted text-center")
    
    componentes = []
    for msg in mensajes:
        componentes.append(
            dbc.Alert([
                html.Small(msg['hora'], className="text-muted d-block mb-1"),
                html.Span(msg['texto'])
            ], color="light", className="mb-2")
        )
    
    return componentes

# ============================================
# FIN DE LA REFERENCIA
# ============================================

"""
TIPS FINALES:

1. Siempre usa IDs únicos para cada componente
2. Los callbacks no pueden tener el mismo Output
3. Usa prevent_initial_call=True para evitar ejecuciones al cargar
4. PreventUpdate es útil para evitar actualizaciones innecesarias
5. El contexto (ctx) es muy útil para callbacks complejos
6. Siempre maneja errores en las llamadas a APIs
7. Usa Loading para dar feedback visual
8. Bootstrap classes hacen el diseño mucho más fácil
9. dcc.Store es perfecto para mantener estado
10. Consulta la documentación oficial para más detalles

DOCUMENTACIÓN OFICIAL:
- Dash: https://dash.plotly.com/
- Dash Bootstrap: https://dash-bootstrap-components.opensource.faculty.ai/
- Requests: https://requests.readthedocs.io/

¡Buena suerte con tu aplicación!
"""

