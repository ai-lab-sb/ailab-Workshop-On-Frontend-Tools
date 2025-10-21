# 4️⃣ GitHub Integration & Code Export

Aprende a sincronizar tu proyecto con GitHub, exportar el código y correrlo localmente.

---

## 🔗 Parte 1: Sincronizar con GitHub

### Conectar Repositorio

1. En tu proyecto de Lovable, click en **Settings** (⚙️)
2. Click en **"Connect to GitHub"**
3. Autoriza Lovable en GitHub (si no lo has hecho)
4. Selecciona:
   - **Repositorio existente** (si tienes uno), o
   - **"Create new repository"** → nombre: `seguros-vida-chat`
5. Click **"Connect"**

### Resultado

- ✅ Cada cambio en Lovable se sincroniza automáticamente
- ✅ Puedes ver commits en GitHub
- ✅ Control de versiones automático
- ✅ Backup en la nube

---

## 📦 Parte 2: Exportar Código Localmente

### Opción A: Clonar desde GitHub

Si conectaste GitHub:

```bash
# Clonar el repositorio
git clone https://github.com/TU_USUARIO/seguros-vida-chat.git
cd seguros-vida-chat
```

### Opción B: Download ZIP

Si no usaste GitHub:

1. En Lovable, click en **"Export"** o **"Download"**
2. Descarga el ZIP
3. Extrae en tu carpeta de proyectos
4. Renombra carpeta a `exported_code`
5. Mueve a `Lovable/exported_code/` en el repositorio del workshop

---

## 💻 Parte 3: Correr Proyecto Localmente

### 1. Instalar Dependencias

```bash
cd exported_code  # o el nombre de tu carpeta
npm install
```

Esto instala:
- React, TypeScript, Vite
- Tailwind CSS
- Shadcn/ui components
- Otras dependencias

### 2. Configurar Variables de Entorno

Crea archivo `.env.local`:

```bash
# Windows (PowerShell)
echo "VITE_API_URL=http://localhost:8000" > .env.local

# Mac/Linux
echo "VITE_API_URL=http://localhost:8000" > .env.local
```

O créalo manualmente con el contenido:
```
VITE_API_URL=http://localhost:8000
```

### 3. Iniciar Backend

En una terminal:

```bash
cd ../../insurance_agent_api/app
python main.py
```

Debe mostrar:
```
INFO:     Uvicorn running on http://127.0.0.1:8000
```

### 4. Iniciar Frontend

En otra terminal:

```bash
cd Lovable/exported_code
npm run dev
```

Debe mostrar:
```
  VITE v5.x.x  ready in xxx ms

  ➜  Local:   http://localhost:5173/
  ➜  Network: use --host to expose
```

### 5. Abrir en Navegador

Ve a `http://localhost:5173`

¡Tu app debería funcionar igual que en Lovable!

---

## 📁 Estructura del Código Exportado

```
exported_code/
├── src/
│   ├── components/        # Componentes React
│   │   ├── ui/           # Componentes Shadcn/ui
│   │   ├── ChatMessage.tsx
│   │   ├── Sidebar.tsx
│   │   └── ...
│   ├── hooks/            # Custom hooks
│   │   └── useChat.ts
│   ├── lib/              # Utilidades
│   │   └── api.ts        # Funciones API
│   ├── pages/            # Páginas
│   │   └── Index.tsx     # Página principal
│   ├── App.tsx           # Componente raíz
│   ├── main.tsx          # Entry point
│   └── index.css         # Estilos globales
├── public/               # Assets estáticos
├── .env.local           # Variables entorno (crear)
├── package.json         # Dependencias
├── vite.config.ts       # Config Vite
├── tailwind.config.ts   # Config Tailwind
└── tsconfig.json        # Config TypeScript
```

---

## 🔧 Personalizar el Código

### Ejemplo: Cambiar Color Primario

**Archivo:** `tailwind.config.ts`

```typescript
export default {
  theme: {
    extend: {
      colors: {
        primary: {
          DEFAULT: '#1e40af', // Cambia este color
          foreground: '#ffffff',
        },
      },
    },
  },
}
```

### Ejemplo: Modificar Lógica del Chat

**Archivo:** `src/lib/api.ts`

```typescript
export async function sendMessage(message: string, threadId: string) {
  const response = await fetch(`${import.meta.env.VITE_API_URL}/chat`, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ message, thread_id: threadId }),
  });
  
  // Agrega tu lógica personalizada aquí
  
  return response.json();
}
```

---

## 🔄 Workflow: Lovable → Local

### Desarrollo Híbrido

1. **Prototipa en Lovable**: Usa IA para construir rápido
2. **Exporta a Local**: Cuando necesites control fino
3. **Personaliza manualmente**: Edita código TypeScript/React
4. **(Opcional) Sube cambios**: Push a GitHub

### Comandos Útiles

```bash
# Desarrollo
npm run dev          # Inicia servidor dev (hot reload)

# Build producción
npm run build        # Crea build optimizado en /dist

# Preview build
npm run preview      # Prueba build de producción localmente

# Linting
npm run lint         # Verifica errores de código
```

---

## 🧪 Testing Local

### Verificar que Todo Funcione

1. ✅ Frontend carga en localhost:5173
2. ✅ Backend responde en localhost:8000/health
3. ✅ Puedes enviar mensajes y recibir respuestas
4. ✅ Múltiples conversaciones funcionan
5. ✅ LocalStorage persiste datos (recarga página)
6. ✅ Errores se manejan (apaga backend, verifica mensaje)

---

## 📚 Aprender del Código

### Para Aprender React

Abre `src/components/ChatMessage.tsx` y estudia:
- Cómo se define un componente
- Props y TypeScript types
- Conditional rendering
- Tailwind classes

### Para Aprender Hooks

Abre `src/hooks/useChat.ts` (si existe) y estudia:
- useState para estado
- useEffect para side effects
- Custom hooks pattern

### Para Aprender API Calls

Abre `src/lib/api.ts` y estudia:
- Fetch API
- Async/await
- Error handling
- Environment variables

---

## ⚠️ Troubleshooting

### Error: "VITE_API_URL is not defined"

**Solución:** Verifica que `.env.local` existe y está bien escrito.

### Error: "Failed to fetch"

**Solución:** Backend no está corriendo. Inicia `python main.py` en `insurance_agent_api/app/`.

### Error: npm install falla

**Solución:**
```bash
# Limpia cache
npm cache clean --force

# Intenta de nuevo
npm install
```

### Puerto 5173 ocupado

**Solución:**
```bash
# Usa otro puerto
npm run dev -- --port 3000
```

---

## 🎯 Siguientes Pasos

Con el código exportado puedes:

1. **Personalizar**: Modifica componentes, colores, lógica
2. **Aprender**: Estudia el código generado
3. **Extender**: Agrega features que Lovable no puede hacer
4. **Deploy**: Sube a Vercel, Netlify, etc.

**[Continuar: 5. Deployment →](./5_DEPLOYMENT.md)**

---

**[← Build Guide](./3_BUILD_GUIDE.md)** | **[Deployment →](./5_DEPLOYMENT.md)**
