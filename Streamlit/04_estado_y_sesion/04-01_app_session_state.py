"""
Session State en Streamlit
Aprende a mantener valores entre ejecuciones
"""

import streamlit as st

st.title("💾 Session State - Estado Persistente")

# ========================================
# PROBLEMA: SIN SESSION STATE
# ========================================

st.header("❌ Problema: Sin Session State")

st.write("Intenta incrementar este contador:")

contador_simple = 0  # Esta variable se reinicia cada vez

if st.button("Incrementar (no funciona)"):
    contador_simple += 1

st.write(f"Contador: {contador_simple}")
st.error("El contador siempre muestra 0 porque la variable se reinicia con cada interacción")

# ========================================
# SOLUCIÓN: CON SESSION STATE
# ========================================

st.divider()
st.header("✅ Solución: Con Session State")

# Inicializar session state
if "contador" not in st.session_state:
    st.session_state.contador = 0

st.write("Ahora sí funciona:")

if st.button("Incrementar (funciona)"):
    st.session_state.contador += 1

st.write(f"Contador: **{st.session_state.contador}**")
st.success("El valor se mantiene porque está en Session State")

if st.button("Resetear contador"):
    st.session_state.contador = 0

# ========================================
# MÚLTIPLES VALORES EN SESSION STATE
# ========================================

st.divider()
st.header("📦 Múltiples Valores en Session State")

# Inicializar múltiples valores
if "nombre" not in st.session_state:
    st.session_state.nombre = ""
if "edad" not in st.session_state:
    st.session_state.edad = 25
if "seguros_seleccionados" not in st.session_state:
    st.session_state.seguros_seleccionados = []

# Inputs que actualizan session state
nombre = st.text_input(
    "Nombre", 
    value=st.session_state.nombre,
    key="input_nombre"
)
st.session_state.nombre = nombre

edad = st.number_input(
    "Edad",
    min_value=18,
    max_value=100,
    value=st.session_state.edad,
    key="input_edad"
)
st.session_state.edad = edad

# Mostrar valores guardados
st.write("**Valores en Session State:**")
st.json({
    "nombre": st.session_state.nombre,
    "edad": st.session_state.edad,
    "contador": st.session_state.contador
})

# ========================================
# LISTA EN SESSION STATE
# ========================================

st.divider()
st.header("📋 Listas en Session State")

st.write("Agrega seguros a tu lista de interés:")

seguros_disponibles = ["Vida", "Auto", "Hogar", "Salud", "Viaje"]

seguro_seleccionado = st.selectbox("Selecciona un seguro", seguros_disponibles)

col1, col2 = st.columns(2)

with col1:
    if st.button("➕ Agregar a mi lista"):
        if seguro_seleccionado not in st.session_state.seguros_seleccionados:
            st.session_state.seguros_seleccionados.append(seguro_seleccionado)
            st.success(f"✅ {seguro_seleccionado} agregado")
        else:
            st.warning("Ya está en tu lista")

with col2:
    if st.button("🗑️ Limpiar lista"):
        st.session_state.seguros_seleccionados = []
        st.info("Lista limpiada")

# Mostrar lista
if st.session_state.seguros_seleccionados:
    st.write("**Tu lista de seguros de interés:**")
    for i, seguro in enumerate(st.session_state.seguros_seleccionados, 1):
        st.write(f"{i}. {seguro}")
else:
    st.info("Tu lista está vacía")

# ========================================
# DICCIONARIO EN SESSION STATE
# ========================================

st.divider()
st.header("📊 Diccionarios en Session State")

# Inicializar diccionario
if "carrito" not in st.session_state:
    st.session_state.carrito = {}

st.write("**Carrito de seguros:**")

# Agregar al carrito
productos = {
    "Seguro de Vida": 25,
    "Seguro de Auto": 45,
    "Seguro de Hogar": 35,
    "Seguro de Salud": 80
}

col1, col2 = st.columns([2, 1])

with col1:
    producto = st.selectbox("Selecciona un producto", list(productos.keys()))

with col2:
    cantidad = st.number_input("Cantidad", min_value=1, max_value=10, value=1)

if st.button("🛒 Agregar al carrito"):
    if producto in st.session_state.carrito:
        st.session_state.carrito[producto] += cantidad
    else:
        st.session_state.carrito[producto] = cantidad
    st.success(f"✅ {cantidad}x {producto} agregado al carrito")

# Mostrar carrito
if st.session_state.carrito:
    st.write("**Contenido del carrito:**")
    total = 0
    for producto, cantidad in st.session_state.carrito.items():
        precio = productos[producto] * cantidad
        total += precio
        st.write(f"- {producto}: {cantidad} x ${productos[producto]} = ${precio}")
    
    st.write(f"**Total: ${total}/mes**")
    
    if st.button("🗑️ Vaciar carrito"):
        st.session_state.carrito = {}
        st.rerun()
else:
    st.info("El carrito está vacío")

# ========================================
# VER TODO EL SESSION STATE
# ========================================

st.divider()
st.header("🔍 Ver todo el Session State")

with st.expander("Ver contenido completo de session_state"):
    st.write(st.session_state)

# ========================================
# TIP
# ========================================

st.divider()
st.info("""
💡 **Tips importantes de Session State**:

1. **Inicializa siempre**: Verifica si existe antes de usar
2. **Úsalo para persistencia**: Todo lo que quieras mantener entre ejecuciones
3. **Cualquier tipo de dato**: Strings, números, listas, diccionarios, objetos
4. **Es por sesión**: Cada usuario tiene su propio session_state
5. **Se pierde al cerrar el browser**: No es persistencia permanente

**Uso en el proyecto final**: Usaremos session_state para mantener el historial del chat 💬
""")
