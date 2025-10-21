# 📊 Módulo Dash - Workshop de Herramientas Frontend con IA

¡Bienvenido al módulo de Dash! Aquí aprenderás a construir aplicaciones web interactivas usando 100% Python.

---

## 📚 Estructura del Módulo

Este módulo está diseñado para seguirse de forma **lineal y secuencial**. Los archivos están numerados para guiarte paso a paso:

### **📖 Documentación (Leer en orden)**

1. **`LEEME.md`** ⭐ **[EMPEZAR AQUÍ]**
   - Guía de inicio rápido
   - Flujo completo del workshop
   - Qué hacer paso a paso

2. **`1_INTRODUCCION_DASH.md`**
   - ¿Qué es Dash?
   - Conceptos fundamentales
   - Componentes y arquitectura
   - Ejemplos básicos

3. **`2_GUIA_EJERCICIO.md`**
   - Pasos detallados del ejercicio
   - Código de ejemplo para cada sección
   - Lista de verificación
   - Solución de problemas

### **💻 Código (Usar en orden)**

4. **`3_PLANTILLA_EJERCICIO.py`** 🎯 **[TU TRABAJO]**
   - Plantilla con TODOs para completar
   - Estructura básica lista
   - Comentarios guía en español

5. **`4_SOLUCION_COMPLETA.py`** ✅ **[REFERENCIA]**
   - Solución completa del ejercicio
   - Código producción-ready
   - Comentarios detallados

6. **`5_REFERENCIA_CODIGO.py`** 📚 **[SNIPPETS]**
   - Ejemplos de código copiables
   - Patrones comunes
   - Referencia rápida

### **🛠️ Herramientas**

- **`test_api.py`** - Verificar conexión con la API
- **`requirements.txt`** - Dependencias del proyecto
- **`assets/custom.css`** - Estilos personalizados

---

## 🚀 Inicio Rápido (5 Pasos)

### Paso 1: Configurar Entorno Virtual de la API
```bash
# Navegar a la carpeta de la API
cd insurance_agent_api

# Crear entorno virtual para la API
python -m venv venv

# Activar entorno virtual
# En Windows (PowerShell):
venv\Scripts\Activate.ps1

# En Windows (CMD):
venv\Scripts\activate.bat

# En macOS/Linux:
source venv/bin/activate

# Instalar dependencias de la API
pip install -r requirements.txt
```

### Paso 2: Configurar Entorno Virtual de Dash
```bash
# Navegar a la carpeta Dash (desde la raíz del proyecto)
cd ../Dash

# Crear entorno virtual para Dash
python -m venv venv

# Activar entorno virtual
# En Windows (PowerShell):
venv\Scripts\Activate.ps1

# En Windows (CMD):
venv\Scripts\activate.bat

# En macOS/Linux:
source venv/bin/activate

# Instalar dependencias de Dash
pip install -r requirements.txt
```

### Paso 3: Iniciar la API
```bash
# En una terminal (con venv de API activado)
cd insurance_agent_api/app
python main.py
```

### Paso 4: Verificar Conexión
```bash
# En otra terminal (con venv de Dash activado)
cd Dash
python test_api.py
```

### Paso 5: Empezar el Workshop
```bash
# En la terminal con venv de Dash activado
# Leer la documentación
cat LEEME.md
cat 1_INTRODUCCION_DASH.md
cat 2_GUIA_EJERCICIO.md

# Comenzar a programar
python 3_PLANTILLA_EJERCICIO.py
# Abre http://localhost:8050 en tu navegador
```

**Nota Importante**: Necesitarás **2 terminales abiertas** durante el workshop:
- **Terminal 1**: Con venv de la API activado (corriendo `python main.py`)
- **Terminal 2**: Con venv de Dash activado (corriendo tu aplicación Dash)

---

## 🎯 ¿Qué Vas a Construir?

Una **interfaz de chat profesional** para SegurosVida+ que incluye:

✅ Chat interactivo con agente de IA  
✅ Historial de conversación  
✅ Indicador de estado de API  
✅ Diseño responsive y profesional  
✅ Manejo de errores robusto  

**Vista previa:**
```
┌─────────────────────────────────────┐
│  🏥 SegurosVida+  [●Conectado]      │
├─────────────────────────────────────┤
│ 14:30  Usuario:                     │
│        ¿Qué seguros ofrecen?      ► │
│                                      │
│ 14:31  ◄ Agente:                    │
│        Ofrecemos 5 tipos...          │
│                                      │
│ [Escribe tu pregunta aquí...]       │
│ [       Botón Enviar       ]        │
└─────────────────────────────────────┘
```

