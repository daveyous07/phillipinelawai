"""
Philippine Law Assistant - FastAPI Application.
"""
from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.config import settings
from app.routes import chat, test, voice
from app.services.rag_service import rag_service


@asynccontextmanager
async def lifespan(app: FastAPI):
    """Startup: ensure RAG index exists."""
    rag_service.reindex_if_empty()
    yield
    # Shutdown: nothing to clean up


app = FastAPI(
    title="Philippine Law Assistant",
    description="Philippine law assistant (local Ollama by default; optional cloud Gemini via LLM_BACKEND)",
    version="1.0.0",
    lifespan=lifespan,
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173", "http://127.0.0.1:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(chat.router, prefix="/api/chat", tags=["chat"])
app.include_router(test.router, prefix="/api/test", tags=["test"])
app.include_router(voice.router, prefix="/api/voice", tags=["voice"])


@app.get("/")
async def root():
    return {"message": "Philippine Law Assistant API", "status": "ok"}


@app.get("/health")
async def health():
    return {"status": "healthy"}
