# 🔧 Guía de Entornos Virtuales - Workshop Dash

## 📋 Resumen

Este workshop requiere **DOS entornos virtuales separados** para evitar conflictos de dependencias entre la API y la aplicación Dash.

---

## 🎯 ¿Por Qué Dos Entornos Virtuales?

La **API del agente de seguros** y la **aplicación Dash** tienen diferentes dependencias:

### API del Agente (`insurance_agent_api/`)
- LangGraph
- LangChain
- FastAPI
- Gemini (langchain-google-genai)
- Uvicorn

### Aplicación Dash (`Dash/`)
- Dash
- dash-bootstrap-components
- requests

**Si instalas todo en un solo entorno**, podrías tener:
- Conflictos de versiones
- Dependencias innecesarias
- Problemas de compatibilidad

---

## 🗂️ Estructura de Directorios

```
FrontEnd_Tools_Workshop/
│
├── insurance_agent_api/
│   ├── venv/                    ← Entorno Virtual #1
│   ├── requirements.txt         ← Dependencias de la API
│   └── app/
│       └── main.py
│
└── Dash/
    ├── venv/                    ← Entorno Virtual #2
    ├── requirements.txt         ← Dependencias de Dash
    └── 3_PLANTILLA_EJERCICIO.py
```

---

## 🚀 Configuración Paso a Paso

### PASO 1: Configurar Entorno de la API

```bash
# Navegar a la carpeta de la API
cd insurance_agent_api

# Crear entorno virtual
python -m venv venv

# Activar el entorno virtual
# En Windows (PowerShell):
venv\Scripts\Activate.ps1
# En Windows (CMD):
venv\Scripts\activate.bat
# En macOS/Linux:
source venv/bin/activate

# Verificar que esté activado (deberías ver "(venv)")
# Prompt debería verse así: (venv) C:\...\insurance_agent_api>

# Instalar dependencias
pip install -r requirements.txt

# Verificar instalación
pip list
```

### PASO 2: Configurar Entorno de Dash

```bash
# Abrir UNA NUEVA TERMINAL
# Navegar a la carpeta Dash
cd Dash

# Crear entorno virtual
python -m venv venv

# Activar el entorno virtual
# En Windows (PowerShell):
venv\Scripts\Activate.ps1
# En Windows (CMD):
venv\Scripts\activate.bat
# En macOS/Linux:
source venv/bin/activate

# Verificar que esté activado (deberías ver "(venv)")
# Prompt debería verse así: (venv) C:\...\Dash>

# Instalar dependencias
pip install -r requirements.txt

# Verificar instalación
pip list
```

---

## 💻 Uso Durante el Workshop

### Terminal 1: API Server
```bash
# Activar venv de la API
cd insurance_agent_api
source venv/bin/activate  # Windows: venv\Scripts\Activate.ps1

# Iniciar el servidor
cd app
python main.py

# Esta terminal debe permanecer abierta
# Verás logs de las peticiones que lleguen a la API
```

### Terminal 2: Aplicación Dash
```bash
# Activar venv de Dash
cd Dash
source venv/bin/activate  # Windows: venv\Scripts\Activate.ps1

# Trabajar en tu aplicación
python 3_PLANTILLA_EJERCICIO.py

# O ejecutar tests
python test_api.py

# Esta es tu terminal de trabajo principal
```

---

## ✅ Verificación

### ¿Cómo saber si estoy en el entorno correcto?

**Método 1: Ver el prompt**
```bash
# Si ves (venv) al inicio, el entorno está activado
(venv) C:\...\Dash>

# Si NO ves (venv), el entorno NO está activado
C:\...\Dash>
```

**Método 2: Verificar paquetes instalados**
```bash
# En el venv de la API, deberías ver:
pip list | grep fastapi
# Resultado: fastapi  0.104.0

# En el venv de Dash, deberías ver:
pip list | grep dash
# Resultado: dash  2.14.0
```

**Método 3: Verificar ruta de Python**
```bash
# En Windows (PowerShell):
Get-Command python | Select-Object Source

# En macOS/Linux:
which python

# Debería apuntar a:
# API: .../insurance_agent_api/venv/...
# Dash: .../Dash/venv/...
```

---

## 🔄 Reactivar Entornos

Cada vez que cierres y reabras una terminal, necesitas **reactivar** el entorno virtual:

### Reactivar API
```bash
cd insurance_agent_api
# Windows PowerShell:
venv\Scripts\Activate.ps1
# Windows CMD:
venv\Scripts\activate.bat
# macOS/Linux:
source venv/bin/activate
```

