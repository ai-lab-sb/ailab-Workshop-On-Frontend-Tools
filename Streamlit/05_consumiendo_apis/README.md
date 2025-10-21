# 05 - Consumiendo APIs

## 📖 ¿Qué aprenderás?

En esta lección aprenderás a consumir APIs REST desde Streamlit, preparándote para integrar el agente de seguros en el proyecto final.

## 🎯 Temas cubiertos:

1. Hacer requests HTTP con `requests`
2. GET y POST requests
3. Procesar respuestas JSON
4. Manejo de errores
5. Loading states y feedback al usuario

## 📝 Aplicaciones de esta lección:

### `05-01_app_api_simple.py`
Conceptos básicos de requests HTTP (GET y POST).

**Ejecutar:**
```bash
streamlit run 05-01_app_api_simple.py
```

### `05-02_app_weather_api.py`
Ejemplo práctico consumiendo una API pública de clima.

**Ejecutar:**
```bash
streamlit run 05-02_app_weather_api.py
```

## 💡 Conceptos Clave

### 1. La librería requests
```python
import requests

# GET request
response = requests.get("https://api.example.com/data")
data = response.json()

# POST request
response = requests.post(
    "https://api.example.com/submit",
    json={"key": "value"}
)
```

### 2. Manejo de respuestas
```python
if response.status_code == 200:
    data = response.json()
    st.success("Éxito!")
else:
    st.error(f"Error: {response.status_code}")
```

### 3. Loading states
```python
with st.spinner("Cargando..."):
    response = requests.get(url)
```

## 🎨 Métodos HTTP principales:

| Método | Uso | Ejemplo |
|--------|-----|---------|
| GET | Obtener datos | Consultar historial de chat |
| POST | Enviar datos | Enviar mensaje al agente |
| PUT | Actualizar datos | Actualizar perfil |
| DELETE | Eliminar datos | Borrar conversación |

## 🏋️ Ejercicio Práctico

Crea una app que:

1. Haga un GET a una API pública (ej: JSONPlaceholder)
2. Muestre los datos en una tabla
3. Permita filtrar los resultados
4. Tenga manejo de errores apropiado

## ⚠️ Buenas Prácticas

### 1. Siempre maneja errores
```python
try:
    response = requests.get(url, timeout=10)
    response.raise_for_status()
except requests.exceptions.RequestException as e:
    st.error(f"Error: {e}")
```

### 2. Usa timeout
```python
requests.get(url, timeout=10)  # 10 segundos máximo
```

### 3. Muestra feedback al usuario
```python
with st.spinner("Procesando..."):
    response = requests.post(url, json=data)

if response.ok:
    st.success("✅ Éxito")
else:
    st.error("❌ Error")
```

## 🎯 Para el Proyecto Final

Usaremos estas técnicas para:
- **POST** a `/chat` para enviar mensajes
- **GET** a `/history/{thread_id}` para obtener historial
- Manejo de errores cuando el API no esté disponible
- Loading states mientras esperamos respuesta

## 📚 APIs para practicar

- [JSONPlaceholder](https://jsonplaceholder.typicode.com/) - API fake para testing
- [OpenWeather](https://openweathermap.org/api) - API de clima
- [CatFacts](https://catfact.ninja/) - Datos sobre gatos
- [PokeAPI](https://pokeapi.co/) - Datos de Pokémon

## ➡️ Siguiente Paso

¡Ya estás listo para el [Proyecto Final](../06_proyecto_final/)!
