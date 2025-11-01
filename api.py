"""
FastAPI web service for the LangChain chatbot.
Run with: uvicorn api:app --reload
"""
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Field
from typing import Optional, List
from main import ChatBot
import uuid

app = FastAPI(
    title="LangChain AI Agent API",
    description="RESTful API for the LangChain chatbot with tool integration",
    version="1.0.0"
)

# CORS middleware for web clients
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Store active chat sessions
chat_sessions = {}


class ChatMessage(BaseModel):
    """Single chat message."""
    message: str = Field(..., description="The user's message")
    session_id: Optional[str] = Field(None, description="Optional session ID for conversation continuity")


class ChatResponse(BaseModel):
    """Chat response model."""
    response: str = Field(..., description="The AI's response")
    session_id: str = Field(..., description="Session ID for this conversation")


class SessionInfo(BaseModel):
    """Session information."""
    session_id: str
    message_count: int
    created_at: str


@app.get("/")
async def root():
    """API root endpoint."""
    return {
        "message": "LangChain AI Agent API",
        "version": "1.0.0",
        "endpoints": {
            "chat": "/chat",
            "new_session": "/session/new",
            "get_session": "/session/{session_id}",
            "clear_session": "/session/{session_id}/clear",
            "list_sessions": "/sessions",
            "health": "/health"
        }
    }


@app.get("/health")
async def health_check():
    """Health check endpoint."""
    return {"status": "healthy", "sessions": len(chat_sessions)}


@app.post("/chat", response_model=ChatResponse)
async def chat(message: ChatMessage):
    """
    Send a message and get a response.
    
    - **message**: The user's message
    - **session_id**: Optional session ID to continue a conversation
    """
    try:
        # Get or create session
        session_id = message.session_id or str(uuid.uuid4())
        
        if session_id not in chat_sessions:
            chat_sessions[session_id] = {
                "bot": ChatBot(),
                "created_at": str(uuid.uuid1().time)
            }
        
        bot = chat_sessions[session_id]["bot"]
        
        # Get response
        response = bot.chat(message.message)
        
        return ChatResponse(
            response=response,
            session_id=session_id
        )
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.post("/session/new")
async def create_session():
    """Create a new chat session."""
    session_id = str(uuid.uuid4())
    chat_sessions[session_id] = {
        "bot": ChatBot(),
        "created_at": str(uuid.uuid1().time)
    }
    
    return {
        "session_id": session_id,
        "message": "New session created"
    }


@app.get("/session/{session_id}")
async def get_session(session_id: str):
    """Get information about a specific session."""
    if session_id not in chat_sessions:
        raise HTTPException(status_code=404, detail="Session not found")
    
    bot = chat_sessions[session_id]["bot"]
    
    return {
        "session_id": session_id,
        "message_count": len(bot.get_history()),
        "created_at": chat_sessions[session_id]["created_at"]
    }


@app.delete("/session/{session_id}/clear")
async def clear_session(session_id: str):
    """Clear the chat history for a session."""
    if session_id not in chat_sessions:
        raise HTTPException(status_code=404, detail="Session not found")
    
    bot = chat_sessions[session_id]["bot"]
    bot.clear_history()
    
    return {"message": "Session history cleared"}


@app.delete("/session/{session_id}")
async def delete_session(session_id: str):
    """Delete a chat session."""
    if session_id not in chat_sessions:
        raise HTTPException(status_code=404, detail="Session not found")
    
    del chat_sessions[session_id]
    
    return {"message": "Session deleted"}


@app.get("/sessions")
async def list_sessions():
    """List all active sessions."""
    return {
        "sessions": [
            {
                "session_id": sid,
                "message_count": len(data["bot"].get_history()),
                "created_at": data["created_at"]
            }
            for sid, data in chat_sessions.items()
        ]
    }


@app.get("/session/{session_id}/history")
async def get_history(session_id: str):
    """Get the chat history for a session."""
    if session_id not in chat_sessions:
        raise HTTPException(status_code=404, detail="Session not found")
    
    bot = chat_sessions[session_id]["bot"]
    history = bot.get_history()
    
    return {
        "session_id": session_id,
        "history": [
            {
                "role": "user" if i % 2 == 0 else "assistant",
                "content": msg.content
            }
            for i, msg in enumerate(history)
        ]
    }


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
