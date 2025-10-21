# 4️⃣ Deployment Guide - Llevando tu App a Producción

Guía completa para containerizar y deployar tu aplicación Seguros Bolívar Chat.

---

## 🎯 Objetivos

Al finalizar este módulo sabrás:
- ✅ Containerizar una app Next.js con Docker
- ✅ Usar Docker Compose para multi-container setup
- ✅ Deploy a Railway (recomendado)
- ✅ Deploy a Vercel (alternativa fácil)
- ✅ Configurar variables de entorno en producción
- ✅ Monitorear y debuggear en producción

---

## 🛤️ Dos Caminos de Deployment

### Track 1: Vercel (⚡ Rápido y Fácil)
**Tiempo**: 10-15 minutos  
**Ideal para**: Prototipos, demos, proyectos personales  
**Pro**: Zero-config, CI/CD automático, CDN global  
**Con**: Limitado en customización, necesitas plan para más recursos  

### Track 2: Railway con Docker (🚂 Profesional)
**Tiempo**: 30-45 minutos  
**Ideal para**: Apps production, aprendizaje de DevOps  
**Pro**: Full control, containerización, escalable  
**Con**: Más complejo, requiere entender Docker  

**Recomendación**: Empieza con Vercel para ver tu app online rápido, luego prueba Railway para aprender containerización.

---

## ⚡ Track 1: Deploy a Vercel (Fácil)

### Step 1: Preparar Proyecto

**Verificaciones**:
```bash
# Desde la carpeta app/
npm run build
# Debe completar sin errores
```

**Fix common build issues con Cursor**:
```markdown
I'm getting build errors when running npm run build:

[paste errors]

Help me fix these before deployment.
Check for:
- TypeScript errors
- Missing dependencies
- Environment variables in build
```

### Step 2: Push a GitHub

```bash
# Inicializar Git (si no lo hiciste)
git init
git add .
git commit -m "Initial commit: Seguros Bolivar Chat"

# Crear repo en GitHub (hazlo manualmente en github.com)
# Luego conecta:
git remote add origin https://github.com/tu-usuario/seguros-chat.git
git branch -M main
git push -u origin main
```

### Step 3: Conectar a Vercel

