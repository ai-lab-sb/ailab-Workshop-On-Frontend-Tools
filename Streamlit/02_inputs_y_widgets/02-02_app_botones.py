"""
Botones y formularios en Streamlit
"""

import streamlit as st

st.title("🔘 Botones y Formularios")

# ========================================
# BOTÓN SIMPLE
# ========================================

st.header("1. Botón Simple")

st.write("Los botones retornan `True` cuando son presionados")

if st.button("Presióname"):
    st.success("¡Botón presionado! 🎉")
    st.balloons()  # Animación de globos

# ========================================
# BOTÓN CON USO PRÁCTICO
# ========================================

st.divider()
st.header("2. Contador con Botón")

st.write("**Problema**: El contador se reinicia porque la app se re-ejecuta")
st.write("(Esto lo resolveremos con Session State en la siguiente lección)")

contador = 0  # Esto se reinicia cada vez

if st.button("Incrementar (no funciona correctamente)"):
    contador += 1

st.write(f"Contador: {contador}")

# ========================================
# DOWNLOAD BUTTON
# ========================================

st.divider()
st.header("3. Botón de Descarga")

texto_para_descargar = """
Este es un archivo de texto generado por Streamlit.
¡Puedes descargar cualquier tipo de contenido!
"""

st.download_button(
    label="📥 Descargar archivo de texto",
    data=texto_para_descargar,
    file_name="mi_archivo.txt",
    mime="text/plain"
)

# ========================================
# FORMULARIOS
# ========================================

st.divider()
st.header("4. Formularios")

st.write("""
Los formularios agrupan widgets y solo se ejecutan cuando presionas el botón submit.
Esto previene que la app se re-ejecute con cada cambio.
""")

with st.form("mi_formulario"):
    st.subheader("Formulario de Registro")
    
    nombre = st.text_input("Nombre completo")
    email = st.text_input("Email")
    edad = st.number_input("Edad", min_value=18, max_value=100, value=25)
    
    tipo_seguro = st.selectbox(
        "Tipo de seguro de interés",
        ["Vida", "Auto", "Hogar", "Salud", "Viaje"]
    )
    
    acepta_terminos = st.checkbox("Acepto términos y condiciones")
    
    # Botón de submit (obligatorio en formularios)
    submitted = st.form_submit_button("Enviar formulario")
    
    if submitted:
        if not acepta_terminos:
            st.error("❌ Debes aceptar los términos y condiciones")
        elif not nombre or not email:
            st.warning("⚠️ Por favor completa todos los campos")
        else:
            st.success("✅ Formulario enviado correctamente")
            st.json({
                "nombre": nombre,
                "email": email,
                "edad": edad,
                "tipo_seguro": tipo_seguro
            })

# ========================================
# CHECKBOX
# ========================================

st.divider()
st.header("5. Checkbox")

acepto = st.checkbox("Acepto los términos")

if acepto:
    st.write("✅ Has aceptado los términos")

mostrar_detalles = st.checkbox("Mostrar detalles avanzados")

if mostrar_detalles:
    st.info("""
    Aquí puedes mostrar información adicional que solo aparece 
    cuando el usuario marca el checkbox.
    """)

# ========================================
# RADIO BUTTONS
# ========================================

st.divider()
st.header("6. Radio Buttons")

opcion = st.radio(
    "¿Cuál es tu lenguaje de programación favorito?",
    ["Python", "JavaScript", "Java", "C++", "Otro"]
)

st.write(f"Seleccionaste: **{opcion}**")

# Radio horizontal
formato = st.radio(
    "Formato de salida",
    ["JSON", "CSV", "XML"],
    horizontal=True
)

# ========================================
# TIP
# ========================================

st.divider()
st.info("""
💡 **Tip importante**: 

- Usa **botones simples** para acciones únicas
- Usa **formularios** cuando tengas múltiples inputs relacionados
- Usa **checkboxes** para mostrar/ocultar contenido opcional
- Usa **radio buttons** para opciones mutuamente excluyentes
""")
