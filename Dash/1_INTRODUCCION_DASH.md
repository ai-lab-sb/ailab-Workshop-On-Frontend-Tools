# 1. Introducción a Dash

## 📊 Bienvenido al Mundo de Dash

**Dash** es un framework de Python de código abierto creado por Plotly para construir aplicaciones web analíticas interactivas **sin necesidad de escribir JavaScript**. Es perfecto para crear dashboards, visualizaciones de datos y aplicaciones web interactivas completamente en Python.

---

## 1.1. ¿Qué es Dash?

Dash te permite crear aplicaciones web modernas usando únicamente Python. Bajo el capó, usa React.js, Plotly.js y Flask, pero tú solo necesitas saber Python.

### ✨ Características Principales

- **100% Python**: No necesitas saber HTML, CSS o JavaScript
- **Componentes Reactivos**: La interfaz se actualiza automáticamente cuando cambian los datos
- **Basado en React**: Usa React.js bajo el capó, pero lo controlas desde Python
- **Plotly Integrado**: Visualizaciones interactivas de alta calidad incluidas
- **Bootstrap Components**: Librería de componentes UI modernos
- **Listo para Producción**: Escalable y preparado para despliegue

---

## 1.2. ¿Cuándo Usar Dash?

### ✅ Ideal para:

- Dashboards analíticos y de visualización de datos
- Aplicaciones internas para equipos de data science
- Prototipos rápidos con gráficas interactivas
- Aplicaciones que requieren actualización en tiempo real
- Cuando tu equipo trabaja principalmente con Python

### ❌ No ideal para:

- Sitios web de contenido estático
- Aplicaciones que requieren SEO intensivo
- Interfaces muy complejas con muchas interacciones personalizadas

---

## 1.3. Comparación con Otras Herramientas

| Característica | Dash | Streamlit |
|----------------|------|-----------|
| Curva de Aprendizaje | Media | Muy Fácil |
| Flexibilidad | Alta | Media |
| Interactividad | Muy Alta (callbacks) | Alta (reruns) |
| Personalización UI | Muy Alta | Media |
| Performance | Mejor en apps grandes | Mejor en prototipos |
| Mejor para | Producción | Prototipos rápidos |

---

## 1.4. Arquitectura de una Aplicación Dash

```
┌─────────────────────────────────────────────┐
│           Aplicación Dash                    │
├─────────────────────────────────────────────┤
│  CAPA 1: Layout (Estructura Visual)         │
│    ├── html.Div, html.H1, html.Button      │
│    ├── dcc.Input, dcc.Graph, dcc.Dropdown   │
│    └── dbc.Card, dbc.Row, dbc.Col           │
├─────────────────────────────────────────────┤
│  CAPA 2: Callbacks (Interactividad)         │
│    ├── @app.callback                        │
│    ├── Input: dispara callbacks             │
│    ├── Output: actualiza componentes        │
│    └── State: accede sin disparar           │
├─────────────────────────────────────────────┤
│  CAPA 3: Lógica de Backend                  │
│    ├── Llamadas a APIs                      │
│    ├── Procesamiento de datos               │
│    └── Lógica de negocio                    │
└─────────────────────────────────────────────┘
```

---

## 1.5. Tu Primera Aplicación Dash

### Paso 1: Instalación

```bash
pip install dash dash-bootstrap-components requests
```

### Paso 2: Código Mínimo

```python
from dash import Dash, html, dcc, callback, Input, Output
import dash_bootstrap_components as dbc

# Crear la aplicación con tema Bootstrap
app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

# Definir el layout (estructura visual)
app.layout = dbc.Container([
    dbc.Row([
        dbc.Col([
            html.H1("Mi Primera App Dash"),
            html.P("Escribe algo:"),
            dcc.Input(id='input', type='text', value=''),
            html.Div(id='output')
        ])
    ])
])

# Crear callback para interactividad
@callback(
    Output('output', 'children'),
    Input('input', 'value')
)
def update_output(value):
    return f'Has escrito: {value}'

if __name__ == '__main__':
    app.run_server(debug=True)
```

---

## 1.6. Conceptos Fundamentales

### 1.6.1. Layout (Estructura Visual)

El **layout** define cómo se ve tu aplicación. Es como el HTML de tu página, pero escrito en Python.

```python
app.layout = html.Div([
    html.H1("Título"),
    html.P("Párrafo de texto"),
    html.Button("Botón")
])
```

### 1.6.2. Componentes

Dash tiene 3 tipos principales de componentes:

#### A) HTML Components (`html.*`)

Representan etiquetas HTML estándar:

```python
html.Div()      # <div>
html.H1()       # <h1>
html.P()        # <p>
html.Button()   # <button>
html.Img()      # <img>
html.A()        # <a>
```

#### B) Core Components (`dcc.*`)

Componentes interactivos específicos de Dash:

```python
dcc.Input()     # Campo de texto
dcc.Dropdown()  # Menú desplegable
dcc.Textarea()  # Área de texto multilínea
dcc.Graph()     # Gráfica interactiva
dcc.Markdown()  # Renderizar markdown
dcc.Store()     # Almacenamiento en el navegador
```

