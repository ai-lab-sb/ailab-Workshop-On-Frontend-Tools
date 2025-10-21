"""
Campos de texto e inputs básicos en Streamlit
"""

import streamlit as st

st.title("📝 Inputs de Texto en Streamlit")

# ========================================
# TEXT INPUT - UNA LÍNEA
# ========================================

st.header("1. Text Input (una línea)")

nombre = st.text_input("¿Cuál es tu nombre?")

if nombre:
    st.write(f"¡Hola, {nombre}! 👋")

# Input con valor por defecto
email = st.text_input("Email", value="ejemplo@correo.com")
st.write(f"Tu email: {email}")

# Input con placeholder
usuario = st.text_input("Usuario", placeholder="Escribe tu usuario aquí...")

# Input de password
password = st.text_input("Contraseña", type="password")
if password:
    st.write(f"Tu contraseña tiene {len(password)} caracteres (no te preocupes, no la mostramos 🔒)")

# ========================================
# TEXT AREA - MÚLTIPLES LÍNEAS
# ========================================

st.divider()
st.header("2. Text Area (múltiples líneas)")

mensaje = st.text_area(
    "Escribe un mensaje largo",
    placeholder="Puedes escribir varias líneas aquí...",
    height=150
)

if mensaje:
    palabras = len(mensaje.split())
    caracteres = len(mensaje)
    st.write(f"📊 Tu mensaje tiene {palabras} palabras y {caracteres} caracteres")

# ========================================
# NUMBER INPUT
# ========================================

st.divider()
st.header("3. Number Input")

edad = st.number_input(
    "¿Cuántos años tienes?",
    min_value=0,
    max_value=120,
    value=25,
    step=1
)
st.write(f"Tienes {edad} años")

precio = st.number_input(
    "Precio del producto",
    min_value=0.0,
    value=100.0,
    step=0.01,
    format="%.2f"
)
st.write(f"Precio: ${precio:,.2f}")

# ========================================
# DATE Y TIME INPUT
# ========================================

st.divider()
st.header("4. Fecha y Hora")

from datetime import datetime, date, time

fecha = st.date_input("Selecciona una fecha", value=date.today())
st.write(f"Fecha seleccionada: {fecha}")

hora = st.time_input("Selecciona una hora", value=time(9, 0))
st.write(f"Hora seleccionada: {hora}")

# ========================================
# COLOR PICKER
# ========================================

st.divider()
st.header("5. Color Picker")

color = st.color_picker("Elige tu color favorito", "#00FF00")
st.write(f"Color seleccionado: {color}")

# Mostrar un cuadro con el color
st.markdown(
    f'<div style="width:100px; height:100px; background-color:{color}; border-radius:10px;"></div>',
    unsafe_allow_html=True
)

# ========================================
# RESUMEN
# ========================================

st.divider()
st.header("📋 Resumen de tus datos")

if nombre:
    st.json({
        "nombre": nombre,
        "email": email,
        "usuario": usuario,
        "edad": edad,
        "precio": precio,
        "fecha": str(fecha),
        "hora": str(hora),
        "color_favorito": color
    })
