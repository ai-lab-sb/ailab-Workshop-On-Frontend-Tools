# 04 - Estado y Sesión

## 📖 ¿Qué aprenderás?

En esta lección aprenderás sobre **Session State**, el concepto más importante para crear aplicaciones interactivas con memoria en Streamlit.

## 🎯 Temas cubiertos:

1. ¿Qué es Session State y por qué es importante?
2. Cómo usar st.session_state
3. Mantener valores entre re-ejecuciones
4. Callbacks y actualización de estado
5. Gestión de estado complejo

## 📝 Aplicaciones de esta lección:

### `04-01_app_session_state.py`
Introducción a Session State con ejemplos básicos.

**Ejecutar:**
```bash
streamlit run 04-01_app_session_state.py
```

### `04-02_app_contador.py`
Ejemplo práctico: un contador que funciona correctamente usando Session State.

**Ejecutar:**
```bash
streamlit run 04-02_app_contador.py
```

## 💡 Concepto Clave: ¿Por qué Session State?

### ❌ El Problema
```python
contador = 0  # Esto se reinicia cada vez!
if st.button("Incrementar"):
    contador += 1  # Nunca funciona
st.write(contador)  # Siempre muestra 0
```

**Streamlit ejecuta tu script de arriba hacia abajo cada vez que hay una interacción.**
Todas las variables se reinician.

### ✅ La Solución: Session State
```python
if "contador" not in st.session_state:
    st.session_state.contador = 0

if st.button("Incrementar"):
    st.session_state.contador += 1  # ¡Funciona!
    
st.write(st.session_state.contador)  # Mantiene el valor
```

## 🎨 Operaciones con Session State:

| Operación | Código |
|-----------|--------|
| Inicializar | `st.session_state.variable = valor` |
| Leer | `valor = st.session_state.variable` |
| Actualizar | `st.session_state.variable = nuevo_valor` |
| Verificar existencia | `if "variable" in st.session_state:` |
| Eliminar | `del st.session_state.variable` |

## 🏋️ Ejercicio Práctico

Crea una app de "carrito de compras" que:

1. Muestre una lista de seguros
2. Permita agregar seguros al carrito (Session State)
3. Muestre el total acumulado
4. Permita vaciar el carrito

## ⚡ Casos de Uso Importantes

Session State es **esencial** para:

- ✅ **Chat conversacional** (historial de mensajes)
- ✅ Contadores, scores, puntuaciones
- ✅ Carrito de compras
- ✅ Formularios de varios pasos
- ✅ Autenticación de usuarios
- ✅ Filtros que persisten entre páginas

## 🎯 Para el Proyecto Final

Session State será **crítico** para:
- Mantener el historial del chat
- Almacenar el thread_id actual
- Guardar mensajes del usuario y del agente
- Gestionar múltiples conversaciones

## ➡️ Siguiente Paso

Continúa con [05_consumiendo_apis](../05_consumiendo_apis/)
