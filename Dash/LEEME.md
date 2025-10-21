# 📊 Módulo Dash - Workshop de Herramientas Frontend con IA

## 🚀 Inicio Rápido

Bienvenido al módulo de **Dash** del workshop. Este módulo te enseñará a construir aplicaciones web interactivas usando Python.

### 🎯 Objetivo del Workshop

Construirás una **interfaz de chat profesional** para el agente de seguros SegurosVida+ usando Dash.

---

## 📚 Estructura del Workshop (Flujo Lineal)

Sigue estos archivos **en orden** para completar el workshop:

### **Paso 1: Preparación**
📄 **Archivo:** `1_INTRODUCCION_DASH.md`  
⏱️ **Tiempo:** 30-40 minutos  
📖 **Contenido:** 
- ¿Qué es Dash?
- Conceptos fundamentales
- Componentes y arquitectura
- Primeros ejemplos

👉 **Lee este archivo primero** para entender los conceptos básicos de Dash.

---

### **Paso 2: Configuración del Entorno**
🔧 **Acción:** Crear entornos virtuales, instalar dependencias y verificar API

**⚠️ IMPORTANTE**: Necesitas crear **DOS entornos virtuales separados**:
- Uno para la API del agente (tiene sus propias dependencias)
- Otro para la aplicación Dash (tiene diferentes dependencias)

```bash
# === PARTE A: Configurar la API ===

# 1. Navegar a la carpeta de la API
cd insurance_agent_api

# 2. Crear entorno virtual para la API
python -m venv venv

# 3. Activar el entorno virtual de la API:
# En Windows (PowerShell):
venv\Scripts\Activate.ps1
# En Windows (CMD):
venv\Scripts\activate.bat
# En macOS/Linux:
source venv/bin/activate

# 4. Instalar dependencias de la API (con venv activado)
pip install -r requirements.txt

# === PARTE B: Configurar Dash ===

# 5. Abrir OTRA TERMINAL y navegar a la carpeta Dash
cd Dash

# 6. Crear entorno virtual para Dash
python -m venv venv

# 7. Activar el entorno virtual de Dash:
# En Windows (PowerShell):
venv\Scripts\Activate.ps1
# En Windows (CMD):
venv\Scripts\activate.bat
# En macOS/Linux:
source venv/bin/activate

# 8. Instalar dependencias de Dash (con venv activado)
pip install -r requirements.txt

# === PARTE C: Iniciar y Verificar ===

# 9. En la TERMINAL 1 (con venv de API), iniciar la API:
cd insurance_agent_api/app

** Asegurate de haber configurado la GOOGLE_API_KEY **
** Lee \insurance_agent_api\README.md**

python main.py

# 10. En la TERMINAL 2 (con venv de Dash), verificar conexión:
cd Dash
python test_api.py
```

✅ **Checkpoint:** Debes ver el mensaje "✅ Todas las pruebas pasaron exitosamente!"

**💡 Nota**: Durante todo el workshop necesitarás **2 terminales abiertas**:
- **Terminal 1**: API corriendo (con su venv activado)
- **Terminal 2**: Tu aplicación Dash (con su venv activado)

---

### **Paso 3: Guía del Ejercicio**
📄 **Archivo:** `2_GUIA_EJERCICIO.md`  
⏱️ **Tiempo:** 15-20 minutos  
📖 **Contenido:**
- Pasos detallados para completar el ejercicio
- Código de ejemplo para cada sección
- Lista de verificación
- Consejos y trucos

👉 **Consulta esta guía** mientras trabajas en el ejercicio.

---

### **Paso 4: Implementación (¡Tu Turno!)**
💻 **Archivo:** `3_PLANTILLA_EJERCICIO.py`  
⏱️ **Tiempo:** 90-120 minutos  
📝 **Qué harás:**
- Completar las funciones marcadas con `# TODO`
- Implementar el layout de la aplicación
- Crear los callbacks de interactividad
- Probar tu aplicación

```bash
# Ejecutar tu aplicación
python 3_PLANTILLA_EJERCICIO.py
# Abre http://localhost:8050 en tu navegador
```

💡 **Ayuda disponible:**
- `5_REFERENCIA_CODIGO.py` - Ejemplos de código para copiar
- `2_GUIA_EJERCICIO.md` - Guía paso a paso
- `4_SOLUCION_COMPLETA.py` - Solución completa (último recurso)

---

### **Paso 5: Verificación**
✅ **Prueba tu aplicación con estas preguntas:**
1. "¿Qué tipos de seguros ofrecen?"
2. "¿Cuánto cuesta el seguro de auto?"
3. "¿Tienen cobertura internacional?"
4. "Quiero un seguro para mi casa"

✅ **Verifica que funcione:**
- [ ] Los mensajes se envían y reciben correctamente
- [ ] El historial se muestra en pantalla
- [ ] El indicador de estado de la API funciona
- [ ] Los errores se manejan apropiadamente
- [ ] La interfaz es clara y profesional

