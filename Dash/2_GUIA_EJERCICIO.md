# 2. Guía del Ejercicio - Chat con el Agente de Seguros

## 🎯 Objetivo

Construir una **interfaz de chat profesional** que se conecte con la API del agente de seguros Seguros Bolívar.

---

## 📋 Descripción del Ejercicio

Crearás una aplicación web interactiva que permita a los usuarios:
- ✅ Enviar mensajes al agente de seguros
- ✅ Ver el historial de la conversación
- ✅ Verificar el estado de conexión con la API
- ✅ Tener una interfaz profesional y agradable

---

## 🏗️ Arquitectura de la Aplicación

```
┌─────────────────────────────────────┐
│  🛡️ Seguros Bolívar  [●Conectado]  │
│  Protegiendo lo que más valoras      │
├─────────────────────────────────────┤
│                                      │
│  Área de Mensajes                    │
│  ┌────────────────────────────────┐ │
│  │ Usuario: Hola                  │ │
│  │ Agente: ¡Hola! ¿En qué puedo..│ │
│  │ Usuario: ¿Qué seguros ofrecen?│ │
│  │ Agente: Ofrecemos 5 tipos...  │ │
│  └────────────────────────────────┘ │
│                                      │
├─────────────────────────────────────┤
│  Input de Mensaje                    │
│  ┌────────────────────────────────┐ │
│  │ Escribe tu pregunta...         │ │
│  └────────────────────────────────┘ │
│  [    Botón Enviar    ]              │
└─────────────────────────────────────┘

Colores: Verde #00A651, Amarillo #FFD100, Blanco
```

---

## 🛠️ Paso 1: Configuración Inicial

**⚠️ IMPORTANTE**: En este paso configurarás **DOS entornos virtuales separados** porque la API y Dash tienen diferentes dependencias.

### 1.1. Configurar Entorno Virtual de la API

**En la Terminal 1:**

```bash
# Navegar a la carpeta de la API (desde la raíz del proyecto)
cd insurance_agent_api

# Crear entorno virtual para la API
python -m venv venv

# Activar el entorno virtual
# En Windows (PowerShell):
venv\Scripts\Activate.ps1

# En Windows (CMD):
venv\Scripts\activate.bat

# En macOS/Linux:
source venv/bin/activate

# Instalar dependencias de la API
pip install -r requirements.txt
```

**Verificación**: Deberías ver `(venv)` al inicio de tu prompt.

### 1.2. Configurar Entorno Virtual de Dash

**Abre una segunda terminal (Terminal 2):**

```bash
# Navegar a la carpeta Dash (desde la raíz del proyecto)
cd Dash

# Crear entorno virtual para Dash
python -m venv venv

# Activar el entorno virtual
# En Windows (PowerShell):
venv\Scripts\Activate.ps1

# En Windows (CMD):
venv\Scripts\activate.bat

# En macOS/Linux:
source venv/bin/activate

# Instalar dependencias de Dash
pip install -r requirements.txt
```

**Verificación**: Deberías ver `(venv)` al inicio de tu prompt.

**Nota**: Deberás activar el entorno virtual correspondiente cada vez que abras una nueva terminal.

### 1.3. Iniciar la API del Agente

**En la Terminal 1 (con venv de la API activado):**

```bash
# Navegar a la carpeta app
cd app

# Iniciar la API
python main.py
```

Deberías ver:
```
✅ Agente de seguros inicializado correctamente
INFO:     Uvicorn running on http://0.0.0.0:8000
```

**Esta terminal debe permanecer abierta** con la API corriendo durante todo el workshop.

### 1.4. Verificar Conexión con la API

**En la Terminal 2 (con venv de Dash activado):**

```bash
# Asegúrate de estar en la carpeta Dash
# Si no estás ahí, navega:
# cd Dash

# Verificar conexión
python test_api.py
```

Deberías ver:
```
🎉 ¡Todas las pruebas pasaron exitosamente!
```

✅ **Checkpoint 1**: Si ves este mensaje, puedes continuar.

**Resumen de terminales:**
- **Terminal 1**: API corriendo (venv de API) - NO CERRAR
- **Terminal 2**: Trabajarás aquí (venv de Dash)

---

## 📝 Paso 2: Implementar Funciones de API

Abre el archivo `3_PLANTILLA_EJERCICIO.py` y completa estas tres funciones:

### 2.1. Función: `verificar_api()`

**Propósito**: Verificar si la API está disponible

**Código a implementar:**

