# 5️⃣ Deployment

Aprende a desplegar tu aplicación en Lovable hosting y las limitaciones con localhost.

---

## 🚀 Deploy en Lovable Hosting

### Opción 1: Deploy Directo (Recomendado para Workshop)

1. En tu proyecto de Lovable, click en **"Deploy"** (botón arriba a la derecha)
2. Elige un nombre para tu app: `seguros-vida-chat`
3. Click **"Deploy to Lovable"**
4. Espera ~30 segundos
5. ¡Listo! Tu app estará en: `https://seguros-vida-chat.lovable.app`

### Resultado

- ✅ URL pública accesible desde cualquier lugar
- ✅ HTTPS automático
- ✅ CDN global (rápido en todo el mundo)
- ✅ Actualizaciones con un click

---

## ⚠️ LIMITACIÓN IMPORTANTE: Localhost

### El Problema

**Tu app desplegada en `lovable.app` NO puede conectarse a `localhost:8000`**

**¿Por qué?**
- Tu app está en servidores de Lovable (en la nube)
- `localhost:8000` es tu computadora local
- No hay conexión entre ellos

### Lo que Funciona vs No Funciona

| Escenario | ¿Funciona? |
|-----------|------------|
| **Preview de Lovable** → localhost:8000 | ✅ Sí |
| **Código local** (localhost:5173) → localhost:8000 | ✅ Sí |
| **Deploy lovable.app** → localhost:8000 | ❌ No |
| **Deploy lovable.app** → API pública | ✅ Sí |

---

## 🎯 Soluciones para Workshop

### Opción 1: Usar Preview de Lovable (Recomendado)

**Para el workshop:**
- Usa la **vista preview** dentro de Lovable
- Esta SÍ se conecta a tu localhost:8000
- Suficiente para demostrar funcionalidad

**Cómo:**
1. Mantén backend corriendo: `python main.py`
2. Trabaja en Lovable
3. La preview funciona perfectamente con localhost

### Opción 2: Código Exportado Local

**Para testing completo:**
```bash
# Terminal 1: Backend
cd insurance_agent_api/app
python main.py

# Terminal 2: Frontend
cd Lovable/exported_code
npm run dev
# Abre localhost:5173
```

Ambos locales → funciona perfectamente.

### Opción 3: Deploy Real (Producción)

Si quieres deploy público que funcione, necesitas:

**Backend público** (opciones):
1. **Railway**: Deploy gratis con GitHub
   ```bash
   # En railway.app
   - New Project → Deploy from GitHub
   - Selecciona insurance_agent_api
   - URL pública: https://tu-api.railway.app
   ```

2. **Render**: Plan gratuito
3. **Heroku**: Opción de pago

Luego en Lovable:
```
Actualiza la URL del API de:
http://localhost:8000
a:
https://tu-api.railway.app
```

---

## 🔧 Variables de Entorno en Deploy

### En Lovable Deploy

1. Settings → Environment Variables
2. Agrega:
   ```
   Key: VITE_API_URL
   Value: https://tu-api-publica.com (o tu backend público)
   ```

### En Código Exportado

Archivo `.env.local`:
```
# Desarrollo
VITE_API_URL=http://localhost:8000

# Producción (comentar/descomentar según necesites)
# VITE_API_URL=https://tu-api-publica.com
```

---

## 📊 Comparación de Opciones

### Para Workshop/Demo

| Opción | Pros | Contras |
|--------|------|---------|
| **Preview Lovable** | ✅ Fácil, funciona con localhost | ⚠️ Solo tú lo ves |
| **Local export** | ✅ Control total | ⚠️ Solo en tu PC |
| **Deploy + mock** | ✅ URL pública | ❌ Sin backend real |

### Para Producción Real

| Opción | Pros | Contras |
|--------|------|---------|
| **Lovable + Railway** | ✅ Todo público, profesional | ⚠️ Backend debe estar online |
| **Export + Vercel/Netlify** | ✅ Más control | ⚠️ Requiere más setup |

---

## 🎯 Recomendación para el Workshop

**Mejor workflow:**

1. **Desarrollo**: Usa preview de Lovable con localhost
2. **Demo**: Muestra la preview funcionando
3. **Código**: Exporta y muestra estructura React
4. **Explicación**: Menciona limitación de localhost en deploy público

**NO es necesario desplegar públicamente para completar el workshop.**

---

## 🚀 Deploy Alternativo: Vercel/Netlify

Si exportaste el código:

### Vercel

```bash
# Instala Vercel CLI
npm i -g vercel

# Deploy
cd exported_code
vercel

# Sigue instrucciones
```

### Netlify

```bash
# Build
npm run build

# Arrastra carpeta /dist a netlify.app/drop
```

---

## ✅ Checklist Final

### Para Workshop (Suficiente)
- ✅ App funciona en preview de Lovable
- ✅ Conecta con backend local (localhost:8000)
- ✅ Todas las features funcionan
- ✅ Código exportado y corriendo localmente

### Para Producción (Opcional)
- ✅ Backend desplegado públicamente
- ✅ Frontend desplegado en lovable.app o Vercel
- ✅ Variables de entorno configuradas
- ✅ URL pública funcional

---

## 🎓 Resumen del Módulo

Has aprendido:

✅ **Lovable Basics**: Qué es y cómo funciona  
✅ **Prompting**: Escribir prompts efectivos  
✅ **Build**: Construir chat conversacional completo  
✅ **Export**: Sincronizar GitHub y descargar código  
✅ **Deploy**: Limitaciones y opciones de deployment  

### Resultado

- 💬 App de chat funcional con IA
- 📦 Código React exportable y limpio
- 🎨 UI profesional generada con prompts
- 🔗 Integración con API REST
- 🚀 Listo para deploy o más desarrollo

---

## 🎯 Próximos Pasos

**Ahora puedes:**

1. **Personalizar**: Modifica colores, estilos, features
2. **Aprender React**: Estudia el código generado
3. **Extender**: Agrega features manualmente
4. **Comparar**: Prueba los otros módulos (Streamlit, Cursor, Dash)

---

**¡Felicitaciones! Has completado el módulo de Lovable 🎉**

**[← GitHub Export](./4_GITHUB_EXPORT.md)** | **[Volver al README](./README.md)**