---

## ⏱️ Tiempo Estimado

| Actividad | Tiempo |
|-----------|--------|
| Lectura de documentación | 60-80 min |
| Configuración | 10-15 min |
| Implementación | 90-120 min |
| Funcionalidades bonus | 30-60 min |
| **TOTAL** | **3-4 horas** |

---

## 📖 Flujo de Aprendizaje Recomendado

```
1️⃣ LEEME.md (10 min)
   ↓
2️⃣ 1_INTRODUCCION_DASH.md (30-40 min)
   ↓
3️⃣ Configuración: pip install + test_api.py (10 min)
   ↓
4️⃣ 2_GUIA_EJERCICIO.md (15-20 min)
   ↓
5️⃣ 3_PLANTILLA_EJERCICIO.py (90-120 min) ⭐
   ├── Consultar: 5_REFERENCIA_CODIGO.py
   └── Si te atascas: 2_GUIA_EJERCICIO.md
   ↓
6️⃣ Verificar y Probar (15 min)
   ↓
7️⃣ Comparar con 4_SOLUCION_COMPLETA.py (20 min)
   ↓
8️⃣ Funcionalidades Bonus (opcional, 30-60 min)
```

---

## 🎓 Lo Que Aprenderás

### Conceptos de Dash
- ✅ Estructura de una aplicación Dash
- ✅ Componentes: html, dcc, dbc
- ✅ Sistema de callbacks
- ✅ Manejo de estado con dcc.Store

### Desarrollo Web con Python
- ✅ Layouts responsivos con Bootstrap
- ✅ Integración con APIs REST
- ✅ Manejo de errores y estados de carga
- ✅ UX/UI profesional

### Mejores Prácticas
- ✅ Organización de código
- ✅ Patrones de diseño
- ✅ Performance y optimización
- ✅ Debugging y testing

---

## 📋 Requisitos Previos

Antes de comenzar, asegúrate de tener:

- ✅ Python 3.10 o superior instalado
- ✅ pip (gestor de paquetes de Python)
- ✅ Capacidad de crear entornos virtuales (venv)
- ✅ Archivo `.env` con `GOOGLE_API_KEY` en `insurance_agent_api/`
- ✅ Conocimientos básicos de Python
- ✅ Navegador web moderno
- ✅ **Capacidad de tener 2 terminales abiertas simultáneamente**

### ⚠️ Importante: Dos Entornos Virtuales

Este workshop requiere **DOS entornos virtuales separados**:

1. **Entorno Virtual de la API** (`insurance_agent_api/venv/`)
   - Para las dependencias del agente de seguros
   - LangGraph, LangChain, FastAPI, etc.

2. **Entorno Virtual de Dash** (`Dash/venv/`)
   - Para las dependencias de la aplicación Dash
   - Dash, dash-bootstrap-components, requests

**Por qué dos entornos**: La API y Dash tienen diferentes dependencias que podrían conflictuar si se instalaran en el mismo entorno virtual.

---

## 🆘 ¿Necesitas Ayuda?

### Orden de consulta recomendado:

1. **`2_GUIA_EJERCICIO.md`** - Pasos detallados con código
2. **`5_REFERENCIA_CODIGO.py`** - Snippets copiables
3. **`1_INTRODUCCION_DASH.md`** - Conceptos fundamentales
4. **`4_SOLUCION_COMPLETA.py`** - Solución completa (último recurso)

### Problemas Comunes:

**❌ Error al crear el entorno virtual**
```bash
# Si python -m venv no funciona, intenta:
python3 -m venv venv

# O instala python-venv:
# En Ubuntu/Debian:
sudo apt-get install python3-venv

# En macOS (con Homebrew):
brew install python
```

**❌ El entorno virtual no se activa**
```bash
# Windows PowerShell (si hay error de permisos):
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser

# Luego intenta activar nuevamente:
venv\Scripts\Activate.ps1
```

**❌ Comando no encontrado después de instalar**
```bash
# Asegúrate de que el entorno virtual CORRECTO esté activado
# Deberías ver (venv) al inicio de tu prompt
# Si no lo ves, activa el entorno virtual nuevamente
```

**❌ Confusión entre los dos entornos virtuales**
```bash
# ERROR COMÚN: Activar el venv equivocado en la terminal equivocada

# ✅ CORRECTO:
# Terminal 1 (API):
cd insurance_agent_api
source venv/bin/activate  # o venv\Scripts\Activate.ps1 en Windows
python app/main.py

# Terminal 2 (Dash):
cd Dash
source venv/bin/activate  # o venv\Scripts\Activate.ps1 en Windows
python 3_PLANTILLA_EJERCICIO.py

# TIP: Puedes renombrar las ventanas de tu terminal para identificarlas:
# - Terminal 1 → "API Server"
# - Terminal 2 → "Dash App"
```

