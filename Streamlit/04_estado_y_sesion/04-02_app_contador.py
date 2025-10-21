"""
Aplicación práctica: Contador con Session State
"""

import streamlit as st
from datetime import datetime

st.set_page_config(page_title="Contador Avanzado", page_icon="🔢")

st.title("🔢 Contador Avanzado con Session State")

# ========================================
# INICIALIZAR SESSION STATE
# ========================================

if "contador" not in st.session_state:
    st.session_state.contador = 0

if "historial" not in st.session_state:
    st.session_state.historial = []

if "paso" not in st.session_state:
    st.session_state.paso = 1

# ========================================
# CONFIGURACIÓN
# ========================================

st.sidebar.header("⚙️ Configuración")

st.session_state.paso = st.sidebar.slider(
    "Valor del incremento/decremento",
    min_value=1,
    max_value=10,
    value=st.session_state.paso
)

color = st.sidebar.color_picker("Color del contador", "#1f77b4")

# ========================================
# DISPLAY PRINCIPAL
# ========================================

# Mostrar el contador en grande
st.markdown(
    f"""
    <div style="text-align: center; padding: 30px;">
        <h1 style="font-size: 80px; color: {color};">{st.session_state.contador}</h1>
    </div>
    """,
    unsafe_allow_html=True
)

# ========================================
# CONTROLES
# ========================================

col1, col2, col3, col4 = st.columns(4)

with col1:
    if st.button("➕ Incrementar", use_container_width=True):
        st.session_state.contador += st.session_state.paso
        st.session_state.historial.append({
            "accion": f"+{st.session_state.paso}",
            "valor": st.session_state.contador,
            "hora": datetime.now().strftime("%H:%M:%S")
        })

with col2:
    if st.button("➖ Decrementar", use_container_width=True):
        st.session_state.contador -= st.session_state.paso
        st.session_state.historial.append({
            "accion": f"-{st.session_state.paso}",
            "valor": st.session_state.contador,
            "hora": datetime.now().strftime("%H:%M:%S")
        })

with col3:
    if st.button("✖️ Duplicar", use_container_width=True):
        nuevo_valor = st.session_state.contador * 2
        st.session_state.historial.append({
            "accion": "×2",
            "valor": nuevo_valor,
            "hora": datetime.now().strftime("%H:%M:%S")
        })
        st.session_state.contador = nuevo_valor

with col4:
    if st.button("🔄 Resetear", use_container_width=True):
        st.session_state.contador = 0
        st.session_state.historial.append({
            "accion": "Reset",
            "valor": 0,
            "hora": datetime.now().strftime("%H:%M:%S")
        })

# ========================================
# ESTADÍSTICAS
# ========================================

st.divider()

col1, col2, col3 = st.columns(3)

with col1:
    st.metric(
        "Valor Actual",
        st.session_state.contador,
        delta=None if not st.session_state.historial else st.session_state.historial[-1]["accion"]
    )

with col2:
    st.metric(
        "Operaciones Realizadas",
        len(st.session_state.historial)
    )

with col3:
    if st.session_state.historial:
        valores = [h["valor"] for h in st.session_state.historial]
        st.metric(
            "Valor Máximo Alcanzado",
            max(valores)
        )
    else:
        st.metric("Valor Máximo Alcanzado", 0)

# ========================================
# HISTORIAL
# ========================================

st.divider()
st.header("📜 Historial de Operaciones")

if st.session_state.historial:
    # Mostrar historial en tabla
    import pandas as pd
    
    df = pd.DataFrame(st.session_state.historial)
    st.dataframe(
        df.iloc[::-1],  # Invertir para mostrar lo más reciente primero
        use_container_width=True,
        hide_index=True
    )
    
    # Botón para limpiar historial
    if st.button("🗑️ Limpiar Historial"):
        st.session_state.historial = []
        st.rerun()
    
    # Gráfica del historial
    if len(st.session_state.historial) > 1:
        st.line_chart(df.set_index("hora")["valor"])
else:
    st.info("No hay operaciones en el historial. ¡Empieza a usar el contador!")

# ========================================
# INFORMACIÓN
# ========================================

st.divider()

with st.expander("ℹ️ ¿Cómo funciona?"):
    st.write("""
    ### Session State en acción
    
    Este contador demuestra cómo usar `st.session_state` para:
    
    1. **Mantener el valor del contador** entre interacciones
    2. **Guardar un historial** de todas las operaciones
    3. **Personalizar la experiencia** con configuraciones que persisten
    
    #### Código clave:
    ```python
    # Inicializar
    if "contador" not in st.session_state:
        st.session_state.contador = 0
    
    # Incrementar
    if st.button("Incrementar"):
        st.session_state.contador += 1
    
    # Leer
    st.write(st.session_state.contador)
    ```
    
    **Sin Session State**, el contador se resetearía a 0 con cada clic.
    **Con Session State**, el valor persiste durante toda la sesión.
    """)

# ========================================
# DESAFÍO
# ========================================

st.divider()
st.success("""
🎯 **Desafío**: 

Modifica esta app para agregar:
1. Un botón que divida el contador entre 2
2. Un botón que eleve el contador al cuadrado
3. Un límite máximo y mínimo para el contador
4. Exportar el historial como CSV
""")
