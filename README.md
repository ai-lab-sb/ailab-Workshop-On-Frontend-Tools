# 🚀 Frontend Tools Workshop - AI-Powered Applications

Repositorio del **Workshop de Herramientas Frontend con IA**, donde aprenderás a construir aplicaciones interactivas modernas utilizando diferentes herramientas y frameworks, todo conectado con inteligencia artificial.

---

## 📋 Descripción General

Este workshop está diseñado para enseñarte cómo construir interfaces de usuario modernas y conectarlas con agentes de IA conversacionales. A través de diferentes módulos, explorarás distintas herramientas y frameworks, cada uno con su propio enfoque y ventajas.

**Objetivo Principal**: Crear aplicaciones de chat interactivas que se conecten con un agente de seguros potenciado por IA (Gemini 2.5 Flash), permitiéndote comparar y contrastar diferentes enfoques de desarrollo frontend.

---

## 🗂️ Estructura del Repositorio

### 🤖 Backend - API del Agente de IA

#### [`insurance_agent_api/`](./insurance_agent_api)
API conversacional con memoria construida con **LangGraph** y **FastAPI**.

**Características**:
- ✅ Agente especializado en seguros (vida, auto, hogar, salud, viaje)
- ✅ Memoria persistente por conversación
- ✅ Powered by Google Gemini 2.5 Flash
- ✅ Endpoints REST documentados

**👉 [Ver documentación completa](./insurance_agent_api/README.md)**

---

### 🎨 Frontend - Módulos del Workshop

Cada módulo te enseña a construir la misma aplicación de chat usando diferentes herramientas:

#### 1️⃣ [`Dash/`](./Dash) - Python Full Stack
Framework Python para crear aplicaciones web reactivas sin escribir JavaScript.

**Ideal para**:
- Data scientists y analistas
- Desarrolladores Python
- Aplicaciones de dashboards y visualización

**Stack**: Python + Plotly Dash + Bootstrap Components

**👉 [Comenzar con Dash](./Dash/README.md)**

---

#### 2️⃣ [`Streamlit/`](./Streamlit) - Rapid Prototyping
Framework Python para crear aplicaciones web con código mínimo.

**Ideal para**:
- Prototipos rápidos
- MVP y demos
- Scripts interactivos
- Data scientists y ML engineers

**Stack**: Python + Streamlit + Session State

**Incluye**:
- ✅ 6 lecciones progresivas (de básico a avanzado)
- ✅ 15+ aplicaciones de ejemplo documentadas
- ✅ Proyecto final en 4 pasos (chat con IA)
- ✅ Guías completas con conceptos y ejercicios

**👉 [Comenzar con Streamlit](./Streamlit/README.md)**

---

#### 3️⃣ [`Cursor/`](./Cursor) - AI-Assisted Development
Desarrollo asistido por IA usando Cursor IDE.

**Ideal para**:
- Acelerar el desarrollo
- Aprender nuevas tecnologías
- Pair programming con IA

**Stack**: Cursor AI + tu framework favorito

**👉 [Comenzar con Cursor](./Cursor/)** *(próximamente)*

---

#### 4️⃣ [`Lovable/`](./Lovable) - No-Code AI Builder
Constructor visual de aplicaciones con IA.

**Ideal para**:
- Prototipos sin código
- Diseñadores y product managers
- Iteración rápida de UI/UX

**Stack**: Lovable.dev Platform

**👉 [Comenzar con Lovable](./Lovable/)** *(próximamente)*

---

## 🚀 Inicio Rápido

### 1. Clonar el Repositorio

```bash
git clone <url-del-repositorio>
cd FrontEnd_Tools_Workshop
```

### 2. Configurar el Backend (Requerido)

El backend es necesario para todos los módulos:

```bash
cd insurance_agent_api
pip install -r requirements.txt

# Crear archivo .env con tu API key de Google Gemini
echo "GOOGLE_API_KEY=tu_api_key_aqui" > .env

# Iniciar el servidor
cd app
python main.py
```

El servidor estará disponible en `http://localhost:8000`

### 3. Elegir un Módulo Frontend

Selecciona el módulo que quieras explorar y sigue su documentación específica:

- **[Módulo Dash](./Dash/README.md)** - Completo y listo para usar ✅
- **[Módulo Streamlit](./Streamlit/README.md)** - Completo y listo para usar ✅
- **Módulo Cursor** - Próximamente 🔜
- **Módulo Lovable** - Próximamente 🔜

