# 🤖 Módulo Cursor - AI-Assisted Development

Bienvenido al módulo de **Cursor AI**! Aquí aprenderás a construir aplicaciones modernas usando desarrollo asistido por inteligencia artificial.

---

## 🎯 ¿Qué Aprenderás?

Este módulo te enseña el **futuro del desarrollo de software**: colaborar con IA para construir aplicaciones completas más rápido y con mejor calidad.

### Skills que Dominarás
- ✅ **AI-Assisted Coding**: Usar Cursor para generar código de calidad
- ✅ **Effective Prompting**: Escribir prompts que generan el código que necesitas
- ✅ **Modern Web Stack**: Next.js 14, React, TypeScript, Tailwind CSS
- ✅ **API Integration**: Conectar frontend con backend
- ✅ **Containerization**: Docker y Docker Compose
- ✅ **Production Deploy**: Llevar tu app a producción

---

## 📋 Proyecto del Módulo

Construirás **Seguros Bolívar Chat**, una aplicación de chat moderna que se conecta con el agente de IA de seguros.

### Tech Stack
```
Frontend:
- Next.js 14 (App Router)
- React + TypeScript
- Tailwind CSS
- Shadcn/ui Components

Backend:
- Conexión a insurance_agent_api
- REST API integration

Deploy:
- Docker containerization
- Railway / Vercel deployment
```

---

## 📚 Estructura del Módulo

### **📖 Documentación (Seguir en orden)**

1. **`1_CURSOR_BASICS.md`** ⭐
   - Qué es Cursor y cómo funciona
   - Features principales
   - Setup y configuración
   - Primera experiencia

2. **`2_PROMPTING_GUIDE.md`** 🎯
   - Anatomía de un buen prompt
   - Ejemplos prácticos
   - Do's and Don'ts
   - Ejercicios de práctica

3. **`3_BUILD_GUIDE.md`** 💻
   - Guía paso a paso del proyecto
   - Prompts exactos para cada fase
   - Checkpoints de progreso
   - Troubleshooting

4. **`4_DEPLOYMENT_GUIDE.md`** 🚀
   - Containerización con Docker
   - Deploy a Railway (recomendado)
   - Deploy a Vercel (alternativa fácil)
   - Variables de entorno

### **📝 Prompts Guiados**

```
prompts/
├── 01_initial_setup.md       # Setup del proyecto
├── 02_ui_components.md       # Componentes de UI
├── 03_api_integration.md     # Conectar con API
├── 04_styling.md             # Estilos y theming
└── 05_optimization.md        # Optimizaciones finales
```

Cada archivo contiene prompts listos para copiar y pegar en Cursor.

### **💻 Código de Referencia**

```
app/                          # Aplicación Next.js completa
├── src/
│   ├── app/                 # App Router
│   ├── components/          # Componentes React
│   ├── hooks/               # Custom hooks
│   ├── lib/                 # Utilidades
│   └── types/               # TypeScript types
├── public/                  # Assets estáticos
├── Dockerfile              # Containerización
├── docker-compose.yml      # Multi-container setup
└── package.json           # Dependencias
```

---

## 🚀 Inicio Rápido

### Prerrequisitos

```bash
✅ Node.js 18+ instalado
✅ Cursor IDE instalado (https://cursor.sh)
✅ Docker Desktop (para deploy local)
✅ Backend API corriendo en http://localhost:8000
```

### Opción A: Construir Desde Cero (Recomendado 🌟)

Esta es la experiencia completa del módulo:

```bash
# 1. Crear carpeta para tu proyecto
mkdir mi-proyecto-cursor
cd mi-proyecto-cursor

# 2. Abrir en Cursor
cursor .

# 3. Seguir la guía 3_BUILD_GUIDE.md
# Usarás prompts para que Cursor genere todo el código

# 4. Instalar dependencias (cuando el proyecto esté creado)
npm install

# 5. Correr en desarrollo
npm run dev
```

### Opción B: Usar App de Referencia

Si quieres ver el resultado final primero:

```bash
# 1. Ir a la carpeta app
cd Cursor/app

# 2. Instalar dependencias
npm install

# 3. Crear .env.local
echo "NEXT_PUBLIC_API_URL=http://localhost:8000" > .env.local

# 4. Correr en desarrollo
npm run dev

# 5. Abrir http://localhost:3000
```

Si encuentras errores al ejecutar npm commands, usa una consola CMD en lugar de Powershell

---

## 📖 Flujo del Workshop

### Fase 1: Fundamentos (30 min)
1. Lee `1_CURSOR_BASICS.md`
2. Instala y configura Cursor
3. Entiende las features principales
4. Practica con ejemplos simples

### Fase 2: Prompting (30 min)
1. Lee `2_PROMPTING_GUIDE.md`
2. Aprende a escribir prompts efectivos
3. Practica con ejercicios
4. Compara prompts buenos vs malos

### Fase 3: Build (2-3 horas)
1. Sigue `3_BUILD_GUIDE.md` paso a paso
2. Usa los prompts de la carpeta `prompts/`
3. Itera con Cursor hasta lograr cada objetivo
4. Verifica cada checkpoint
5. App completa funcionando localmente

### Fase 4: Deploy (1 hora)
1. Sigue `4_DEPLOYMENT_GUIDE.md`
2. Containeriza con Docker
3. Deploy a Railway o Vercel
4. Configura variables de entorno
5. App en producción con URL pública

---

## 🎓 Niveles de Dificultad

### 🟢 Principiante
- **Requisitos**: JavaScript básico
- **Tiempo**: 4-5 horas
- **Ruta**: Sigue todos los pasos de la guía
- **Usa**: Prompts pre-escritos tal cual