#### C) Bootstrap Components (`dbc.*`)

Componentes con estilos de Bootstrap:

```python
dbc.Container() # Contenedor responsive
dbc.Row()       # Fila del grid
dbc.Col()       # Columna del grid
dbc.Card()      # Tarjeta
dbc.Button()    # Botón estilizado
dbc.Navbar()    # Barra de navegación
```

### 1.6.3. Callbacks (Interactividad)

Los **callbacks** son funciones que se ejecutan cuando algo cambia en la interfaz. Conectan los componentes entre sí.

```python
@callback(
    Output('componente-destino', 'propiedad'),  # Qué actualizar
    Input('componente-origen', 'propiedad')     # Qué escuchar
)
def mi_funcion(valor_input):
    # Procesar el valor
    return nuevo_valor
```

**Tipos de dependencias:**

- **Output**: Define QUÉ componente y propiedad se actualizarán
- **Input**: Cuando cambia, DISPARA el callback
- **State**: Permite LEER un valor sin disparar el callback

**Ejemplo completo:**

```python
@callback(
    Output('resultado', 'children'),
    Input('boton', 'n_clicks'),
    State('nombre-input', 'value')
)
def mostrar_saludo(n_clicks, nombre):
    if n_clicks:
        return f'¡Hola {nombre}!'
    return ''
```

---

## 1.7. Sistema de Grid de Bootstrap

Dash usa Bootstrap para crear layouts responsivos con un sistema de 12 columnas:

```python
dbc.Container([
    dbc.Row([
        dbc.Col([
            html.H1("Columna 1")
        ], width=6),  # 50% del ancho (6 de 12)
        
        dbc.Col([
            html.H1("Columna 2")
        ], width=6)   # 50% del ancho (6 de 12)
    ])
])
```

### Anchos Responsivos:

```python
dbc.Col([
    html.Div("Contenido")
], 
    xs=12,  # 100% en móviles extra pequeños
    sm=12,  # 100% en móviles
    md=6,   # 50% en tablets
    lg=4,   # 33% en laptops
    xl=3    # 25% en pantallas grandes
)
```

---

## 1.8. Componentes Comunes para el Ejercicio

### 1.8.1. Inputs del Usuario

```python
# Campo de texto simple
dcc.Input(
    id='nombre-input',
    type='text',
    placeholder='Escribe tu nombre...',
    value='',
    style={'width': '100%'}
)

# Área de texto (multilínea)
dcc.Textarea(
    id='mensaje-textarea',
    placeholder='Escribe un mensaje...',
    style={'width': '100%', 'height': '100px'}
)

# Botón
dbc.Button(
    'Enviar',
    id='enviar-btn',
    color='primary',
    n_clicks=0
)
```

### 1.8.2. Contenedores y Layout

```python
# Card para agrupar contenido
dbc.Card([
    dbc.CardHeader("Título de la Card"),
    dbc.CardBody([
        html.H5("Subtítulo"),
        html.P("Contenido de la card")
    ])
])

# Navbar (barra de navegación)
dbc.Navbar(
    dbc.Container([
        dbc.NavbarBrand("Mi App", className="ms-2")
    ]),
    color="primary",
    dark=True
)
```

### 1.8.3. Mostrar Información

```python
# Div simple
html.Div(id='output', children='Texto aquí')

# Alert (mensajes destacados)
dbc.Alert(
    "Este es un mensaje importante",
    color="success",  # success, info, warning, danger
)

# Badge (etiquetas)
dbc.Badge(
    "Nuevo",
    color="primary",
    pill=True
)

# Loading spinner
dcc.Loading(
    id="loading",
    type="circle",
    children=[html.Div(id="loading-output")]
)
```

---

## 1.9. Conexión con APIs

Para conectar tu app Dash con una API (como la del agente de seguros):

```python
import requests

def llamar_api(mensaje):
    """Envía un mensaje a la API y retorna la respuesta"""
    try:
        response = requests.post(
            "http://localhost:8000/chat",
            json={
                "message": mensaje,
                "thread_id": "usuario_123"
            },
            timeout=30
        )
        response.raise_for_status()
        return response.json()
    except Exception as e:
        return {"error": str(e)}

# Usar en un callback
@callback(
    Output('respuesta', 'children'),
    Input('enviar-btn', 'n_clicks'),
    State('mensaje-input', 'value')
)
def enviar_mensaje(n_clicks, mensaje):
    if n_clicks > 0 and mensaje:
        resultado = llamar_api(mensaje)
        if 'error' in resultado:
            return f"Error: {resultado['error']}"
        return resultado.get('response', 'Sin respuesta')
    return ''
```

---

## 1.10. Manejo de Estado con dcc.Store

`dcc.Store` te permite guardar datos en el navegador del usuario:

