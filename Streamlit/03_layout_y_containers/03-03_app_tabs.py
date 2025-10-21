"""
Tabs (pestañas) para organizar contenido en Streamlit
"""

import streamlit as st

st.title("📑 Tabs - Organización por Pestañas")

st.write("""
Las tabs son perfectas para organizar contenido relacionado en secciones separadas.
El usuario puede navegar entre ellas sin recargar la página.
""")

# ========================================
# TABS BÁSICAS
# ========================================

st.header("1. Tabs Básicas")

tab1, tab2, tab3 = st.tabs(["📊 Datos", "📈 Gráficas", "⚙️ Configuración"])

with tab1:
    st.subheader("Datos")
    st.write("Aquí puedes mostrar datos en formato tabla")
    
    import pandas as pd
    
    df = pd.DataFrame({
        'Producto': ['Seguro de Vida', 'Seguro de Auto', 'Seguro de Hogar'],
        'Precio': [25, 45, 35],
        'Ventas': [1234, 890, 567]
    })
    
    st.dataframe(df, use_container_width=True)

with tab2:
    st.subheader("Gráficas")
    st.write("Aquí puedes mostrar visualizaciones")
    st.bar_chart(df.set_index('Producto')['Ventas'])

with tab3:
    st.subheader("Configuración")
    st.write("Opciones de configuración")
    
    mostrar_detalles = st.checkbox("Mostrar detalles avanzados")
    theme = st.selectbox("Tema", ["Claro", "Oscuro", "Auto"])
    idioma = st.radio("Idioma", ["Español", "English"])
    
    if st.button("Guardar configuración"):
        st.success("✅ Configuración guardada")

# ========================================
# TABS CON EMOJIS Y CONTENIDO COMPLEJO
# ========================================

st.divider()
st.header("2. Tabs de Productos")

tab_vida, tab_auto, tab_hogar, tab_salud, tab_viaje = st.tabs([
    "❤️ Vida",
    "🚗 Auto", 
    "🏠 Hogar",
    "🏥 Salud",
    "✈️ Viaje"
])

with tab_vida:
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.subheader("Seguro de Vida")
        st.write("""
        Protege a tu familia con nuestro seguro de vida.
        
        **Beneficios:**
        - Cobertura desde $50,000 hasta $1,000,000
        - Beneficiarios ilimitados
        - Cobertura por muerte natural o accidental
        - Opciones de pago flexibles
        """)
    
    with col2:
        st.metric("Desde", "$25/mes")
        st.metric("Cobertura máxima", "$1M")
        if st.button("Cotizar", key="vida"):
            st.success("Solicitud enviada")

with tab_auto:
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.subheader("Seguro de Auto")
        st.write("""
        Tu auto protegido en todo momento.
        
        **Beneficios:**
        - Todo riesgo con franquicia desde $500
        - Asistencia en carretera 24/7
        - Auto de reemplazo
        - Cobertura a terceros incluida
        """)
    
    with col2:
        st.metric("Desde", "$45/mes")
        st.metric("Cobertura", "Todo riesgo")
        if st.button("Cotizar", key="auto"):
            st.success("Solicitud enviada")

with tab_hogar:
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.subheader("Seguro de Hogar")
        st.write("""
        Tu hogar seguro y protegido.
        
        **Beneficios:**
        - Protección contra incendios, robos e inundaciones
        - Responsabilidad civil incluida
        - Cobertura de contenidos hasta $200,000
        - Asistencia de emergencia
        """)
    
    with col2:
        st.metric("Desde", "$35/mes")
        st.metric("Cobertura", "$200K")
        if st.button("Cotizar", key="hogar"):
            st.success("Solicitud enviada")

with tab_salud:
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.subheader("Seguro de Salud")
        st.write("""
        Tu salud, nuestra prioridad.
        
        **Beneficios:**
        - Red de más de 500 clínicas y hospitales
        - Cobertura dental y oftalmológica
        - Medicamentos con descuento del 50%
        - Chequeos anuales gratuitos
        """)
    
    with col2:
        st.metric("Desde", "$80/mes")
        st.metric("Red", "500+ centros")
        if st.button("Cotizar", key="salud"):
            st.success("Solicitud enviada")

with tab_viaje:
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.subheader("Seguro de Viaje")
        st.write("""
        Viaja tranquilo, nosotros te cuidamos.
        
        **Beneficios:**
        - Cobertura internacional
        - Asistencia médica en el extranjero
        - Cancelación de vuelos
        - Pérdida de equipaje
        """)
    
    with col2:
        st.metric("Desde", "$15/viaje")
        st.metric("Cobertura", "Internacional")
        if st.button("Cotizar", key="viaje"):
            st.success("Solicitud enviada")

# ========================================
# TIP
# ========================================

st.divider()
st.info("""
💡 **Cuándo usar Tabs**:

- Para organizar contenido relacionado pero separado
- Cuando tienes múltiples vistas de los mismos datos
- Para evitar páginas muy largas
- Para comparar información lado a lado
- Ideal para dashboards y paneles de control

**Ventaja**: El usuario puede navegar sin recargar la página
""")