### 🟡 Intermedio
- **Requisitos**: React/Next.js básico
- **Tiempo**: 2-3 horas
- **Ruta**: Usa prompts como base, personaliza
- **Usa**: Itera con Cursor para mejorar

### 🔴 Avanzado
- **Requisitos**: Full stack experience
- **Tiempo**: 1-2 horas
- **Ruta**: Construye solo con Cursor, consulta docs
- **Usa**: Escribe tus propios prompts

---

## 💡 ¿Por Qué Cursor?

### Ventajas sobre Desarrollo Traditional
- ⚡ **10x más rápido**: De idea a código funcional en minutos
- 🧠 **Menos memorización**: La IA conoce las APIs y sintaxis
- 🐛 **Menos bugs**: Code review automático
- 📚 **Aprendizaje acelerado**: Aprende mientras construyes
- 🎨 **Más creatividad**: Menos tiempo en boilerplate

### Ventajas sobre GitHub Copilot
- 💬 **Chat contextual**: Entiende todo tu proyecto
- ✨ **Composer**: Edita múltiples archivos a la vez
- 🔍 **Codebase search**: Busca semánticamente en tu código
- 🎯 **Cmd+K inline**: Edita código en el lugar
- 📝 **Mejor contexto**: Lee tu documentación automáticamente

---

## 🛠️ Tech Stack Detallado

### Frontend Framework
**Next.js 14 (App Router)**
- Server Components por defecto
- Routing basado en archivos
- API routes integradas
- Optimizaciones automáticas
- Excelente DX (Developer Experience)

### UI & Styling
**Tailwind CSS + Shadcn/ui**
- Utility-first CSS
- Componentes pre-construidos
- Totalmente personalizable
- Responsive por defecto
- Dark mode ready

### Type Safety
**TypeScript**
- Tipos estáticos
- Mejor IntelliSense
- Menos runtime errors
- Refactoring seguro
- Mejor con IA (Cursor entiende mejor)

### State & API
**React Hooks + Fetch API**
- useState, useEffect
- Custom hooks (useChat)
- Async/await patterns
- Error boundaries
- Loading states

---

## 📊 Comparación con Otros Módulos

| Aspecto | Dash (Python) | Cursor (Next.js) | Streamlit |
|---------|---------------|------------------|-----------|
| **Lenguaje** | Python | TypeScript/JS | Python |
| **Curva** | Media | Alta | Baja |
| **Performance** | Media | Alta | Media |
| **Customización** | Media | Muy Alta | Baja |
| **Deploy** | Medio | Fácil | Muy Fácil |
| **AI Assist** | No | ✅ Sí | Parcial |
| **Production** | Sí | ✅ Ideal | Prototipos |

---

## 🎯 Resultado Final

Al completar este módulo tendrás:

### ✅ Una App Funcional
- Chat interactivo con IA
- UI moderna y responsiva
- Integración con backend
- Manejo de errores robusto
- Loading states
- Colores corporativos Seguros Bolívar

### ✅ Skills Nuevas
- Desarrollo asistido por IA
- Prompting efectivo
- Next.js y React moderno
- Docker y containerización
- Deploy a producción

### ✅ Portfolio Piece
- Código en GitHub
- App desplegada con URL pública
- Caso de uso real
- Stack moderno y demandado

---

## 🔧 Troubleshooting Común

### Cursor no responde bien
- ✅ Sé más específico en tu prompt
- ✅ Proporciona contexto del proyecto
- ✅ Divide en pasos más pequeños

### Errores de TypeScript
- ✅ Pregunta a Cursor: "Fix TypeScript errors"
- ✅ Revisa imports
- ✅ Verifica tipos en `types/index.ts`

### API no conecta
- ✅ Backend debe estar corriendo en :8000
- ✅ Revisa .env.local
- ✅ Verifica CORS en el backend

### Docker build falla
- ✅ Verifica .dockerignore incluye node_modules
- ✅ Asegura que dependencies estén en package.json
- ✅ Usa Node 20 alpine

---

## 📚 Recursos Adicionales

### Cursor
- 🌐 [Cursor Docs](https://docs.cursor.com/)
- 📺 [Cursor Tips (YouTube)](https://youtube.com/cursor)
- 💬 [Cursor Community](https://cursor.sh/community)

### Next.js
- 📖 [Next.js Docs](https://nextjs.org/docs)
- 🎓 [Learn Next.js](https://nextjs.org/learn)
- 📺 [Next.js YouTube](https://www.youtube.com/@nextjs)

### Shadcn/ui
- 🎨 [Component Library](https://ui.shadcn.com/)
- 📦 [Examples](https://ui.shadcn.com/examples)

### Deployment
- 🚂 [Railway Docs](https://docs.railway.app/)
- ▲ [Vercel Docs](https://vercel.com/docs)
- 🐳 [Docker Docs](https://docs.docker.com/)

---

## 🤝 Contribuciones

¿Encontraste un bug o tienes una mejora?
- Abre un issue
- Envía un PR
- Comparte tu experiencia

---

## 🌟 Próximos Pasos

**¿Listo para empezar?**

1. 📖 Lee `1_CURSOR_BASICS.md`
2. 🎯 Practica con `2_PROMPTING_GUIDE.md`
3. 💻 Construye siguiendo `3_BUILD_GUIDE.md`
4. 🚀 Deploy con `4_DEPLOYMENT_GUIDE.md`

---

<div align="center">

**¡Bienvenido al futuro del desarrollo de software! 🚀✨**

*Construido con Cursor AI y ❤️*

</div>