---

## 📚 ¿Qué Aprenderás?

### Habilidades Técnicas
- ✅ Construcción de interfaces conversacionales
- ✅ Integración con APIs REST
- ✅ Manejo de estado en aplicaciones web
- ✅ Diseño UI/UX moderno y responsivo
- ✅ Despliegue de aplicaciones

### Herramientas y Frameworks
- 🐍 **Python**: Dash, Streamlit
- 🤖 **IA**: LangGraph, Google Gemini
- 🌐 **APIs**: FastAPI, REST
- 🎨 **UI**: Bootstrap, CSS personalizado
- 🔧 **Dev Tools**: Cursor AI, Git

---

## 🎯 Caso de Uso: SegurosVida+

Todos los módulos construyen variaciones de la misma aplicación: **SegurosVida+ Chat**, un asistente virtual para una empresa ficticia de seguros.

**Funcionalidades de la Aplicación**:
- 💬 Chat interactivo con el agente
- 🧠 Memoria de conversación
- 📊 Información sobre productos de seguros
- 🎨 Interfaz con colores corporativos
- 📱 Diseño responsivo
- ⚡ Respuestas en tiempo real

---

## 🛠️ Requisitos Previos

### Software
- **Python 3.10+** (para módulos Python)
- **Git** (para clonar el repositorio)
- **Editor de código** (VSCode, Cursor, etc.)

### APIs y Servicios
- **Google Gemini API Key** - [Obtener gratis aquí](https://makersuite.google.com/app/apikey)

### Conocimientos Recomendados
- Python básico
- Conceptos de APIs REST
- HTML/CSS básico (opcional)

---

## 📖 Flujo Recomendado del Workshop

### Para Principiantes
1. **Configurar el backend** (`insurance_agent_api`)
2. **Empezar con Streamlit** (más simple y rápido para prototipos)
   - Curso estructurado desde cero con 6 lecciones
   - Aprende paso a paso hasta el proyecto final
3. **Explorar Dash** (más robusto para aplicaciones completas)
4. Experimentar con Cursor AI
5. Probar Lovable para no-code

### Para Desarrolladores Experimentados
- Salta directo al módulo que te interese
- **Streamlit**: Ideal para MVPs y prototipos rápidos
- **Dash**: Mejor para aplicaciones enterprise y dashboards
- Compara diferentes implementaciones
- Personaliza y extiende las aplicaciones

---

## 🤝 Contribuciones

Este es un proyecto educativo. Si encuentras errores o tienes sugerencias:

1. Abre un **Issue** describiendo el problema
2. Envía un **Pull Request** con mejoras
3. Comparte tus proyectos construidos con este workshop

---

## 📄 Licencia

Este proyecto es de código abierto y está disponible para uso educativo.

---

## 📞 Soporte

- 📧 **Email**: Contacta al instructor del workshop
- 💬 **Issues**: Usa el sistema de issues de GitHub
- 📚 **Documentación**: Cada módulo tiene su README detallado

---

## ⭐ Estado del Proyecto

| Módulo | Estado | Documentación | Código |
|--------|--------|---------------|--------|
| Backend API | ✅ Completo | ✅ Completa | ✅ Funcional |
| Dash | ✅ Completo | ✅ Completa | ✅ Funcional |
| Streamlit | ✅ Completo | ✅ Completa | ✅ Funcional |
| Cursor | 🔜 Próximamente | ⏳ Planeado | ⏳ Planeado |
| Lovable | 🔜 Próximamente | ⏳ Planeado | ⏳ Planeado |

---

## 🌟 Próximos Pasos

¿Listo para comenzar?

1. **Configura el backend**: Sigue las instrucciones en [`insurance_agent_api/README.md`](./insurance_agent_api/README.md)
2. **Elige tu primer módulo**: 
   - 🚀 [`Streamlit/README.md`](./Streamlit/README.md) - Para prototipos rápidos y aprender rápido
   - 📊 [`Dash/README.md`](./Dash/README.md) - Para aplicaciones más robustas
3. **Construye tu aplicación**: Sigue la guía paso a paso
4. **Experimenta y personaliza**: Haz tuyo el proyecto

---

<div align="center">

**¡Feliz aprendizaje! 🎓✨**

*Construido con ❤️ para la comunidad de desarrolladores*

</div>

