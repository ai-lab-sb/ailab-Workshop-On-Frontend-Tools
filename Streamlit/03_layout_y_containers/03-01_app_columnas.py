"""
Columnas y layouts en Streamlit
"""

import streamlit as st

st.title("📐 Columnas y Layouts")

# ========================================
# COLUMNAS BÁSICAS
# ========================================

st.header("1. Columnas Básicas (2 columnas iguales)")

col1, col2 = st.columns(2)

with col1:
    st.subheader("Columna 1")
    st.write("Este contenido está en la primera columna")
    st.button("Botón 1")

with col2:
    st.subheader("Columna 2")
    st.write("Este contenido está en la segunda columna")
    st.button("Botón 2")

# ========================================
# COLUMNAS CON PROPORCIONES DIFERENTES
# ========================================

st.divider()
st.header("2. Columnas con diferentes anchos")

col1, col2, col3 = st.columns([2, 1, 1])  # Primera columna es el doble

with col1:
    st.write("Columna ancha (2x)")
    st.info("Esta columna ocupa el doble de espacio")

with col2:
    st.write("Columna 2")
    st.success("Normal")

with col3:
    st.write("Columna 3")
    st.warning("Normal")

# ========================================
# 3 COLUMNAS CON MÉTRICAS
# ========================================

st.divider()
st.header("3. Dashboard con métricas")

st.write("Ejemplo: Panel de seguros vendidos")

col1, col2, col3 = st.columns(3)

with col1:
    st.metric(
        label="Seguros de Vida",
        value="1,234",
        delta="12%"
    )

with col2:
    st.metric(
        label="Seguros de Auto",
        value="890",
        delta="-5%",
        delta_color="inverse"
    )

with col3:
    st.metric(
        label="Seguros de Hogar",
        value="567",
        delta="8%"
    )

# ========================================
# EXPANDERS
# ========================================

st.divider()
st.header("4. Expanders (Contenido colapsable)")

with st.expander("📋 Ver términos y condiciones"):
    st.write("""
    Aquí puedes poner contenido que no quieres mostrar todo el tiempo.
    
    - Términos y condiciones
    - Información adicional
    - Detalles técnicos
    - FAQs
    
    El usuario puede expandir/colapsar según necesite.
    """)

with st.expander("📊 Ver estadísticas detalladas", expanded=True):
    # Este expander está expandido por defecto
    st.write("Datos detallados:")
    col1, col2 = st.columns(2)
    with col1:
        st.write("- Métrica A: 100")
        st.write("- Métrica B: 200")
    with col2:
        st.write("- Métrica C: 150")
        st.write("- Métrica D: 250")

# ========================================
# CONTAINERS
# ========================================

st.divider()
st.header("5. Containers")

st.write("Los containers te permiten agrupar elementos y actualizarlos después")

container = st.container()
container.write("Este es el contenido del container")

st.write("Este texto está fuera del container")

# Puedes agregar más cosas al container después
container.write("Agregamos esto al container después")

# ========================================
# EMPTY - PLACEHOLDER
# ========================================

st.divider()
st.header("6. Empty (Placeholder actualizable)")

placeholder = st.empty()

# Puedes actualizar el placeholder
if st.button("Mostrar mensaje 1"):
    placeholder.success("✅ Este es el mensaje 1")

if st.button("Mostrar mensaje 2"):
    placeholder.error("❌ Este es el mensaje 2")

if st.button("Limpiar"):
    placeholder.empty()

# ========================================
# LAYOUT COMPLETO: TARJETAS DE SEGUROS
# ========================================

st.divider()
st.header("🎯 Ejemplo: Tarjetas de Productos")

st.write("**Nuestros seguros más populares**")

col1, col2, col3 = st.columns(3)

with col1:
    with st.container():
        st.subheader("🚗 Seguro de Auto")
        st.write("Desde **$45/mes**")
        st.write("✅ Todo riesgo")
        st.write("✅ Asistencia 24/7")
        st.write("✅ Auto de reemplazo")
        if st.button("Más info", key="auto"):
            st.info("El seguro de auto más completo del mercado")

with col2:
    with st.container():
        st.subheader("🏠 Seguro de Hogar")
        st.write("Desde **$35/mes**")
        st.write("✅ Incendios y robos")
        st.write("✅ Responsabilidad civil")
        st.write("✅ Asistencia hogar")
        if st.button("Más info", key="hogar"):
            st.info("Protege tu hogar y tu familia")

with col3:
    with st.container():
        st.subheader("❤️ Seguro de Vida")
        st.write("Desde **$25/mes**")
        st.write("✅ Hasta $1M cobertura")
        st.write("✅ Beneficiarios ilimitados")
        st.write("✅ Pago flexible")
        if st.button("Más info", key="vida"):
            st.info("La tranquilidad de tu familia asegurada")

# ========================================
# TIP
# ========================================

st.divider()
st.info("""
💡 **Tips de Layout**:

- Usa **columnas** para comparar información lado a lado
- Usa **expanders** para contenido opcional o largo
- Usa **containers** cuando necesites actualizar contenido dinámicamente
- Usa **empty()** para placeholders que cambiarán
- Combina estos elementos para crear layouts complejos
""")
