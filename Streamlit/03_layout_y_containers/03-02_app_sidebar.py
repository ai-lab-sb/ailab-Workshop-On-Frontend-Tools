"""
Sidebar para navegación y controles en Streamlit
"""

import streamlit as st

# ========================================
# CONFIGURACIÓN DE LA PÁGINA
# ========================================

st.set_page_config(
    page_title="App con Sidebar",
    page_icon="🎯",
    layout="wide"  # Layout ancho para aprovechar el espacio
)

# ========================================
# SIDEBAR - BARRA LATERAL
# ========================================

st.sidebar.title("🎯 Panel de Control")
st.sidebar.write("Usa este menú para navegar")

# Navegación principal
pagina = st.sidebar.radio(
    "Selecciona una sección",
    ["Inicio", "Productos", "Cotizador", "Contacto"]
)

st.sidebar.divider()

# Filtros
st.sidebar.subheader("Filtros")

tipo_seguro = st.sidebar.multiselect(
    "Tipo de seguro",
    ["Vida", "Auto", "Hogar", "Salud", "Viaje"],
    default=["Auto"]
)

presupuesto = st.sidebar.slider(
    "Presupuesto mensual ($)",
    min_value=20,
    max_value=200,
    value=50
)

st.sidebar.divider()

# Información adicional
with st.sidebar.expander("ℹ️ Acerca de"):
    st.write("""
    **SegurosVida+**
    
    Tu tranquilidad, nuestra prioridad.
    
    25 años de experiencia en el mercado.
    """)

# Botón de acción
if st.sidebar.button("🔍 Buscar Seguros", type="primary"):
    st.sidebar.success("Búsqueda iniciada!")

# ========================================
# CONTENIDO PRINCIPAL
# ========================================

st.title("Aplicación con Sidebar")

# Mostrar contenido según la página seleccionada
if pagina == "Inicio":
    st.header("🏠 Bienvenido a SegurosVida+")
    st.write("Tu tranquilidad, nuestra prioridad")
    
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("Clientes Satisfechos", "10,000+")
    with col2:
        st.metric("Años de Experiencia", "25")
    with col3:
        st.metric("Calificación", "4.8/5 ⭐")
    
    st.info(f"""
    **Filtros activos**:
    - Tipos de seguro: {', '.join(tipo_seguro) if tipo_seguro else 'Ninguno'}
    - Presupuesto: ${presupuesto}/mes
    """)

elif pagina == "Productos":
    st.header("📦 Nuestros Productos")
    
    st.write(f"Mostrando seguros: **{', '.join(tipo_seguro)}**")
    st.write(f"Con presupuesto de: **${presupuesto}/mes**")
    
    for seguro in tipo_seguro:
        with st.expander(f"Seguro de {seguro}"):
            st.write(f"Detalles del seguro de {seguro}")
            st.write(f"Precio estimado: ${presupuesto}/mes")
            st.button(f"Cotizar {seguro}", key=f"btn_{seguro}")

elif pagina == "Cotizador":
    st.header("💰 Cotizador")
    
    st.write("Obtén una cotización personalizada")
    
    with st.form("formulario_cotizacion"):
        nombre = st.text_input("Nombre completo")
        email = st.text_input("Email")
        telefono = st.text_input("Teléfono")
        
        submitted = st.form_submit_button("Solicitar Cotización")
        
        if submitted:
            if nombre and email:
                st.success(f"""
                ✅ Cotización enviada para {nombre}
                
                Te contactaremos pronto al email: {email}
                """)
            else:
                st.error("Por favor completa todos los campos")

else:  # Contacto
    st.header("📞 Contacto")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("Información de contacto")
        st.write("📞 Teléfono: 1-800-SEGVIDA")
        st.write("📧 Email: contacto@segurosvida.com")
        st.write("📱 WhatsApp: +57 300 123 4567")
    
    with col2:
        st.subheader("Horarios")
        st.write("Lunes a Viernes: 8:00 AM - 6:00 PM")
        st.write("Sábados: 9:00 AM - 1:00 PM")
        st.write("Domingos: Cerrado")

# ========================================
# FOOTER EN SIDEBAR
# ========================================

st.sidebar.divider()
st.sidebar.caption("© 2025 SegurosVida+")
st.sidebar.caption("Todos los derechos reservados")