---

### **Paso 6: Comparar con la Solución**
📄 **Archivo:** `4_SOLUCION_COMPLETA.py`  
⏱️ **Tiempo:** 20-30 minutos  
📖 **Qué hacer:**
- Compara tu implementación con la solución
- Identifica mejoras posibles
- Implementa funcionalidades bonus

```bash
# Ver la solución funcionando
python 4_SOLUCION_COMPLETA.py
# Abre http://localhost:8050 en tu navegador
```

---

### **Paso 7: Funcionalidades Bonus (Opcional)**
🌟 **Si terminas antes, intenta agregar:**
- [ ] Botones con preguntas de ejemplo
- [ ] Enviar mensaje presionando Enter (requiere cambiar a `dcc.Input`)
- [ ] Timestamps en cada mensaje (ya implementados en solución)
- [ ] Spinner de carga mientras espera respuesta (ya implementado)
- [ ] Auto-scroll al último mensaje
- [ ] Formato markdown en las respuestas (ya implementado)
- [ ] Mejoras visuales en el diseño
- [ ] Contador de caracteres
- [ ] Limpiar historial con un botón

---

## 📖 Archivos de Referencia

### Durante el Desarrollo:

**`5_REFERENCIA_CODIGO.py`**
- Snippets de código listos para usar
- Ejemplos de componentes
- Patrones de callbacks
- Código de manejo de APIs

**`test_api.py`**
- Herramienta para verificar la conexión con la API
- Ejecutar cuando tengas problemas de conexión

---

## 🎓 Lo Que Aprenderás

Al completar este módulo, sabrás:

✅ **Conceptos de Dash:**
- Estructura de una aplicación Dash
- Sistema de componentes (html, dcc, dbc)
- Callbacks e interactividad

✅ **Desarrollo Web con Python:**
- Layouts responsivos con Bootstrap
- Manejo de estado en el cliente
- Integración con APIs REST

✅ **Mejores Prácticas:**
- Organización de código
- Manejo de errores
- UX/UI profesional

---

## ⏱️ Tiempo Estimado

| Actividad | Tiempo |
|-----------|--------|
| Lectura de introducción | 30-40 min |
| Configuración | 10-15 min |
| Lectura de guía | 15-20 min |
| Implementación | 90-120 min |
| Funcionalidades bonus | 30-60 min |
| **TOTAL** | **3-4 horas** |

---

## 🆘 ¿Problemas?

### La API no se conecta
```bash
# Verifica que la API esté corriendo
curl http://localhost:8000/health
# O en Windows PowerShell:
Invoke-WebRequest http://localhost:8000/health
```

### El código no funciona
1. Lee los mensajes de error en la terminal
2. Verifica que los IDs de los componentes coincidan
3. Consulta `5_REFERENCIA_CODIGO.py` para ejemplos
4. Revisa `2_GUIA_EJERCICIO.md` para ayuda específica

### ¿Dónde pedir ayuda?
- Consulta primero `2_GUIA_EJERCICIO.md`
- Revisa `5_REFERENCIA_CODIGO.py` para ejemplos
- Como último recurso, mira `4_SOLUCION_COMPLETA.py`

---

## 📋 Requisitos Previos

- ✅ Python 3.10 o superior instalado
- ✅ API del agente de seguros configurada
- ✅ Archivo `.env` con `GOOGLE_API_KEY` configurado
- ✅ Conocimientos básicos de Python

---

## 🎯 Criterios de Éxito

Has completado exitosamente el módulo cuando:

- [x] Entiendes los conceptos básicos de Dash
- [x] Tu aplicación se conecta a la API correctamente
- [x] Puedes enviar y recibir mensajes
- [x] El historial se muestra correctamente
- [x] La interfaz es profesional y funcional
- [x] Has implementado al menos 2 funcionalidades bonus

---

## 🚀 ¿Listo para Empezar?

**👉 Comienza leyendo:** `1_INTRODUCCION_DASH.md`

**Luego sigue el flujo lineal:**
```
1_INTRODUCCION_DASH.md
    ↓
Configuración (pip install + test_api.py)
    ↓
2_GUIA_EJERCICIO.md
    ↓
3_PLANTILLA_EJERCICIO.py (TU TRABAJO)
    ↓
Verificación y pruebas
    ↓
4_SOLUCION_COMPLETA.py (comparación)
    ↓
Funcionalidades bonus
```

---

## 📞 Soporte

Si tienes dudas durante el workshop:
1. Consulta la documentación en orden
2. Usa los archivos de referencia
3. Lee los mensajes de error cuidadosamente
4. Pregunta al instructor

---

**¡Buena suerte y disfruta construyendo con Dash! 🎉**

---

*Versión: 1.0 | Workshop de Herramientas Frontend con IA*