**❌ La API no se conecta**
```bash
# Verificar que esté corriendo
python test_api.py

# Si falla, iniciar la API
cd ../insurance_agent_api/app
python main.py
```

**❌ El callback no se ejecuta**
- Verifica que los IDs coincidan exactamente
- Usa `prevent_initial_call=True` cuando corresponda
- Revisa la consola de Python para errores

**❌ Los mensajes no se muestran**
- Inspecciona el historial con `print(historial)`
- Abre DevTools del navegador (F12) > Console
- Verifica la estructura de datos del Store

---

## 🌟 Funcionalidades Bonus

Una vez que completes el ejercicio básico, intenta agregar:

- [ ] Botones con preguntas de ejemplo
- [ ] Enviar mensaje presionando Enter (requiere cambiar a `dcc.Input`)
- [ ] Timestamps en cada mensaje
- [ ] Spinner de carga
- [ ] Auto-scroll al último mensaje
- [ ] Markdown en respuestas del agente
- [ ] Mejoras visuales personalizadas
- [ ] Contador de caracteres en el input
- [ ] Historial exportable a archivo

---

## 📊 Estructura de Archivos

```
Dash/
├── LEEME.md                        # ⭐ Inicio rápido
├── 1_INTRODUCCION_DASH.md          # 📖 Conceptos
├── 2_GUIA_EJERCICIO.md             # 📖 Pasos detallados
├── 3_PLANTILLA_EJERCICIO.py        # 🎯 Tu trabajo
├── 4_SOLUCION_COMPLETA.py          # ✅ Referencia
├── 5_REFERENCIA_CODIGO.py          # 📚 Snippets
├── test_api.py                     # 🧪 Testing
├── requirements.txt                # 📦 Dependencias
├── assets/
│   └── custom.css                  # 🎨 Estilos
└── __init__.py
```

---

## 🎯 Criterios de Éxito

Has completado el módulo exitosamente cuando:

- [x] Entiendes los conceptos básicos de Dash
- [x] Tu aplicación se conecta a la API correctamente
- [x] Puedes enviar y recibir mensajes
- [x] El historial se muestra correctamente
- [x] La interfaz es profesional y funcional
- [x] Has implementado al menos 2 funcionalidades bonus

---

## 📚 Recursos Adicionales

### Documentación Oficial
- [Dash Documentation](https://dash.plotly.com/)
- [Dash Bootstrap Components](https://dash-bootstrap-components.opensource.faculty.ai/)
- [Plotly Python](https://plotly.com/python/)

### Comunidad
- [Dash Community Forum](https://community.plotly.com/)
- [GitHub - plotly/dash](https://github.com/plotly/dash)
- [Stack Overflow - dash](https://stackoverflow.com/questions/tagged/plotly-dash)

### Tutoriales
- [Official Tutorial](https://dash.plotly.com/tutorial)
- [Gallery of Examples](https://dash.gallery/Portal/)
- [Cheatsheet](https://dashcheatsheet.pythonanywhere.com/)

---

## 💡 Tips para el Workshop

1. **Lee la documentación primero** - No te saltes `1_INTRODUCCION_DASH.md`
2. **Sigue el orden** - Los archivos están numerados por una razón
3. **Prueba frecuentemente** - Ejecuta tu código después de cada sección
4. **Usa la referencia** - `5_REFERENCIA_CODIGO.py` tiene snippets útiles
5. **No copies ciegamente** - Entiende qué hace cada línea
6. **Experimenta** - Cambia colores, textos, layouts
7. **Pide ayuda** - Si te atascas más de 15 min, consulta la guía

---

## 🎉 ¡Comienza Ahora!

**👉 Tu próximo paso:** Abre `LEEME.md` y comienza el workshop.

```bash
cat LEEME.md
```

O si prefieres leerlo en tu editor de código, ábrelo y sigue las instrucciones.

---

## 📞 Soporte

Si tienes preguntas durante el workshop:
1. Consulta la documentación en orden
2. Usa los archivos de referencia
3. Lee los mensajes de error cuidadosamente
4. Pregunta al instructor o compañeros

---

**¡Buena suerte y disfruta construyendo con Dash! 🚀**

---

*Versión: 1.0 | Workshop de Herramientas Frontend con IA*  
*Última actualización: Octubre 2025*

