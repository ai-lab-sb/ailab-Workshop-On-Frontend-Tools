"""
Ejemplo práctico: Consumir API de clima
"""

import streamlit as st
import requests

st.set_page_config(page_title="App del Clima", page_icon="🌤️")

st.title("🌤️ Aplicación del Clima")
st.write("Ejemplo práctico de consumo de API")

# ========================================
# INFORMACIÓN
# ========================================

st.info("""
Esta app consume la API de OpenWeather para obtener datos del clima.

**Nota**: Para uso en producción necesitarías una API key gratuita de:
https://openweathermap.org/api

Para este ejemplo usamos una API pública alternativa.
""")

# ========================================
# API ALTERNATIVA (sin key required)
# ========================================

st.header("🌍 Consultar Clima")

ciudad = st.text_input(
    "Nombre de la ciudad",
    value="Bogota",
    placeholder="Ej: Bogota, Medellin, Cali"
)

col1, col2 = st.columns([1, 3])

with col1:
    if st.button("🔍 Consultar", type="primary"):
        if ciudad:
            with st.spinner(f"Obteniendo clima de {ciudad}..."):
                try:
                    # Usando wttr.in - API pública de clima sin API key
                    url = f"https://wttr.in/{ciudad}?format=j1"
                    
                    response = requests.get(url, timeout=10)
                    
                    if response.status_code == 200:
                        data = response.json()
                        
                        # Obtener datos actuales
                        current = data['current_condition'][0]
                        temp_c = current['temp_C']
                        feels_like = current['FeelsLikeC']
                        descripcion = current['weatherDesc'][0]['value']
                        humedad = current['humidity']
                        viento = current['windspeedKmph']
                        
                        # Mostrar resultados
                        st.success(f"✅ Datos obtenidos para {ciudad}")
                        
                        # Métricas principales
                        col1, col2, col3 = st.columns(3)
                        
                        with col1:
                            st.metric(
                                "🌡️ Temperatura",
                                f"{temp_c}°C",
                                delta=f"Sensación: {feels_like}°C"
                            )
                        
                        with col2:
                            st.metric(
                                "💧 Humedad",
                                f"{humedad}%"
                            )
                        
                        with col3:
                            st.metric(
                                "💨 Viento",
                                f"{viento} km/h"
                            )
                        
                        # Descripción
                        st.write(f"**Condición**: {descripcion}")
                        
                        # Pronóstico
                        st.subheader("📅 Pronóstico 3 días")
                        
                        for day in data['weather'][:3]:
                            fecha = day['date']
                            max_temp = day['maxtempC']
                            min_temp = day['mintempC']
                            desc = day['hourly'][0]['weatherDesc'][0]['value']
                            
                            with st.expander(f"{fecha} - {desc}"):
                                col1, col2 = st.columns(2)
                                with col1:
                                    st.write(f"🔺 Máxima: {max_temp}°C")
                                with col2:
                                    st.write(f"🔻 Mínima: {min_temp}°C")
                        
                        # Mostrar JSON completo
                        with st.expander("📊 Ver datos completos (JSON)"):
                            st.json(data)
                            
                    else:
                        st.error(f"❌ Error: {response.status_code}")
                        st.write("No se pudieron obtener los datos. Verifica el nombre de la ciudad.")
                        
                except requests.exceptions.Timeout:
                    st.error("❌ La solicitud tardó demasiado. Intenta de nuevo.")
                except requests.exceptions.ConnectionError:
                    st.error("❌ No se pudo conectar a la API. Verifica tu conexión.")
                except requests.exceptions.RequestException as e:
                    st.error(f"❌ Error: {e}")
                except KeyError:
                    st.error("❌ Ciudad no encontrada. Verifica el nombre.")
        else:
            st.warning("⚠️ Por favor ingresa el nombre de una ciudad")

# ========================================
# EJEMPLO CON API PÚBLICA DE DATOS RANDOM
# ========================================

st.divider()
st.header("🐱 Bonus: API de Datos de Gatos")

st.write("Otro ejemplo de API pública")

if st.button("🎲 Obtener dato random de gatos"):
    with st.spinner("Obteniendo dato..."):
        try:
            response = requests.get("https://catfact.ninja/fact", timeout=10)
            
            if response.status_code == 200:
                data = response.json()
                st.success("✅ Dato obtenido")
                st.info(f"🐱 **Cat Fact**: {data['fact']}")
            else:
                st.error(f"❌ Error: {response.status_code}")
                
        except requests.exceptions.RequestException as e:
            st.error(f"❌ Error: {e}")

# ========================================
# COMPARACIÓN CON PROYECTO FINAL
# ========================================

st.divider()
st.header("🎯 Relación con el Proyecto Final")

st.write("""
En el proyecto final usarás estos mismos conceptos para comunicarte con el agente de seguros:
""")

code_comparison = """
# Ejemplo: API de Clima (este archivo)
response = requests.get(
    f"https://wttr.in/{ciudad}?format=j1",
    timeout=10
)
data = response.json()

# Proyecto Final: Chat con agente
response = requests.post(
    "http://localhost:8000/chat",
    json={
        "message": "¿Qué seguros ofrecen?",
        "thread_id": "user_123"
    },
    timeout=30
)
data = response.json()
mensaje_respuesta = data['response']
"""

st.code(code_comparison, language="python")

st.success("""
✅ **Ya sabes**:
- Hacer GET y POST requests
- Manejar respuestas JSON
- Manejo de errores
- Loading states

¡Estás listo para el proyecto final! 🎉
""")

# ========================================
# DEBUGGING
# ========================================

with st.expander("🔧 Tips de debugging"):
    st.write("""
    **Cómo debuggear APIs**:
    
    1. **Imprime la respuesta completa**:
    ```python
    st.write("Status:", response.status_code)
    st.write("Headers:", response.headers)
    st.json(response.json())
    ```
    
    2. **Usa try/except específicos**:
    ```python
    except requests.exceptions.Timeout:
        st.error("Timeout!")
    except requests.exceptions.ConnectionError:
        st.error("No hay conexión!")
    ```
    
    3. **Verifica la estructura del JSON**:
    ```python
    data = response.json()
    st.write("Keys disponibles:", list(data.keys()))
    ```
    
    4. **Usa herramientas externas**:
    - Postman
    - Thunder Client (VS Code)
    - curl en terminal
    """)