```python
def verificar_api():
    """Verifica si la API está disponible."""
    try:
        response = requests.get(f"{API_URL}/health", timeout=3)
        return response.status_code == 200
    except:
        return False
```

**Explicación:**
- Hace un GET request al endpoint `/health`
- Si responde con código 200, la API está funcionando
- Si hay algún error (timeout, conexión), retorna `False`

### 2.2. Función: `enviar_mensaje_api(mensaje, thread_id)`

**Propósito**: Enviar un mensaje al agente y recibir respuesta

**Código a implementar:**

```python
def enviar_mensaje_api(mensaje, thread_id):
    """Envía un mensaje al agente de seguros."""
    try:
        response = requests.post(
            f"{API_URL}/chat",
            json={"message": mensaje, "thread_id": thread_id},
            timeout=30
        )
        response.raise_for_status()
        return response.json()
    except requests.exceptions.Timeout:
        return {"error": "La solicitud tomó demasiado tiempo. Intenta nuevamente."}
    except requests.exceptions.ConnectionError:
        return {"error": "No se pudo conectar con la API. Verifica que esté corriendo."}
    except Exception as e:
        return {"error": f"Error: {str(e)}"}
```

**Explicación:**
- Hace un POST request al endpoint `/chat`
- Envía el mensaje y el thread_id en formato JSON
- Timeout de 30 segundos (las respuestas de IA pueden tardar)
- Maneja diferentes tipos de errores con mensajes claros

### 2.3. Función: `obtener_historial_api(thread_id)`

**Propósito**: Obtener el historial de conversación

**Código a implementar:**

```python
def obtener_historial_api(thread_id):
    """Obtiene el historial de conversación."""
    try:
        response = requests.get(f"{API_URL}/history/{thread_id}", timeout=5)
        response.raise_for_status()
        data = response.json()
        return data.get("history", [])
    except:
        return []
```

**Explicación:**
- Hace un GET request al endpoint `/history/{thread_id}`
- Retorna la lista de mensajes del historial
- Si hay error, retorna lista vacía

✅ **Checkpoint 2**: Prueba ejecutando el archivo. Debe decir "✅ API conectada correctamente"

---

## 🎨 Paso 3: Crear el Layout

### 3.1. Función: `crear_header()`

**Propósito**: Crear la barra superior con logo y estado de API

**Código a implementar:**

```python
def crear_header():
    """Crea el header de la aplicación."""
    return dbc.Navbar(
        dbc.Container([
            dbc.Row([
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
```

