# 02 - Inputs y Widgets

## 📖 ¿Qué aprenderás?

En esta lección aprenderás a capturar información del usuario usando diferentes tipos de inputs y widgets de Streamlit.

## 🎯 Temas cubiertos:

1. Campos de texto (input, text_area)
2. Botones y acciones
3. Selectores (selectbox, multiselect)
4. Sliders y controles numéricos
5. Formularios

## 📝 Aplicaciones de esta lección:

### `02-01_app_inputs.py`
Diferentes tipos de campos de texto para capturar información del usuario.

**Ejecutar:**
```bash
streamlit run 02-01_app_inputs.py
```

### `02-02_app_botones.py`
Cómo usar botones y formularios para crear interacciones.

**Ejecutar:**
```bash
streamlit run 02-02_app_botones.py
```

### `02-03_app_selectores.py`
Selectores, checkboxes, sliders y más widgets de selección.

**Ejecutar:**
```bash
streamlit run 02-03_app_selectores.py
```

## 💡 Conceptos Clave

### 1. Los widgets retornan valores
```python
nombre = st.text_input("Tu nombre")
# La variable 'nombre' contiene lo que el usuario escribió
```

### 2. La app se re-ejecuta con cada interacción
Cada vez que el usuario interactúa con un widget, todo el script se ejecuta de nuevo.

### 3. Los valores se actualizan en tiempo real
No necesitas un botón "enviar" para capturar valores (aunque puedes usarlo si quieres).

## 🎨 Widgets principales:

| Widget | Descripción |
|--------|-------------|
| `st.text_input()` | Entrada de texto de una línea |
| `st.text_area()` | Entrada de texto multilínea |
| `st.number_input()` | Entrada numérica |
| `st.button()` | Botón clickeable |
| `st.checkbox()` | Casilla de verificación |
| `st.radio()` | Selector de opción única |
| `st.selectbox()` | Lista desplegable |
| `st.multiselect()` | Selector múltiple |
| `st.slider()` | Control deslizante |
| `st.date_input()` | Selector de fecha |
| `st.time_input()` | Selector de hora |

## 🏋️ Ejercicio Práctico

Crea una aplicación que:

1. Pida nombre y apellido del usuario
2. Pida su edad con un slider
3. Pida que seleccione sus hobbies (multiselect)
4. Al presionar un botón, muestre un resumen de todo

## ⚠️ Nota Importante

Los valores de los widgets se pierden cada vez que la app se recarga. En la siguiente lección aprenderás sobre **Session State** para mantener valores persistentes.

## ➡️ Siguiente Paso

Continúa con [03_layout_y_containers](../03_layout_y_containers/)
