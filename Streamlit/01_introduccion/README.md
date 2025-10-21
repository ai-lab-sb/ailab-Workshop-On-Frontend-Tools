# 01 - Introducción a Streamlit

## 📖 ¿Qué es Streamlit?

Streamlit es un framework de Python de código abierto que permite crear aplicaciones web de forma rápida y sencilla, sin necesidad de conocimientos de frontend.

### ✨ Características principales:

- **Puro Python**: No necesitas HTML, CSS o JavaScript
- **Hot reload**: Los cambios se reflejan automáticamente
- **Componentes listos**: Inputs, gráficos, tablas, etc.
- **Fácil de aprender**: Curva de aprendizaje muy suave
- **Deployment gratuito**: Streamlit Cloud

## 🎯 En esta lección aprenderás:

1. Cómo crear tu primera aplicación
2. Mostrar texto de diferentes formas
3. Usar markdown y emojis
4. Elementos básicos de Streamlit

## 📝 Aplicaciones de esta lección:

### `01-01_app_hello_world.py`
Tu primera aplicación de Streamlit. Simplemente muestra "Hola Mundo".

**Ejecutar:**
```bash
streamlit run 01-01_app_hello_world.py
```

### `01-02_app_basicos.py`
Elementos básicos de texto en Streamlit: títulos, encabezados, texto, markdown, código, etc.

**Ejecutar:**
```bash
streamlit run 01-02_app_basicos.py
```

## 💡 Conceptos Clave

### 1. Todo es reactivo
Cuando cambias el código y guardas, Streamlit recarga automáticamente la app.

### 2. Ejecución de arriba hacia abajo
Streamlit ejecuta tu script de arriba hacia abajo cada vez que algo cambia.

### 3. Sintaxis simple
```python
import streamlit as st

st.write("Hola Mundo")  # ¡Así de simple!
```

## 🎨 Elementos básicos de texto:

| Función | Descripción |
|---------|-------------|
| `st.title()` | Título principal (más grande) |
| `st.header()` | Encabezado |
| `st.subheader()` | Subencabezado |
| `st.text()` | Texto simple |
| `st.write()` | Texto versátil (acepta casi todo) |
| `st.markdown()` | Texto con formato Markdown |
| `st.code()` | Bloque de código |

## 🏋️ Ejercicio Práctico

Modifica `01-02_app_basicos.py` para:

1. Cambiar el título principal
2. Agregar una nueva sección con tu información
3. Usar emojis diferentes
4. Agregar un bloque de código en tu lenguaje favorito

## ➡️ Siguiente Paso

Una vez que te sientas cómodo con estos conceptos, continúa con [02_inputs_y_widgets](../02_inputs_y_widgets/)
