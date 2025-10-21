"""
Conceptos básicos de consumo de APIs con Streamlit
"""

import streamlit as st
import requests
import json

st.title("🌐 Consumiendo APIs REST")

# ========================================
# INTRODUCCIÓN
# ========================================

st.header("📖 ¿Qué es una API REST?")

st.write("""
Una API REST permite que aplicaciones se comuniquen entre sí usando HTTP.
Es como un "mesero" que toma tu orden (request) y te trae la comida (response).
""")

with st.expander("Ver conceptos básicos"):
    st.write("""
    **Métodos HTTP comunes:**
    - **GET**: Obtener datos (leer)
    - **POST**: Enviar datos (crear)
    - **PUT**: Actualizar datos
    - **DELETE**: Eliminar datos
    
    **Componentes de un request:**
    - URL: Dirección del recurso
    - Headers: Metadatos del request
    - Body: Datos que enviamos (en POST/PUT)
    
    **Respuestas comunes:**
    - 200: Éxito
    - 404: No encontrado
    - 500: Error del servidor
    """)

# ========================================
# GET REQUEST SIMPLE
# ========================================

st.divider()
st.header("1. GET Request - Obtener Datos")

st.write("Vamos a obtener datos de una API pública de prueba")

# API pública para testing
API_URL = "https://jsonplaceholder.typicode.com"

if st.button("Obtener lista de usuarios"):
    with st.spinner("Obteniendo datos..."):
        try:
            response = requests.get(f"{API_URL}/users", timeout=10)
            
            if response.status_code == 200:
                users = response.json()
                st.success(f"✅ Se obtuvieron {len(users)} usuarios")
                
                # Mostrar los primeros 3 usuarios
                import pandas as pd
                df = pd.DataFrame(users)
                st.dataframe(df[['id', 'name', 'email', 'phone']], use_container_width=True)
            else:
                st.error(f"❌ Error: {response.status_code}")
                
        except requests.exceptions.RequestException as e:
            st.error(f"❌ Error en la solicitud: {e}")

# ========================================
# GET CON PARÁMETROS
# ========================================

st.divider()
st.header("2. GET con Parámetros")

user_id = st.number_input("ID del usuario a buscar", min_value=1, max_value=10, value=1)

if st.button("Buscar usuario"):
    with st.spinner(f"Buscando usuario {user_id}..."):
        try:
            response = requests.get(f"{API_URL}/users/{user_id}", timeout=10)
            
            if response.status_code == 200:
                user = response.json()
                st.success("✅ Usuario encontrado")
                
                col1, col2 = st.columns(2)
                
                with col1:
                    st.write("**Información Personal**")
                    st.write(f"Nombre: {user['name']}")
                    st.write(f"Email: {user['email']}")
                    st.write(f"Teléfono: {user['phone']}")
                    st.write(f"Website: {user['website']}")
                
                with col2:
                    st.write("**Dirección**")
                    st.write(f"Ciudad: {user['address']['city']}")
                    st.write(f"Calle: {user['address']['street']}")
                    st.write(f"Código postal: {user['address']['zipcode']}")
                    
            elif response.status_code == 404:
                st.error("❌ Usuario no encontrado")
            else:
                st.error(f"❌ Error: {response.status_code}")
                
        except requests.exceptions.RequestException as e:
            st.error(f"❌ Error en la solicitud: {e}")

# ========================================
# POST REQUEST
# ========================================

st.divider()
st.header("3. POST Request - Enviar Datos")

st.write("Envía datos al servidor (simulado)")

with st.form("post_form"):
    titulo = st.text_input("Título del post")
    contenido = st.text_area("Contenido")
    submitted = st.form_submit_button("Publicar")
    
    if submitted:
        if titulo and contenido:
            # Datos a enviar
            datos = {
                "title": titulo,
                "body": contenido,
                "userId": 1
            }
            
            with st.spinner("Publicando..."):
                try:
                    response = requests.post(
                        f"{API_URL}/posts",
                        json=datos,
                        timeout=10
                    )
                    
                    if response.status_code == 201:  # 201 = Created
                        resultado = response.json()
                        st.success("✅ Post publicado exitosamente")
                        st.json(resultado)
                    else:
                        st.error(f"❌ Error: {response.status_code}")
                        
                except requests.exceptions.RequestException as e:
                    st.error(f"❌ Error en la solicitud: {e}")
        else:
            st.warning("⚠️ Por favor completa todos los campos")

# ========================================
# MANEJO DE ERRORES
# ========================================

st.divider()
st.header("4. Manejo de Errores")

st.write("Prueba diferentes escenarios de error:")

error_tipo = st.selectbox(
    "Tipo de prueba",
    ["URL inválida", "Timeout", "URL inexistente"]
)

if st.button("Probar error"):
    try:
        if error_tipo == "URL inválida":
            response = requests.get("not-a-valid-url", timeout=5)
        elif error_tipo == "Timeout":
            response = requests.get("https://httpbin.org/delay/10", timeout=2)
        else:  # URL inexistente
            response = requests.get(f"{API_URL}/endpoint-que-no-existe", timeout=5)
        
        response.raise_for_status()
        st.success("✅ Éxito")
        
    except requests.exceptions.Timeout:
        st.error("❌ Error: La solicitud tardó demasiado (timeout)")
    except requests.exceptions.ConnectionError:
        st.error("❌ Error: No se pudo conectar al servidor")
    except requests.exceptions.HTTPError as e:
        st.error(f"❌ Error HTTP: {e}")
    except requests.exceptions.RequestException as e:
        st.error(f"❌ Error en la solicitud: {e}")

# ========================================
# CÓDIGO DE EJEMPLO
# ========================================

st.divider()
st.header("💻 Código de Ejemplo")

with st.expander("Ver código de un request completo"):
    st.code("""
import requests
import streamlit as st

# GET request
try:
    response = requests.get(
        "https://api.example.com/data",
        params={"id": 123},
        headers={"Authorization": "Bearer token"},
        timeout=10
    )
    
    if response.status_code == 200:
        data = response.json()
        st.success("✅ Datos obtenidos")
        st.json(data)
    else:
        st.error(f"Error: {response.status_code}")
        
except requests.exceptions.RequestException as e:
    st.error(f"Error: {e}")

# POST request
try:
    response = requests.post(
        "https://api.example.com/submit",
        json={"message": "Hola"},
        timeout=10
    )
    
    if response.status_code == 201:
        st.success("✅ Datos enviados")
        
except requests.exceptions.RequestException as e:
    st.error(f"Error: {e}")
""", language="python")

# ========================================
# TIP
# ========================================

st.divider()
st.info("""
💡 **Mejores prácticas**:

1. **Siempre usa timeout**: `requests.get(url, timeout=10)`
2. **Maneja errores**: Usa try/except
3. **Muestra feedback**: Usa spinner, success, error
4. **Valida respuestas**: Verifica status_code
5. **Usa raise_for_status()**: Para lanzar excepciones automáticas

**En el proyecto final** usaremos estos conceptos para comunicarnos con el agente de seguros! 🤖
""")