**Componentes clave:**
- `dbc.Navbar`: Barra de navegación con colores corporativos de Seguros Bolívar (Verde #00A651)
- `dbc.NavbarBrand`: Logo/nombre de la empresa
- `dbc.Badge` con `id="estado-api"`: Indicador de estado (se actualizará con callback)
- Los estilos personalizados en `assets/custom.css` aplicarán el borde amarillo y otros detalles

### 3.2. Función: `crear_area_mensajes()`

**Propósito**: Crear el área donde se mostrarán los mensajes del chat

**Código a implementar:**

```python
def crear_area_mensajes():
    """Crea el área donde se mostrarán los mensajes del chat."""
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
```

**Componentes clave:**
- `dbc.Card`: Contenedor visual
- `dcc.Loading`: Spinner de carga
- `html.Div` con `id='chat-display'`: Aquí se renderizarán los mensajes
- `height: 450px` y `overflowY: auto`: Scroll cuando hay muchos mensajes

### 3.3. Función: `crear_area_input()`

**Propósito**: Crear el área de input y botón de enviar

**Código a implementar:**

```python
def crear_area_input():
    """Crea el área de input para enviar mensajes."""
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
```

**Componentes clave:**
- `dcc.Textarea` con `id='mensaje-input'`: Campo para escribir mensajes
- `dbc.Button` con `id='enviar-btn'`: Botón de enviar
- `n_clicks=0`: Contador de clicks (se usa en el callback)

### 3.4. Ensamblar el Layout Principal

**En el código principal:**

```python
app.layout = dbc.Container([
    # Header
    crear_header(),
    
    # Contenido principal
    dbc.Row([
        dbc.Col([
            # Área de mensajes
            crear_area_mensajes(),
            
            # Área de input
            crear_area_input(),
            
            # Info del sistema
            html.Div([
                html.Small([
                    html.I(className="bi bi-info-circle me-2"),
                    f"Thread ID: {THREAD_ID}"
                ], className="text-muted")
            ], className="mt-3 text-center")
        ], lg=8, md=10, sm=12, className="mx-auto")
    ]),
    
    # Stores para mantener estado
    dcc.Store(id='historial-store', data=[]),
    
    # Interval para verificar estado de API
    dcc.Interval(
        id='api-check-interval',
        interval=5000,  # cada 5 segundos
        n_intervals=0
    )
], fluid=True, className="py-4")
```

**Componentes clave:**
- `dcc.Store` con `id='historial-store'`: Almacena el historial de mensajes
- `dcc.Interval`: Timer que dispara callbacks periódicamente
- `lg=8, md=10, sm=12`: Responsive (8 columnas en pantallas grandes, 10 en medianas, 12 en pequeñas)

✅ **Checkpoint 3**: Ejecuta la aplicación. Deberías ver el layout completo.

---

## 🔄 Paso 4: Implementar Callbacks

### 4.1. Callback: Verificar Estado de API

**Propósito**: Actualizar el indicador de estado cada 5 segundos

**Código a implementar:**

```python
@callback(
    [Output('estado-api', 'children'),
     Output('estado-api', 'color')],
    Input('api-check-interval', 'n_intervals')
)
def actualizar_estado_api(n):
    """Verifica el estado de la API periódicamente."""
    if verificar_api():
        return [html.I(className="bi bi-circle-fill me-2"), "Conectado"], "success"
    else:
        return [html.I(className="bi bi-circle-fill me-2"), "Desconectado"], "danger"
```

**Explicación:**
- Se ejecuta cada 5 segundos (disparado por `api-check-interval`)
- Llama a `verificar_api()`
- Actualiza el texto y color del badge

### 4.2. Callback: Enviar Mensaje

**Propósito**: Procesar el envío de mensajes cuando se presiona el botón

**Código a implementar:**

```python
@callback(
    [Output('historial-store', 'data'),
     Output('mensaje-input', 'value')],
    Input('enviar-btn', 'n_clicks'),
    [State('mensaje-input', 'value'),
     State('historial-store', 'data')],
    prevent_initial_call=True
)
def procesar_mensaje(n_clicks, mensaje, historial_actual):
    """Procesa el envío de mensajes."""
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
    
    # Enviar mensaje a la API
    respuesta = enviar_mensaje_api(mensaje.strip(), THREAD_ID)
    
    # Agregar respuesta al historial
    if "error" in respuesta:
        historial_nuevo.append({
            "type": "error",
            "content": respuesta["error"],
            "timestamp": datetime.now().strftime("%H:%M:%S")
        })
    else:
        historial_nuevo.append({
            "type": "ai",
            "content": respuesta.get("response", "Sin respuesta"),
            "timestamp": datetime.now().strftime("%H:%M:%S")
        })
    
    # Retornar historial actualizado y limpiar el input
    return historial_nuevo, ''
```

**Explicación:**
- **Input**: `enviar-btn.n_clicks` - Se ejecuta cuando se presiona el botón
- **State**: Lee `mensaje-input.value` y `historial-store.data` sin disparar callbacks
- **Output**: Actualiza el historial y limpia el campo de texto
- **prevent_initial_call=True**: No se ejecuta al cargar la página

**Estructura de datos del historial:**
```python
[
    {"type": "human", "content": "Hola", "timestamp": "14:30:45"},
    {"type": "ai", "content": "¡Hola! ¿En qué puedo ayudarte?", "timestamp": "14:30:47"},
    {"type": "error", "content": "Error de conexión", "timestamp": "14:31:00"}
]
```

### 4.3. Callback: Renderizar Mensajes

**Propósito**: Convertir el historial en componentes visuales

**Código a implementar:**

```python
@callback(
    Output('chat-display', 'children'),
    Input('historial-store', 'data')
)
def actualizar_chat_display(historial):
    """Renderiza los mensajes del historial en la interfaz."""
    if not historial:
        return html.Div([
            html.Div([
                html.I(className="bi bi-chat-text", 
                       style={"fontSize": "48px", "color": "#ccc"}),
                html.P(
                    "¡Bienvenido a SegurosVida+!",
                    className="mt-3",
                    style={"fontSize": "18px", "color": "#666"}
                ),
                html.P(
                    "Escribe tu pregunta para comenzar.",
                    style={"color": "#999"}
                )
            ], className="text-center", style={"marginTop": "100px"})
        ])
    
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
```

**Explicación:**
- Se ejecuta cada vez que cambia `historial-store`
- Si no hay mensajes, muestra mensaje de bienvenida
- Crea un componente visual diferente según el tipo de mensaje:
  - `human`: Alert azul alineado a la derecha
  - `ai`: Alert gris alineado a la izquierda con Markdown
  - `error`: Alert rojo centrado

✅ **Checkpoint 4**: Tu aplicación debería estar completamente funcional ahora.

---

## 🧪 Paso 5: Probar la Aplicación

### 5.1. Ejecutar la Aplicación

```bash
python 3_PLANTILLA_EJERCICIO.py
```

Abre en tu navegador: http://localhost:8050

### 5.2. Preguntas de Prueba

Prueba tu aplicación con estas preguntas:

1. **"¿Qué tipos de seguros ofrecen?"**
   - Debe responder con los 5 tipos de seguros

2. **"¿Cuánto cuesta el seguro de auto?"**
   - Debe dar información sobre precios

3. **"¿El seguro de auto incluye asistencia en carretera?"**
   - Debe responder sobre coberturas específicas

4. **"Quiero un seguro para mi casa, ¿qué me recomiendan?"**
   - Debe dar recomendaciones personalizadas

### 5.3. Verificar Funcionalidades

- [ ] Los mensajes se envían al presionar el botón
- [ ] Las respuestas del agente aparecen correctamente
- [ ] El historial se mantiene durante la sesión
- [ ] El indicador de estado muestra "Conectado" en verde
- [ ] Los mensajes de error se muestran si la API falla
- [ ] Los mensajes del usuario están a la derecha
- [ ] Los mensajes del agente están a la izquierda
- [ ] Los timestamps se muestran correctamente

---

## 🌟 Paso 6: Funcionalidades Bonus (Opcional)

Si terminas antes y quieres mejorar tu aplicación, intenta agregar:

### 6.1. Botones de Preguntas de Ejemplo

**Agregar antes del área de input:**

```python
def crear_botones_ejemplo():
    """Crea botones con preguntas de ejemplo."""
    preguntas = [
        "¿Qué tipos de seguros ofrecen?",
        "¿Cuánto cuesta el seguro de auto?",
        "¿Tienen cobertura internacional?",
        "¿Cómo hago una reclamación?"
    ]
    
    return dbc.Card([
        dbc.CardHeader([
            html.I(className="bi bi-lightbulb me-2"),
            "Preguntas sugeridas"
        ]),
        dbc.CardBody([
            dbc.Row([
                dbc.Col([
                    dbc.Button(
                        pregunta,
                        id={"type": "ejemplo-btn", "index": i},
                        color="light",
                        outline=True,
                        size="sm",
                        className="mb-2 w-100"
                    )
                ], width=6)
                for i, pregunta in enumerate(preguntas)
            ])
        ])
    ], className="mb-3")
```

**Modificar el callback de envío:**

```python
@callback(
    [Output('historial-store', 'data'),
     Output('mensaje-input', 'value')],
    [Input('enviar-btn', 'n_clicks'),
     Input({'type': 'ejemplo-btn', 'index': dbc.ALL}, 'n_clicks')],
    [State('mensaje-input', 'value'),
     State('historial-store', 'data')],
    prevent_initial_call=True
)
def procesar_mensaje(n_clicks, n_clicks_ejemplos, mensaje, historial_actual):
    # Determinar qué disparó el callback
    triggered_id = ctx.triggered_id
    
    # Si fue un botón de ejemplo, usar el texto del botón
    if isinstance(triggered_id, dict) and triggered_id.get('type') == 'ejemplo-btn':
        button_index = triggered_id.get('index')
        preguntas = [
            "¿Qué tipos de seguros ofrecen?",
            "¿Cuánto cuesta el seguro de auto?",
            "¿Tienen cobertura internacional?",
            "¿Cómo hago una reclamación?"
        ]
        mensaje = preguntas[button_index]
    
    # ... resto del código igual
```

### 6.2. Cambiar a Input para Enviar con Enter

**⚠️ Nota**: `dcc.Textarea` no soporta enviar con Enter (`n_submit`). Si quieres esta funcionalidad, debes cambiar a `dcc.Input`:

```python
# En lugar de Textarea, usar Input:
dcc.Input(
    id='mensaje-input',
    type='text',
    placeholder='Escribe tu pregunta sobre seguros aquí...',
    style={'width': '100%'}
)

# Luego modificar el callback:
@callback(
    [Output('historial-store', 'data'),
     Output('mensaje-input', 'value')],
    [Input('enviar-btn', 'n_clicks'),
     Input('mensaje-input', 'n_submit')],  # Solo funciona con dcc.Input
    [State('mensaje-input', 'value'),
     State('historial-store', 'data')],
    prevent_initial_call=True
)
def procesar_mensaje(n_clicks, n_submit, mensaje, historial_actual):
    # ... resto del código
    pass
```

**Trade-off**: `dcc.Input` solo permite una línea, mientras que `dcc.Textarea` permite múltiples líneas.

### 6.3. Auto-scroll al Último Mensaje

**Agregar al final de la función `actualizar_chat_display`:**

```python
# Agregar un div invisible al final para auto-scroll
mensajes.append(html.Div(id="scroll-anchor"))
return mensajes
```

**Nota**: El archivo `assets/custom.css` ya incluye CSS que hace scroll automático suavemente.

### 6.4. Contador de Caracteres

**Agregar debajo del textarea:**

```python
html.Small(id='char-count', children='0 caracteres', className='text-muted')

# Callback para actualizar contador
@callback(
    Output('char-count', 'children'),
    Input('mensaje-input', 'value')
)
def actualizar_contador(mensaje):
    if not mensaje:
        return '0 caracteres'
    return f'{len(mensaje)} caracteres'
```

### 6.5. Botón para Limpiar Historial

**Agregar en el layout:**

```python
dbc.Button(
    "Limpiar Historial",
    id='limpiar-btn',
    color='danger',
    outline=True,
    size='sm'
)

# Callback para limpiar
@callback(
    Output('historial-store', 'data', allow_duplicate=True),
    Input('limpiar-btn', 'n_clicks'),
    prevent_initial_call=True
)
def limpiar_historial(n_clicks):
    return []
```

---

## ✅ Lista de Verificación Final

Antes de dar por terminado el ejercicio, verifica que:

### Funcionalidades Básicas:
- [ ] La aplicación se conecta correctamente a la API
- [ ] Los mensajes se envían y reciben correctamente
- [ ] El historial se muestra de forma clara
- [ ] La UI es intuitiva y profesional
- [ ] Los errores se manejan apropiadamente
- [ ] La aplicación es responsive
- [ ] El código está bien organizado y comentado

### Funcionalidades Bonus (Opcional):
- [ ] Botones de preguntas de ejemplo
- [ ] Enviar mensaje con Enter (requiere cambiar a `dcc.Input`)
- [ ] Timestamps en mensajes (✅ ya en solución)
- [ ] Loading spinner (✅ ya en solución)
- [ ] Auto-scroll
- [ ] Markdown en respuestas (✅ ya en solución)
- [ ] Estilos personalizados (✅ ya en solución)
- [ ] Contador de caracteres
- [ ] Botón limpiar historial

---

## 🆘 Solución de Problemas Comunes

### Problema 1: "No se puede conectar con la API"

**Solución:**
```bash
# Verificar que la API esté corriendo
python test_api.py

# Si falla, revisar:
# 1. ¿Está la API corriendo en otra terminal?
# 2. ¿Está en el puerto 8000?
# 3. ¿Tienes el archivo .env configurado?
```

### Problema 2: "El callback no se ejecuta"

**Solución:**
- Verifica que los IDs coincidan exactamente
- Usa `print()` para debugear
- Revisa la consola de Python para errores
- Asegúrate de usar `prevent_initial_call=True` cuando corresponda

### Problema 3: "Los mensajes no se muestran"

**Solución:**
- Revisa la estructura de datos en `historial-store`
- Usa las DevTools del navegador (F12) > Console
- Verifica que el callback de renderizado se esté ejecutando
- Imprime el historial en el callback: `print(historial)`

### Problema 4: "Error de imports"

**Solución:**
```bash
# Reinstalar dependencias
pip install -r requirements.txt
```

---

## 📚 Recursos de Ayuda

### Durante el Desarrollo:

1. **`5_REFERENCIA_CODIGO.py`**: Ejemplos de código para cada componente
2. **`1_INTRODUCCION_DASH.md`**: Conceptos fundamentales
3. **`4_SOLUCION_COMPLETA.py`**: Solución completa (último recurso)

### Documentación Externa:

- **Dash**: https://dash.plotly.com/
- **Bootstrap Components**: https://dash-bootstrap-components.opensource.faculty.ai/
- **Requests**: https://requests.readthedocs.io/

---

## ✨ ¡Felicitaciones!

Si llegaste hasta aquí y tu aplicación funciona, ¡has completado exitosamente el ejercicio de Dash!

**Siguiente paso:** Compara tu implementación con `4_SOLUCION_COMPLETA.py` para ver otras formas de resolver el problema.

---

*Esta guía es parte del Workshop de Herramientas Frontend con IA - Módulo Dash*

