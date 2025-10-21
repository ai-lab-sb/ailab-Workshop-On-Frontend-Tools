"""
Selectores y sliders en Streamlit
"""

import streamlit as st

st.title("🎚️ Selectores y Sliders")

# ========================================
# SELECTBOX - DROPDOWN
# ========================================

st.header("1. Selectbox (Lista desplegable)")

ciudad = st.selectbox(
    "¿En qué ciudad vives?",
    ["Bogotá", "Medellín", "Cali", "Barranquilla", "Cartagena", "Otra"]
)

st.write(f"Vives en: **{ciudad}**")

# Con índice por defecto
tipo_seguro = st.selectbox(
    "Tipo de seguro",
    ["Vida", "Auto", "Hogar", "Salud", "Viaje"],
    index=1  # Auto será la opción por defecto
)

# ========================================
# MULTISELECT - SELECCIÓN MÚLTIPLE
# ========================================

st.divider()
st.header("2. Multiselect (Selección múltiple)")

hobbies = st.multiselect(
    "¿Cuáles son tus hobbies?",
    ["Deportes", "Lectura", "Música", "Viajes", "Cocina", "Gaming", "Arte"],
    default=["Lectura", "Viajes"]  # Opciones pre-seleccionadas
)

if hobbies:
    st.write(f"Has seleccionado {len(hobbies)} hobbies:")
    for hobby in hobbies:
        st.write(f"  - {hobby}")
else:
    st.write("No has seleccionado ningún hobby")

# ========================================
# SLIDER - CONTROL DESLIZANTE
# ========================================

st.divider()
st.header("3. Slider")

edad = st.slider("¿Cuántos años tienes?", min_value=18, max_value=100, value=30)
st.write(f"Edad: {edad} años")

# Slider con rango
rango_precio = st.slider(
    "Rango de precio que buscas ($)",
    min_value=0,
    max_value=1000,
    value=(200, 600),  # Tupla para rango
    step=50
)
st.write(f"Buscas seguros entre ${rango_precio[0]} y ${rango_precio[1]}")

# Slider con formato personalizado
calificacion = st.slider(
    "Califica nuestro servicio",
    min_value=1.0,
    max_value=5.0,
    value=4.5,
    step=0.1,
    format="%.1f ⭐"
)

# ========================================
# SELECT SLIDER
# ========================================

st.divider()
st.header("4. Select Slider")

prioridad = st.select_slider(
    "Prioridad del ticket",
    options=["Muy Baja", "Baja", "Media", "Alta", "Muy Alta"],
    value="Media"
)
st.write(f"Prioridad: **{prioridad}**")

# ========================================
# TOGGLE
# ========================================

st.divider()
st.header("5. Toggle (Interruptor)")

notificaciones = st.toggle("Activar notificaciones", value=True)

if notificaciones:
    st.success("✅ Notificaciones activadas")
else:
    st.info("🔕 Notificaciones desactivadas")

# ========================================
# APLICACIÓN PRÁCTICA: FILTRO DE SEGUROS
# ========================================

st.divider()
st.header("🎯 Aplicación Práctica: Filtro de Seguros")

st.write("Ayuda al usuario a encontrar el seguro perfecto")

col1, col2 = st.columns(2)

with col1:
    tipos_interes = st.multiselect(
        "Tipos de seguro de interés",
        ["Vida", "Auto", "Hogar", "Salud", "Viaje"],
        default=["Auto"]
    )
    
    presupuesto_max = st.slider(
        "Presupuesto mensual máximo ($)",
        min_value=20,
        max_value=200,
        value=50,
        step=10
    )

with col2:
    cobertura = st.select_slider(
        "Nivel de cobertura deseado",
        options=["Básica", "Estándar", "Premium", "Elite"],
        value="Estándar"
    )
    
    incluir_familia = st.toggle("Incluir cobertura familiar", value=False)

# Mostrar resumen
if st.button("🔍 Buscar seguros"):
    st.success("Resultados de búsqueda:")
    st.json({
        "tipos_seguros": tipos_interes,
        "presupuesto_mensual_max": f"${presupuesto_max}",
        "nivel_cobertura": cobertura,
        "cobertura_familiar": incluir_familia
    })
    
    st.info(f"""
    💡 **Recomendación**: 
    Con un presupuesto de ${presupuesto_max}/mes y cobertura {cobertura}, 
    te recomendamos nuestro plan {cobertura} que incluye {', '.join(tipos_interes)}.
    """)

# ========================================
# TIP
# ========================================

st.divider()
st.info("""
💡 **Tips de selectores**:

- **Selectbox**: Para elegir una opción de muchas
- **Multiselect**: Para elegir varias opciones
- **Slider**: Para valores numéricos en un rango
- **Select Slider**: Para valores discretos ordenados
- **Toggle**: Para opciones binarias (sí/no)
""")
