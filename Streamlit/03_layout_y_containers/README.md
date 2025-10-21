# 03 - Layout y Containers

## 📖 ¿Qué aprenderás?

En esta lección aprenderás a organizar el contenido de tu aplicación usando columnas, contenedores y el sidebar.

## 🎯 Temas cubiertos:

1. Columnas para layouts horizontales
2. Sidebar para navegación
3. Tabs para organizar contenido
4. Expanders para contenido colapsable
5. Containers y organización avanzada

## 📝 Aplicaciones de esta lección:

### `03-01_app_columnas.py`
Cómo crear layouts con columnas y distribuir contenido horizontalmente.

**Ejecutar:**
```bash
streamlit run 03-01_app_columnas.py
```

### `03-02_app_sidebar.py`
Usar el sidebar para navegación y controles.

**Ejecutar:**
```bash
streamlit run 03-02_app_sidebar.py
```

### `03-03_app_tabs.py`
Organizar contenido en pestañas (tabs).

**Ejecutar:**
```bash
streamlit run 03-03_app_tabs.py
```

## 💡 Conceptos Clave

### 1. Columnas
Permite distribuir contenido horizontalmente:
```python
col1, col2 = st.columns(2)
with col1:
    st.write("Columna 1")
with col2:
    st.write("Columna 2")
```

### 2. Sidebar
Barra lateral perfecta para navegación y controles:
```python
st.sidebar.title("Menú")
opcion = st.sidebar.selectbox("Elige", ["A", "B"])
```

### 3. Tabs
Organiza contenido en pestañas:
```python
tab1, tab2 = st.tabs(["Pestaña 1", "Pestaña 2"])
with tab1:
    st.write("Contenido 1")
```

## 🎨 Elementos de Layout:

| Elemento | Descripción |
|----------|-------------|
| `st.columns()` | Divide el espacio en columnas |
| `st.sidebar` | Barra lateral colapsable |
| `st.tabs()` | Pestañas para organizar contenido |
| `st.expander()` | Sección colapsable |
| `st.container()` | Contenedor para agrupar elementos |
| `st.empty()` | Placeholder que puedes actualizar |

## 🏋️ Ejercicio Práctico

Crea una app que:

1. Tenga un sidebar con opciones de filtro
2. Muestre el contenido principal en 3 columnas
3. Use tabs para diferentes secciones
4. Incluya expanders con información adicional

## 💡 Cuándo usar cada uno

- **Columns**: Cuando necesitas mostrar info lado a lado
- **Sidebar**: Para controles, filtros o navegación
- **Tabs**: Para separar secciones grandes de contenido
- **Expanders**: Para info opcional que no quieres mostrar siempre

## ➡️ Siguiente Paso

Continúa con [04_estado_y_sesion](../04_estado_y_sesion/)
