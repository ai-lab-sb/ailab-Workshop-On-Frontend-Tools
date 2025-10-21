import type { Metadata } from "next";
import "./globals.css";

export const metadata: Metadata = {
  title: "Seguros Bolívar - Chat con IA",
  description: "Asistente virtual de seguros powered by inteligencia artificial. Obtén información sobre seguros de vida, auto, hogar, salud y más.",
};

export default function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode;
}>) {
  return (
    <html lang="es">
      <body className="antialiased">
        <main className="min-h-screen">
          {children}
        </main>
        <footer className="py-6 text-center text-sm text-gray-500 bg-gray-50">
          © 2024 Seguros Bolívar | Powered by Cursor AI
        </footer>
      </body>
    </html>
  );
}

