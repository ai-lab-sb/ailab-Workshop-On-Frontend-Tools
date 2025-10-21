"""
API FastAPI para el agente de seguros con memoria.
"""

from contextlib import asynccontextmanager
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import Optional, List, Dict, Any
import os
from agent import InsuranceAgent

# Instancia global del agente
agent: Optional[InsuranceAgent] = None

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup
    global agent
    try:
        agent = InsuranceAgent()
        print("✅ Agente de seguros inicializado correctamente")
    except Exception as e:
        print(f"❌ Error al inicializar el agente: {e}")
        print("Verifica que GOOGLE_API_KEY esté configurada en el archivo .env")
        raise
    
    yield
    
    # Shutdown
    print("🔄 Cerrando agente de seguros")

app = FastAPI(
    title="SegurosVida+ API",
    description="API del asistente virtual de SegurosVida+ - Agente conversacional con memoria para información sobre seguros",
    version="1.0.0",
    lifespan=lifespan
)

# Configurar CORS para permitir requests desde frontends
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # En producción, especificar dominios específicos
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Modelos para requests y responses
class ChatRequest(BaseModel):
    message: str
    thread_id: Optional[str] = "default"

class ChatResponse(BaseModel):
    response: str
    thread_id: str

class HistoryResponse(BaseModel):
    history: List[Dict[str, Any]]


@app.get("/")
async def root():
    """Endpoint raíz con información de la API."""
    return {
        "service": "SegurosVida+ API",
        "status": "active",
        "description": "Asistente virtual de seguros con memoria conversacional",
        "endpoints": {
            "chat": "/chat",
            "history": "/history/{thread_id}",
            "health": "/health",
            "docs": "/docs"
        }
    }

@app.post("/chat", response_model=ChatResponse)
async def chat(request: ChatRequest):
    """
    Endpoint principal para chatear con el agente de seguros.
    
    El agente mantiene memoria de la conversación usando thread_id.
    Cada thread_id representa una conversación independiente.
    """
    global agent
    
    if agent is None:
        raise HTTPException(status_code=500, detail="Agente no inicializado")
    
    try:
        result = await agent.chat(request.message, request.thread_id)
        return ChatResponse(**result)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error al procesar mensaje: {str(e)}")

@app.get("/history/{thread_id}", response_model=HistoryResponse)
async def get_history(thread_id: str):
    """
    Obtiene el historial completo de conversación para un thread_id específico.
    
    Útil para revisar conversaciones previas o mostrar el historial en el frontend.
    """
    global agent
    
    if agent is None:
        raise HTTPException(status_code=500, detail="Agente no inicializado")
    
    try:
        history = await agent.get_conversation_history(thread_id)
        return HistoryResponse(history=history)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error al obtener historial: {str(e)}")

@app.get("/health")
async def health_check():
    """Endpoint de salud para verificar que el servicio está funcionando."""
    return {
        "status": "healthy",
        "service": "SegurosVida+ Insurance Agent API",
        "agent_ready": agent is not None
    }

if __name__ == "__main__":
    import uvicorn
    port = int(os.environ.get("PORT", 8000))
    uvicorn.run(app, host="0.0.0.0", port=port)
