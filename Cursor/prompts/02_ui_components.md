# 🎨 Prompt 2: UI Components Setup

Prompts para configurar Shadcn/ui y componentes base.

---

## Part A: Install Shadcn/ui

### 💬 Prompt para Cursor

```markdown
I need to add Shadcn/ui to this Next.js project.

Steps:
1. Explain what Shadcn/ui is and why it's useful
2. Guide me through running: npx shadcn@latest init
3. Recommend configuration options for Next.js App Router
4. Install these essential components:
   - button
   - card
   - input
   - textarea

Show me the exact commands to run.
```

### ✅ Checkpoint

```bash
# Components should be in:
src/components/ui/button.tsx
src/components/ui/card.tsx
src/components/ui/input.tsx
src/components/ui/textarea.tsx
```

---

## Part B: Configure Tailwind Colors

### 💬 Prompt para Cursor

```markdown
Update the Tailwind config to include Seguros Bolívar corporate colors.

File: @file:tailwind.config.ts

Add to theme.extend.colors:
- bolivar-green: '#00A651'
- bolivar-green-dark: '#008040'
- bolivar-yellow: '#FFD100'
- bolivar-yellow-dark: '#E6BC00'

Also add to theme.extend:
- Animation for message fade-in
- Custom box shadows for cards

Keep all existing configuration, just extend it.
```

---

## Part C: Global Styles

### 💬 Prompt para Cursor

```markdown
Update the globals.css file with custom styles for our chat app.

File: @file:src/app/globals.css

Keep the existing Tailwind directives (@tailwind base, etc.)

Add custom styles:
1. Body: white background, smooth scrolling behavior
2. Custom scrollbar styling:
   - Thin scrollbar (8px width)
   - Track: light gray
   - Thumb: gradient from bolivar-green to bolivar-yellow
   - Hover: darker shade
3. Animation keyframes:
   - fadeIn: opacity 0 to 1, translateY 10px to 0
   - slideIn: translateX -20px to 0
   - bounce: for loading dots
4. Chat message animations

Use CSS variables and modern CSS features.
```

---

## ✅ Checkpoint

Your app should now have:
- ✅ Shadcn components installed
- ✅ Custom theme colors
- ✅ Global styles and animations

Test by running:
```bash
npm run dev
```

---

## ➡️ Next Steps

Now you're ready to create the chat components!

Continue to **Prompt 3: API Integration**

