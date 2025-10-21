"""
Elementos básicos de texto en Streamlit
Aprende a mostrar diferentes tipos de contenido
"""

import streamlit as st

# ========================================
# TÍTULOS Y ENCABEZADOS
# ========================================

st.title("🎨 Elementos Básicos de Streamlit")
st.header("Bienvenido al curso")
st.subheader("Aprende lo fundamental")

# ========================================
# TEXTO SIMPLE
# ========================================

st.text("Este es texto simple con st.text()")
st.text("Es útil para mostrar texto plano sin formato")

# ========================================
# WRITE - EL MÁS VERSÁTIL
# ========================================

st.write("---")  # Separador
st.header("📝 st.write() - El comando mágico")

st.write("st.write() puede mostrar casi cualquier cosa:")
st.write("- Texto normal")
st.write("- **Texto en negrita**")
st.write("- *Texto en cursiva*")
st.write("- Números:", 42)
st.write("- Listas:", [1, 2, 3, 4, 5])
st.write("- Diccionarios:", {"nombre": "Juan", "edad": 30})

# ========================================
# MARKDOWN
# ========================================

st.write("---")
st.header("📄 Markdown")

st.markdown("""
### Puedes usar Markdown completo

Markdown te permite formatear texto fácilmente:

- **Negrita** con `**texto**`
- *Cursiva* con `*texto*`
- `Código inline` con \`texto\`
- [Enlaces](https://streamlit.io)
- Listas con guiones

> Este es un bloque de cita

1. Lista numerada
2. Segundo elemento
3. Tercer elemento
""")

# ========================================
# CÓDIGO
# ========================================

st.write("---")
st.header("💻 Bloques de código")

st.code("""
def saludar(nombre):
    return f"Hola, {nombre}!"

mensaje = saludar("Mundo")
print(mensaje)
""", language="python")

st.write("También puedes mostrar código en otros lenguajes:")

st.code("""
SELECT nombre, edad 
FROM usuarios 
WHERE edad > 18
ORDER BY nombre;
""", language="sql")

# ========================================
# EMOJIS
# ========================================

st.write("---")
st.header("😀 Emojis")

st.write("Streamlit soporta emojis nativamente:")
st.write("🎉 🚀 💡 ⚡ 🎯 📊 🤖 💬 ✅ ❌ ⚠️ 📱 💻 🔥")

# ========================================
# LATEX (MATEMÁTICAS)
# ========================================

st.write("---")
st.header("🔢 Fórmulas matemáticas (LaTeX)")

st.latex(r"e^{i\pi} + 1 = 0")

st.write("También puedes escribir fórmulas inline: $E = mc^2$")

# ========================================
# MENSAJES DE ESTADO
# ========================================

st.write("---")
st.header("📢 Mensajes especiales")

st.success("✅ Esto es un mensaje de éxito")
st.info("ℹ️ Esto es un mensaje informativo")
st.warning("⚠️ Esto es una advertencia")
st.error("❌ Esto es un mensaje de error")

# ========================================
# DIVIDER
# ========================================

st.divider()  # Línea divisoria moderna

# ========================================
# CAPTION
# ========================================

st.header("Texto final")
st.caption("Este es un caption - texto pequeño para aclaraciones")

# ========================================
# TIP FINAL
# ========================================

st.write("---")
st.info("""
💡 **Tip**: `st.write()` es el comando más versátil. 
Cuando tengas duda, úsalo. Streamlit detectará automáticamente 
qué tipo de contenido estás pasando y lo mostrará apropiadamente.
""")
