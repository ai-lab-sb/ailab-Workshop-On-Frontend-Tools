# 🚀 Prompt 1: Initial Project Setup

Copia este prompt para que Cursor te ayude a crear el proyecto inicial.

---

## 📋 Objetivo

Crear un proyecto Next.js 14 con TypeScript, Tailwind CSS, y Shadcn/ui configurado.

---

## 💬 Prompt para Cursor

```markdown
Create a new Next.js 14 project with the following setup:

Project name: seguros-chat

Configuration:
- Use App Router (not Pages Router)
- Enable TypeScript
- Include Tailwind CSS
- Use src/ directory structure
- Include ESLint
- Do NOT use the default Next.js font optimization

Guide me through running:
npx create-next-app@latest seguros-chat --typescript --tailwind --eslint --app --src-dir

Then explain the project structure created and what each folder is for.
```

---

## 🎯 Expected Output

Cursor should:
1. Show you the command to run
2. Explain the folder structure
3. Confirm dependencies installed

---

## ✅ Checkpoint

Verify:
```bash
cd seguros-chat
npm run dev
# Should start on http://localhost:3000
```

---

## ➡️ Next Steps

After project is created:
- Install Shadcn/ui components
- Configure environment variables
- Setup Tailwind theme colors

Continue to **Prompt 2: UI Components Setup**

