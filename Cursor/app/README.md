# Seguros Bolívar Chat - Next.js App

This is the reference implementation of the Seguros Bolívar Chat application built with Next.js 14, TypeScript, and Tailwind CSS.

## 🚀 Getting Started

### Prerequisites

- Node.js 18+ installed
- Backend API running on http://localhost:8000

### Installation

```bash
# Install dependencies
npm install

# Setup environment variables
cp .env.example .env.local
# Edit .env.local with your API URL
```

### Development

```bash
# Run development server
npm run dev

# Open http://localhost:3000
```

### Build

```bash
# Create production build
npm run build

# Start production server
npm start
```

### Docker

```bash
# Build Docker image
docker build -t seguros-chat .

# Run container
docker run -p 3000:3000 -e NEXT_PUBLIC_API_URL=http://localhost:8000 seguros-chat
```

## 📁 Project Structure

```
src/
├── app/                    # Next.js App Router
│   ├── layout.tsx         # Root layout
│   ├── page.tsx           # Home page
│   └── globals.css        # Global styles
│
├── components/            # React components
│   └── chat/
│       ├── ChatContainer.tsx
│       ├── MessageList.tsx
│       ├── MessageBubble.tsx
│       └── InputArea.tsx
│
├── hooks/                 # Custom React hooks
│   └── useChat.ts
│
├── lib/                   # Utilities
│   └── api.ts
│
└── types/                 # TypeScript types
    └── chat.ts
```

## 🎨 Features

- ✅ Real-time chat with AI agent
- ✅ Responsive design
- ✅ Loading states
- ✅ Error handling
- ✅ Auto-scroll to latest message
- ✅ Character counter
- ✅ Keyboard shortcuts (Cmd+Enter to send)
- ✅ Seguros Bolívar branding
- ✅ TypeScript throughout
- ✅ Accessibility features

## 🛠️ Tech Stack

- **Framework**: Next.js 14 (App Router)
- **Language**: TypeScript
- **Styling**: Tailwind CSS
- **UI Components**: Custom components
- **State Management**: React hooks
- **API Client**: Fetch API

## 🎯 Environment Variables

```env
NEXT_PUBLIC_API_URL=http://localhost:8000
```

## 📝 Scripts

- `npm run dev` - Start development server
- `npm run build` - Build for production
- `npm start` - Start production server
- `npm run lint` - Run ESLint
- `npm run type-check` - Check TypeScript types

## 🐛 Troubleshooting

### API Connection Issues

If you can't connect to the backend:

1. Verify backend is running: `curl http://localhost:8000/health`
2. Check `.env.local` has correct API URL
3. Restart the development server

### Build Errors

If build fails:

1. Delete `.next` folder: `rm -rf .next`
2. Delete `node_modules`: `rm -rf node_modules`
3. Reinstall: `npm install`
4. Try build again: `npm run build`

## 📄 License

This project is part of the FrontEnd Tools Workshop.

## 🤝 Contributing

This is a reference implementation for educational purposes. Feel free to use it as a template for your own projects!

---

Built with ❤️ using Cursor AI

