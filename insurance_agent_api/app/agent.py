"""
Agente de seguros con memoria usando LangGraph y Gemini 2.5 Flash.
Este agente responde preguntas sobre una empresa ficticia de seguros.
"""

import os
from typing import List, Dict, Any
from langchain_core.messages import HumanMessage, SystemMessage, BaseMessage
from langchain_google_genai import ChatGoogleGenerativeAI
from langgraph.graph import StateGraph, START, MessagesState
from langgraph.checkpoint.memory import MemorySaver
from dotenv import load_dotenv
from prompts import INSURANCE_AGENT_SYSTEM_PROMPT

# Cargar variables de entorno desde .env
load_dotenv()


class InsuranceAgent:
    """
    Agente conversacional con memoria especializado en seguros.
    Representa a "SegurosVida+", una empresa ficticia de seguros.
    """
    
    def __init__(self, google_api_key: str = None):
        """
        Inicializa el agente de seguros.
        
        Args:
            google_api_key: API key de Google para Gemini
        """
        if google_api_key:
            os.environ["GOOGLE_API_KEY"] = google_api_key
        elif not os.environ.get("GOOGLE_API_KEY"):
            raise ValueError("Se requiere GOOGLE_API_KEY")
        
        # Inicializar modelo Gemini 2.5 Flash
        self.llm = ChatGoogleGenerativeAI(
            model="gemini-2.5-flash",
            temperature=0
        )
        
        # Configurar memoria
        self.memory = MemorySaver()
        
        # Mensaje del sistema con información de la empresa
        self.system_message = SystemMessage(content=INSURANCE_AGENT_SYSTEM_PROMPT)
        
        # Construir el grafo
        self._build_graph()
    
    def _build_graph(self):
        """Construye el grafo de conversación con memoria."""
        
        def assistant_node(state: MessagesState) -> Dict[str, List[BaseMessage]]:
            """Nodo del asistente que procesa mensajes."""
            messages = [self.system_message] + state["messages"]
            response = self.llm.invoke(messages)
            return {"messages": [response]}
        
        # Crear el grafo
        builder = StateGraph(MessagesState)
        builder.add_node("assistant", assistant_node)
        builder.add_edge(START, "assistant")
        
        # Compilar con memoria
        self.graph = builder.compile(checkpointer=self.memory)
    
    async def chat(self, message: str, thread_id: str = "default") -> Dict[str, Any]:
        """
        Procesa un mensaje del usuario.
        
        Args:
            message: Mensaje del usuario
            thread_id: ID del hilo de conversación
            
        Returns:
            Respuesta del agente
        """
        config = {"configurable": {"thread_id": thread_id}}
        human_message = HumanMessage(content=message)
        
        # Ejecutar el grafo
        result = await self.graph.ainvoke({"messages": [human_message]}, config)
        
        # Extraer la última respuesta del asistente
        last_ai_message = None
        for msg in reversed(result["messages"]):
            if hasattr(msg, 'type') and msg.type == 'ai':
                last_ai_message = msg
                break
        
        return {
            "response": last_ai_message.content if last_ai_message else "No se pudo generar respuesta",
            "thread_id": thread_id
        }
    
    async def get_conversation_history(self, thread_id: str = "default") -> List[Dict[str, Any]]:
        """Obtiene el historial de conversación."""
        config = {"configurable": {"thread_id": thread_id}}
        
        try:
            state = self.graph.get_state(config)
            
            if not state.values or "messages" not in state.values:
                return []
            
            history = []
            for msg in state.values["messages"]:
                history.append({
                    "type": msg.type,
                    "content": msg.content
                })
            
            return history
        
        except Exception:
            return []
