# 💜 Módulo Lovable - No-Code AI Builder

Construye aplicaciones web profesionales usando **solo lenguaje natural**, sin escribir código.

---

## 🎯 ¿Qué es Lovable?

**Lovable** es una plataforma que construye aplicaciones web completas conversando con IA. Describes lo que quieres y Lovable lo crea automáticamente.

### Características Clave
- 💬 **Build con chat**: Escribe en lenguaje natural
- ⚡ **Preview en tiempo real**: Ve cambios instantáneamente  
- 🎨 **UI profesional**: Componentes modernos automáticos (React + Shadcn/ui)
- 🔗 **GitHub sync**: Sincroniza tu código automáticamente
- 📦 **Code export**: Descarga el código React completo
- 🚀 **Deploy instantáneo**: Publica con un clic

### Tech Stack Generado
- React + TypeScript + Vite
- Tailwind CSS + Shadcn/ui
- LocalStorage para persistencia

---

## 📋 Proyecto: SegurosVida+ Chat

Construirás un **chat conversacional** que consume la API `insurance_agent_api` usando únicamente prompts.

**Funcionalidades:**
- Chat con el agente de seguros
- Múltiples conversaciones (threads)
- Integración con API local (localhost:8000)
- UI moderna y responsive
- Manejo de errores y loading states

---

## 📚 Guías del Módulo

Sigue este orden para mejores resultados:

1. **`1_LOVABLE_BASICS.md`** ⭐ - Qué es Lovable, crear cuenta, interfaz básica
2. **`2_PROMPTING_GUIDE.md`** 🎯 - Cómo escribir prompts efectivos
3. **`3_BUILD_GUIDE.md`** 💻 - Construcción paso a paso del chat (lo más importante)
4. **`4_GITHUB_EXPORT.md`** 📦 - Exportar código y correr localmente
5. **`5_DEPLOYMENT.md`** 🚀 - Deploy y limitaciones con localhost

### Prompts Listos

```
prompts/
├── 01_initial_project.md      # Setup inicial
├── 02_chat_interface.md       # UI del chat
├── 03_api_integration.md      # Conectar con backend
├── 04_multiple_threads.md     # Múltiples conversaciones
└── 05_final_polish.md         # Pulir y mejorar
```

---

## 🚀 Inicio Rápido

### Prerrequisitos
- Cuenta en [lovable.dev](https://lovable.dev) (gratuita)
- Backend corriendo en `http://localhost:8000`

### Construir en Lovable

1. Ir a https://lovable.dev y crear cuenta
2. Crear nuevo proyecto
3. Seguir `3_BUILD_GUIDE.md` con los prompts
4. Iterar hasta completar la app
5. Deploy con un clic (⚠️ no conectará a localhost)

### Correr Código Exportado

```bash
cd Lovable/exported_code
npm install
echo "VITE_API_URL=http://localhost:8000" > .env.local

# Terminal 1: Backend
cd ../../insurance_agent_api/app
python main.py

# Terminal 2: Frontend  
cd ../../Lovable/exported_code
npm run dev
# Abrir http://localhost:5173
```

---

## 📊 Lovable vs Otras Herramientas

| Aspecto | Lovable | Streamlit | Cursor |
|---------|---------|-----------|--------|
| **Requiere código** | No | Sí (Python) | Sí (TypeScript) |
| **Curva aprendizaje** | Muy baja | Baja | Alta |
| **Velocidad inicial** | Ultra rápida | Rápida | Muy rápida |
| **UI Quality** | Excelente | Básica | Excelente |
| **Code export** | ✅ Sí | No | Nativo |
| **Ideal para** | MVPs rápidos | Data apps | Apps completas |

**Usa Lovable cuando:**
- ✅ Necesitas prototipo rápido
- ✅ No sabes programar o quieres velocidad extrema
- ✅ Quieres UI profesional sin esfuerzo

---

## ⚠️ Limitación Importante

### Localhost en Deploy
- ✅ **Preview de Lovable**: Funciona con `localhost:8000`
- ❌ **Deploy en lovable.app**: NO puede conectar a localhost (app está en la nube)

**Para workshop:** Usa la preview de Lovable que sí accede a tu localhost.

---

## 🎯 Lo que Aprenderás

- No-code development con IA
- Prompting efectivo para UIs
- Integración con APIs REST
- Exportar y modificar código React
- Deploy de apps web

---

**[Comenzar: 1. Lovable Basics →](./1_LOVABLE_BASICS.md)**