1. Ve a [vercel.com](https://vercel.com)
2. Sign in con GitHub
3. Click "New Project"
4. Import tu repositorio
5. Configuración:
   - Framework Preset: Next.js (auto-detectado)
   - Root Directory: `./app` (si tu app está en subdirectorio)
   - Build Command: (dejar default) `next build`
   - Output Directory: (dejar default) `.next`

6. Environment Variables:
   ```
   NEXT_PUBLIC_API_URL = https://tu-api-backend.com
   ```
   ⚠️ **Importante**: Necesitas que tu backend también esté deployed

7. Click "Deploy"

### Step 4: Deploy Automático

✅ Cada push a `main` → deploy automático  
✅ Pull requests → preview deployments  
✅ URL pública: `tu-app.vercel.app`  

**✅ Checkpoint**: App deployed en Vercel

---

## 🐳 Track 2: Docker + Railway (Profesional)

### Prerequisitos

```bash
✅ Docker Desktop instalado
✅ Cuenta en Railway.app
✅ Railway CLI instalado
```

Instalar Railway CLI:
```bash
npm install -g @railway/cli
```

---

### Step 1: Crear Dockerfile

**Prompt para Cursor** (crea `app/Dockerfile`):
```markdown
Create a production-ready Dockerfile for this Next.js 14 app.

Requirements:
1. Multi-stage build for smaller image size
2. Use Node.js 20 Alpine (lightweight)
3. Stages:
   - deps: Install dependencies
   - builder: Build the app
   - runner: Run production server

4. Optimizations:
   - Only copy necessary files
   - Use standalone output mode
   - Run as non-root user
   - Minimize layers

5. Port: 3000
6. Health check: optional but nice

Follow Next.js official Docker recommendations.
Add comments explaining each section.
```

**Resultado esperado** (verifica que tenga esto):
```dockerfile
FROM node:20-alpine AS deps
# Install dependencies only

FROM node:20-alpine AS builder
# Build the application

FROM node:20-alpine AS runner
# Run the production server
```

### Step 2: Configurar Next.js para Docker

**Prompt para Cursor** (edita `app/next.config.js` o crea si no existe):
```markdown
Update next.config.js to enable standalone output mode for Docker.

Add:
```
const nextConfig = {
  output: 'standalone',
}
```

This creates a self-contained build in .next/standalone/
which includes all necessary files for production.

Explain why this is needed for Docker deployment.
```

### Step 3: Crear .dockerignore

**Prompt para Cursor** (crea `app/.dockerignore`):
```markdown
Create a .dockerignore file to exclude unnecessary files from Docker build.

Exclude:
- node_modules
- .next (will be rebuilt)
- .git
- .env.local (use .env.production)
- README.md
- *.md
- .vscode
- .idea
- *.log
- .DS_Store
- coverage
- dist

This reduces build context size and speeds up builds.
```

### Step 4: Build Local (Prueba)

```bash
cd app

# Build the Docker image
docker build -t seguros-chat .

# Run locally
docker run -p 3000:3000 -e NEXT_PUBLIC_API_URL=http://localhost:8000 seguros-chat

# Test en http://localhost:3000
```

**Si hay errores**, usa Cursor:
```markdown
Docker build is failing with this error:
[paste error]

Dockerfile: @file:Dockerfile

Help me fix this issue.
```

**✅ Checkpoint**: Docker image funciona localmente

---

### Step 5: Crear docker-compose.yml

**Objetivo**: Correr frontend + backend juntos.

**Prompt para Cursor** (crea `docker-compose.yml` en la raíz del workspace):
```markdown
Create a docker-compose.yml that orchestrates:

1. Backend service:
   - Build from: ./insurance_agent_api
   - Port: 8000
   - Environment: GOOGLE_API_KEY from env
   - Name: api

2. Frontend service:
   - Build from: ./Cursor/app
   - Port: 3000
   - Environment: NEXT_PUBLIC_API_URL=http://api:8000
   - Depends on: api
   - Name: frontend

3. Network:
   - Create a bridge network so services can communicate
   - Frontend can reach backend at http://api:8000

Add health checks if possible.
Add restart policies (restart: unless-stopped).
Use environment files (.env) for secrets.

This allows running the entire stack with:
docker-compose up --build
```

### Step 6: Probar Stack Completo

```bash
# Desde la raíz del proyecto
docker-compose up --build

# Deberías ver:
# - Backend corriendo en :8000
# - Frontend corriendo en :3000
# - Frontend conectándose al backend

# Abre http://localhost:3000
# Prueba enviar mensajes
```

**✅ Checkpoint**: Stack completo funciona con Docker Compose

---

### Step 7: Deploy a Railway

#### 7.1 Configurar Railway Project

```bash
# Login
railway login

# Crear nuevo proyecto
railway init

# Nombre del proyecto: seguros-bolivar-chat
```

#### 7.2 Deploy Backend Primero

```bash
# Desde insurance_agent_api/
cd ../insurance_agent_api

# Crear servicio
railway up

# Configurar variables de entorno en Railway dashboard
```

En el dashboard de Railway (railway.app):
1. Ve a tu servicio API
2. Variables → Add Variable:
   ```
   GOOGLE_API_KEY=tu_api_key_aqui
   ```
3. Settings → Generate Domain
4. Copia la URL (ej: `https://tu-api.up.railway.app`)

#### 7.3 Deploy Frontend

```bash
cd Cursor/app

# Crear nuevo servicio
railway up

# Este comando:
# 1. Detecta Dockerfile
# 2. Build la image
# 3. Deploy a Railway
```

En Railway dashboard:
1. Ve al servicio frontend
2. Variables → Add Variable:
   ```
   NEXT_PUBLIC_API_URL=https://tu-api.up.railway.app
   ```
3. Settings → Generate Domain
4. Tu app está en: `https://tu-frontend.up.railway.app`

**✅ Checkpoint**: App deployed en Railway con URL pública

---

## 🔐 Variables de Entorno en Producción

### Ambiente: Development (.env.local)
```bash
NEXT_PUBLIC_API_URL=http://localhost:8000
```

### Ambiente: Production (Railway/Vercel)
```bash
NEXT_PUBLIC_API_URL=https://api-production.railway.app
```

### Best Practices

1. **Nunca commits secrets**:
   ```bash
   # .gitignore debe incluir:
   .env
   .env.local
   .env.*.local
   ```

2. **Usa .env.example como template**:
   ```bash
   NEXT_PUBLIC_API_URL=http://localhost:8000
   # Otros secrets aquí sin valores reales
   ```

3. **Variables de Entorno en Next.js**:
   - `NEXT_PUBLIC_*`: Accesibles en browser (URLs públicas)
   - Sin prefijo: Solo en servidor (API keys secretas)

---

## 🔍 Monitoreo y Debugging

### Logs en Vercel

```bash
# CLI
vercel logs [deployment-url]

# O en dashboard: Deployments → [tu deploy] → Logs
```

### Logs en Railway

```bash
# CLI
railway logs

# O en dashboard: tu servicio → View Logs
```

### Debugging Común

#### Error: "API_URL is undefined"

**Causa**: Variable de entorno no configurada.

**Solución**:
```bash
# Vercel: Agregar en Settings → Environment Variables
# Railway: Agregar en Variables tab
# Redeploy después de agregar
```

#### Error: "CORS error"

**Causa**: Backend rechaza requests del frontend.

**Solución en backend**:
```python
# insurance_agent_api/app/main.py
from fastapi.middleware.cors import CORSMiddleware

app.add_middleware(
    CORSMiddleware,
    allow_origins=["https://tu-frontend.vercel.app"],  # Tu dominio
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
```

#### Error: "Build failed"

**Debugging con Cursor**:
```markdown
My deployment is failing with this error:
[paste error from deployment logs]

Build configuration:
- Platform: [Vercel/Railway]
- Framework: Next.js 14
- Node version: 20

Help me understand and fix the error.
```

---

## 🚀 Optimizaciones Post-Deploy

### 1. Performance Optimization

**Prompt para Cursor**:
```markdown
Optimize the Next.js app for better performance:

1. Enable Image Optimization (Next.js Image component)
2. Add loading states with Suspense boundaries
3. Implement code splitting for heavy components
4. Add caching headers for static assets
5. Lazy load non-critical components

Show me what changes to make and where.
```

### 2. SEO Optimization

**Prompt para Cursor**:
```markdown
Improve SEO for the app:

1. Add proper meta tags in layout.tsx:
   - title
   - description
   - og:image, og:title, og:description
   - twitter:card

2. Add favicon and app icons
3. Create robots.txt
4. Add sitemap.xml
5. Ensure semantic HTML

Update @file:src/app/layout.tsx with these improvements.
```

### 3. Analytics (Opcional)

```bash
# Instalar Vercel Analytics
npm install @vercel/analytics

# O Google Analytics
npm install react-ga4
```

**Prompt para Cursor**:
```markdown
Add Vercel Analytics to track page views.

1. Install @vercel/analytics
2. Add Analytics component to layout.tsx
3. Ensure GDPR compliance (show notice)

Keep it simple and privacy-friendly.
```

---

## 🌍 Custom Domain (Opcional)

### En Vercel:

1. Compra dominio (Namecheap, Google Domains, etc.)
2. Vercel dashboard → tu proyecto → Settings → Domains
3. Add Domain: `tudominio.com`
4. Configura DNS:
   ```
   Type: A
   Name: @
   Value: 76.76.21.21
   
   Type: CNAME
   Name: www
   Value: cname.vercel-dns.com
   ```
5. Espera propagación (5-15 min)

### En Railway:

1. Railway dashboard → tu servicio → Settings
2. Custom Domain → Add Domain
3. Configura DNS en tu registrar:
   ```
   Type: CNAME
   Name: @
   Value: [railway te da el valor]
   ```

---

## 🔒 Seguridad en Producción

### Checklist de Seguridad:

```
✅ Secrets en variables de entorno (no en código)
✅ HTTPS enabled (automático en Vercel/Railway)
✅ CORS configurado correctamente
✅ Rate limiting en API (si aplica)
✅ Input validation en forms
✅ XSS protection (React lo hace por default)
✅ CSP headers (opcional pero recomendado)
✅ Dependencies actualizadas (npm audit fix)
```

**Prompt para Cursor**:
```markdown
Review security best practices for this Next.js app.

Check @codebase for:
1. Any hardcoded secrets
2. Missing input validation
3. Insecure dependencies (npm audit)
4. XSS vulnerabilities
5. Recommend improvements

Provide a security checklist and fixes.
```

---

## 📊 Comparison: Vercel vs Railway

| Aspecto | Vercel | Railway |
|---------|--------|---------|
| **Setup Time** | 5 min ⚡ | 30 min |
| **Precio Free** | Muy generoso | 500 hrs/mes |
| **CDN Global** | ✅ Sí | ⚠️ Limitado |
| **Serverless** | ✅ Sí | ❌ No |
| **Docker Support** | ⚠️ Limitado | ✅ Full |
| **Backend + Frontend** | Separados | ✅ Juntos |
| **Database** | Requiere integraciones | ✅ Built-in Postgres |
| **CI/CD** | ✅ Automático | ✅ Automático |
| **Monitoreo** | ✅ Built-in | ✅ Built-in |
| **Custom Domains** | ✅ Gratis | ✅ Gratis |
| **Learning Curve** | Fácil | Media |

**Recomendación**:
- **Vercel**: Si solo tienes frontend o proyectos Next.js/React
- **Railway**: Si necesitas full stack con DB, background jobs, etc.

---

## 🎓 Lo Que Aprendiste

Ahora sabes:
- ✅ Cómo funciona containerización con Docker
- ✅ Multi-stage Docker builds para optimización
- ✅ Docker Compose para orchestration
- ✅ Deploy serverless (Vercel)
- ✅ Deploy containerizado (Railway)
- ✅ Configurar variables de entorno en producción
- ✅ Debugging de deployments
- ✅ Optimizaciones post-deploy
- ✅ Consideraciones de seguridad

**Estas son skills profesionales muy demandadas.** 💼

---

## ✅ Checklist Final

```
✅ App deployed y accesible con URL pública
✅ Backend conectado y funcionando
✅ Variables de entorno configuradas
✅ HTTPS habilitado
✅ Logs accesibles para debugging
✅ No hay secrets en el código
✅ Build optimizado para producción
✅ Probado en diferentes dispositivos
✅ Custom domain (opcional)
✅ Monitoring configurado (opcional)
```

---

## 🎉 ¡Felicidades!

Has completado el módulo de Cursor AI. Ahora tienes:

1. ✅ Una aplicación Next.js moderna
2. ✅ Construida con asistencia de IA
3. ✅ Deployed en producción
4. ✅ Con URL pública para compartir
5. ✅ Skills en desarrollo moderno

### Comparte Tu Proyecto

- 📱 URL pública: `_______________________`
- 💻 GitHub repo: `_______________________`
- 📸 Screenshot para portfolio

---

## 🚀 Próximos Pasos Sugeridos

### Nivel 1: Mejora Este Proyecto
- Agrega autenticación (NextAuth.js)
- Implementa base de datos (Prisma + PostgreSQL)
- Añade tests (Jest + React Testing Library)
- Crea dashboard de analytics

### Nivel 2: Nuevos Proyectos
- Construye otro proyecto con Cursor
- Prueba otro framework (Remix, Astro)
- Contribuye a open source
- Enseña a otros lo que aprendiste

### Nivel 3: Profundiza
- Aprende Kubernetes para orchestration avanzada
- Explora CI/CD con GitHub Actions
- Estudia arquitecturas serverless
- Experimenta con edge computing

---

## 📚 Recursos Adicionales

### Docker
- [Docker Docs](https://docs.docker.com/)
- [Docker Compose Docs](https://docs.docker.com/compose/)
- [Docker Best Practices](https://docs.docker.com/develop/dev-best-practices/)

### Deployment Platforms
- [Vercel Docs](https://vercel.com/docs)
- [Railway Docs](https://docs.railway.app/)
- [Render](https://render.com/docs)
- [Fly.io](https://fly.io/docs/)

### Next.js Production
- [Next.js Deployment](https://nextjs.org/docs/deployment)
- [Next.js Docker](https://github.com/vercel/next.js/tree/canary/examples/with-docker)
- [Next.js Performance](https://nextjs.org/docs/advanced-features/measuring-performance)

---

<div align="center">

**🎊 ¡Has completado el Módulo Cursor! 🎊**

*De cero a producción con IA como copiloto*

**Siguiente**: Explora otros módulos del workshop o construye tu próximo proyecto.

---

⭐ **Si este módulo te ayudó, considera**:
- Compartir tu experiencia
- Contribuir mejoras
- Ayudar a otros learners

**Keep building! 🚀**

</div>