```python
# En el layout
app.layout = html.Div([
    dcc.Store(id='historial-store', data=[]),
    html.Div(id='display')
])

# Guardar datos
@callback(
    Output('historial-store', 'data'),
    Input('agregar-btn', 'n_clicks'),
    State('historial-store', 'data')
)
def agregar_al_historial(n_clicks, historial_actual):
    if n_clicks:
        historial_actual.append({'mensaje': 'Nuevo mensaje'})
        return historial_actual
    return historial_actual

# Leer datos
@callback(
    Output('display', 'children'),
    Input('historial-store', 'data')
)
def mostrar_historial(historial):
    return f"Hay {len(historial)} mensajes"
```

**Tipos de almacenamiento:**
- `memory`: Se pierde al refrescar la página
- `session`: Persiste durante la sesión del navegador
- `local`: Persiste permanentemente en el navegador

---

## 1.11. Estilos y Personalización

### Tres formas de aplicar estilos:

#### 1. Estilos inline (diccionarios Python)

```python
html.Div(
    "Texto con estilo",
    style={
        'color': 'blue',
        'fontSize': '20px',  # Nota: camelCase
        'textAlign': 'center',
        'backgroundColor': '#f0f0f0',
        'padding': '10px',
        'borderRadius': '5px'
    }
)
```

#### 2. Clases CSS

```python
html.Div("Texto", className='mi-clase-css otra-clase')
```

#### 3. Temas Bootstrap

```python
# Al crear la app
app = Dash(__name__, external_stylesheets=[dbc.themes.FLATLY])
```

**Temas populares:**
- `BOOTSTRAP` - Clásico
- `FLATLY` - Moderno y limpio
- `DARKLY` - Modo oscuro
- `CYBORG` - Oscuro futurista
- `COSMO` - Limpio y profesional

---

## 1.12. Tips y Mejores Prácticas

### 1. Organiza tu código en funciones

```python
def crear_header():
    return dbc.Navbar([
        dbc.NavbarBrand("Mi App")
    ])

def crear_contenido():
    return dbc.Container([
        html.H1("Contenido")
    ])

app.layout = html.Div([
    crear_header(),
    crear_contenido()
])
```

### 2. Usa `prevent_initial_call`

```python
@callback(
    Output('output', 'children'),
    Input('button', 'n_clicks'),
    prevent_initial_call=True  # No ejecuta al cargar la página
)
def mi_callback(n_clicks):
    return f"Clicks: {n_clicks}"
```

### 3. Maneja errores gracefully

```python
from dash.exceptions import PreventUpdate

@callback(
    Output('output', 'children'),
    Input('input', 'value')
)
def procesar(value):
    if not value:
        raise PreventUpdate  # No actualiza si no hay valor
    return value
```

### 4. Usa el contexto para saber qué disparó el callback

```python
from dash import ctx

@callback(
    Output('output', 'children'),
    [Input('btn1', 'n_clicks'),
     Input('btn2', 'n_clicks')]
)
def multi_button(btn1, btn2):
    if ctx.triggered_id == 'btn1':
        return "Botón 1 presionado"
    elif ctx.triggered_id == 'btn2':
        return "Botón 2 presionado"
    return "Ningún botón presionado"
```

---

## 1.13. Debugging y Solución de Problemas

### Ver qué está pasando

```python
@callback(
    Output('output', 'children'),
    Input('input', 'value')
)
def mi_callback(value):
    print(f"DEBUG: valor recibido = {value}")  # Se imprime en la terminal
    return value
```

### Herramientas del Navegador (F12)

- **Console**: Ver errores de JavaScript
- **Network**: Ver llamadas HTTP
- **Elements**: Inspeccionar HTML generado

### Modo Debug

```python
if __name__ == '__main__':
    app.run_server(debug=True)  # Recarga automática al guardar
```

---

## 1.14. Recursos de Aprendizaje

### Documentación Oficial:
- **Dash**: https://dash.plotly.com/
- **Dash Bootstrap**: https://dash-bootstrap-components.opensource.faculty.ai/
- **Plotly**: https://plotly.com/python/

### Comunidad:
- **Forum**: https://community.plotly.com/
- **GitHub**: https://github.com/plotly/dash
- **Stack Overflow**: Etiqueta `plotly-dash`

### Tutoriales:
- Tutorial oficial de Dash
- Galería de ejemplos: https://dash.gallery/Portal/
- Cheatsheet: https://dashcheatsheet.pythonanywhere.com/

---

## 1.15. Resumen de Conceptos Clave

Antes de pasar al ejercicio, asegúrate de entender:

✅ **Layout**: Es la estructura visual de tu app (como HTML pero en Python)
✅ **Componentes**: html.*, dcc.*, dbc.* - bloques de construcción
✅ **Callbacks**: Funciones que conectan componentes y crean interactividad
✅ **Input/Output/State**: Diferentes tipos de dependencias en callbacks
✅ **dcc.Store**: Almacenamiento de datos en el navegador
✅ **Bootstrap Grid**: Sistema de filas y columnas para layouts responsivos

---

## ✅ ¿Listo para el Ejercicio?

Ahora que entiendes los conceptos básicos de Dash, estás listo para construir la aplicación de chat.

**Siguiente paso:** Lee `2_GUIA_EJERCICIO.md` para obtener instrucciones detalladas.

---

*Este documento es parte del Workshop de Herramientas Frontend con IA - Módulo Dash*