### Reactivar Dash
```bash
cd Dash
# Windows PowerShell:
venv\Scripts\Activate.ps1
# Windows CMD:
venv\Scripts\activate.bat
# macOS/Linux:
source venv/bin/activate
```

---

## ❌ Errores Comunes y Soluciones

### Error 1: "ModuleNotFoundError: No module named 'dash'"

**Causa**: Estás en el entorno virtual equivocado o no está activado.

**Solución**:
```bash
# Verificar que estés en la carpeta correcta
pwd  # Deberías estar en .../Dash

# Activar el entorno de Dash
source venv/bin/activate  # o venv\Scripts\Activate.ps1

# Verificar que dash esté instalado
pip list | grep dash
```

### Error 2: "ModuleNotFoundError: No module named 'langchain'"

**Causa**: Estás en el entorno de Dash pero necesitas el de la API.

**Solución**:
```bash
# Desactivar el entorno actual
deactivate

# Navegar a la API
cd ../insurance_agent_api

# Activar el entorno de la API
source venv/bin/activate  # o venv\Scripts\Activate.ps1
```

### Error 3: Instalé un paquete pero no lo encuentra

**Causa**: Instalaste en un entorno pero estás ejecutando en otro.

**Solución**:
```bash
# Verificar en qué entorno estás
which python  # o Get-Command python en PowerShell

# Si es el incorrecto, desactivar y activar el correcto
deactivate
cd ../[carpeta-correcta]
source venv/bin/activate
```

### Error 4: No puedo activar el entorno en Windows PowerShell

**Causa**: Política de ejecución de scripts restrictiva.

**Solución**:
```powershell
# Ejecutar como administrador (una sola vez):
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser

# Luego activar normalmente:
venv\Scripts\Activate.ps1
```

---

## 💡 Tips y Mejores Prácticas

### Tip 1: Nombra tus Ventanas de Terminal
Muchos terminales permiten renombrar las pestañas:
- **Terminal 1**: "API Server"
- **Terminal 2**: "Dash App"

### Tip 2: Usa alias (macOS/Linux)
```bash
# En tu ~/.bashrc o ~/.zshrc:
alias api-activate='cd ~/path/to/insurance_agent_api && source venv/bin/activate'
alias dash-activate='cd ~/path/to/Dash && source venv/bin/activate'
```

### Tip 3: Verifica antes de instalar
```bash
# Antes de hacer pip install, verifica que estés en el entorno correcto
echo "Estoy en: $(pwd)"
which python
```

### Tip 4: Mantén las terminales abiertas
Durante el workshop, mantén ambas terminales abiertas:
- Una con la API corriendo
- Otra para trabajar en Dash

### Tip 5: Usa un IDE que soporte múltiples terminales
Editores como VS Code permiten tener varias terminales integradas en la misma ventana.

---

## 🧹 Limpieza (Después del Workshop)

Si quieres eliminar los entornos virtuales:

```bash
# Desactivar primero
deactivate

# Eliminar venv de la API
rm -rf insurance_agent_api/venv  # o en Windows: rmdir /s insurance_agent_api\venv

# Eliminar venv de Dash
rm -rf Dash/venv  # o en Windows: rmdir /s Dash\venv
```

**Nota**: Los archivos .gitignore ya están configurados para no subir los venv a Git.

---

## 📚 Recursos Adicionales

### Documentación Oficial de venv
- https://docs.python.org/3/library/venv.html

### Guías de Entornos Virtuales
- https://realpython.com/python-virtual-environments-a-primer/
- https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/

### Alternativas a venv
Si tienes problemas con venv, puedes usar:
- **virtualenv**: `pip install virtualenv && virtualenv venv`
- **conda**: `conda create -n dash-env python=3.10`
- **poetry**: Gestor de dependencias moderno

---

## 🎯 Checklist de Configuración

Antes de empezar el workshop, verifica que:

- [ ] Python 3.10+ está instalado
- [ ] pip está actualizado: `pip install --upgrade pip`
- [ ] Puedes crear entornos virtuales: `python -m venv test_venv`
- [ ] Tienes permisos para ejecutar scripts (Windows)
- [ ] Tienes 2 ventanas de terminal disponibles
- [ ] Entorno de API creado y funcionando
- [ ] Entorno de Dash creado y funcionando
- [ ] API responde correctamente: `python test_api.py`

---

**¡Estás listo para el workshop! 🚀**

Si tienes problemas con los entornos virtuales, consulta la sección de errores comunes o pregunta al instructor.

---

*Guía de Entornos Virtuales - Workshop de Herramientas Frontend con IA*

