# 🚀 Curso de Streamlit - Workshop Frontend con IA

Bienvenido al curso de **Streamlit**, una de las herramientas más populares para crear aplicaciones web con Python de forma rápida y sencilla.

## 📋 ¿Qué es Streamlit?

Streamlit es un framework de Python que permite crear aplicaciones web interactivas sin necesidad de conocer HTML, CSS o JavaScript. Es ideal para:

- 📊 Dashboards de datos
- 🤖 Interfaces para modelos de IA
- 💬 Aplicaciones de chat conversacional
- 📈 Visualizaciones interactivas

## 🎯 Objetivo del Curso

Al finalizar este curso, habrás creado una **aplicación de chat conversacional completa** que consume el API del agente de seguros de SegurosVida+.

## 📚 Estructura del Curso

### **Nivel 1: Fundamentos**

#### [01 - Introducción](./01_introduccion/)
- ¿Qué es Streamlit?
- Instalación y configuración
- Tu primera aplicación
- Elementos básicos de texto

#### [02 - Inputs y Widgets](./02_inputs_y_widgets/)
- Campos de texto y áreas
- Botones y formularios
- Selectores y sliders
- Interacción con el usuario

### **Nivel 2: Organización**

#### [03 - Layout y Containers](./03_layout_y_containers/)
- Columnas y grids
- Sidebar para navegación
- Tabs y expanders
- Organizar contenido complejo

### **Nivel 3: Interactividad**

#### [04 - Estado y Sesión](./04_estado_y_sesion/)
- Session State (concepto clave)
- Mantener datos entre ejecuciones
- Variables persistentes
- Gestión de estado complejo

### **Nivel 4: Integración**

#### [05 - Consumiendo APIs](./05_consumiendo_apis/)
- Hacer requests HTTP
- GET y POST con requests
- Procesar respuestas JSON
- Manejo de errores

### **Nivel 5: Proyecto Final**

#### [06 - Proyecto Final: Chat de Seguros](./06_proyecto_final/)
- Paso 1: Chat básico sin API
- Paso 2: Integración con API
- Paso 3: Gestión de historial
- Paso 4: Aplicación completa y pulida

## ⚙️ Instalación

### 1. Crear entorno virtual (recomendado)

```bash
# Crear entorno virtual
python -m venv venv

# Activar en Windows
venv\Scripts\activate

# Activar en Mac/Linux
source venv/bin/activate
```

### 2. Instalar dependencias

```bash
pip install -r requirements.txt
```

## ▶️ Cómo Ejecutar las Aplicaciones

Cada carpeta contiene aplicaciones `.py` que puedes ejecutar con:

```bash
streamlit run nombre_del_archivo.py
```

Por ejemplo:
```bash
cd 01_introduccion
streamlit run app_hello_world.py
```

La aplicación se abrirá automáticamente en tu navegador en `http://localhost:8501`

## 🎓 Metodología de Aprendizaje

1. **Lee el README** de cada carpeta
2. **Ejecuta las aplicaciones** de ejemplo
3. **Revisa el código** comentado
4. **Experimenta** modificando el código
5. **Practica** con los ejercicios sugeridos

## 📝 Requisitos Previos

- Python 3.10 o superior
- Conocimientos básicos de Python
- El agente de seguros (`insurance_agent_api`) corriendo en `http://localhost:8000`

## 🚀 Inicio Rápido

Si quieres ver el resultado final directamente:

```bash
cd 06_proyecto_final
streamlit run paso_4_completo.py
```

Asegúrate de tener el API del agente corriendo antes.

## 💡 Consejos para el Workshop

- 🔄 Streamlit recarga automáticamente al guardar cambios
- 🐛 Usa el botón "Always rerun" para desarrollo
- 📱 Las apps son responsive por defecto
- 🎨 Usa emojis para mejorar la UI
- 💾 Session state es tu mejor amigo para chat

## 📖 Recursos Adicionales

- [Documentación oficial de Streamlit](https://docs.streamlit.io/)
- [Galería de apps de Streamlit](https://streamlit.io/gallery)
- [Cheat Sheet de Streamlit](https://cheat-sheet.streamlit.app/)

## 🤝 Soporte

Este curso es parte del workshop de AI Lab - Seguros Bolívar sobre herramientas de frontend con IA.

---

**¡Empecemos! 🎉 Dirígete a [01_introduccion](./01_introduccion/) para comenzar.**
