"""
Chat API - Text-based conversation with RAG-augmented LLM.
"""
from typing import List, Optional

from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

from app.services.llm_service import llm_service

router = APIRouter()


class ChatRequest(BaseModel):
    message: str
    history: List[dict] = []


class ChatResponse(BaseModel):
    response: str


class ChatStreamResponse(BaseModel):
    """SSE chunk - actual streaming done via StreamResponse."""


@router.post("", response_model=ChatResponse)
async def chat(request: ChatRequest) -> ChatResponse:
    """Non-streaming chat. Returns full response."""
    if not request.message.strip():
        raise HTTPException(status_code=400, detail="Message cannot be empty")
    response = await llm_service.chat(
        message=request.message.strip(),
        history=request.history or [],
    )
    return ChatResponse(response=response)


@router.post("/stream")
async def chat_stream(request: ChatRequest):
    """Streaming chat via Server-Sent Events."""
    from fastapi.responses import StreamingResponse

    if not request.message.strip():
        raise HTTPException(status_code=400, detail="Message cannot be empty")

    async def generate():
        async for chunk in llm_service.chat_stream(
            message=request.message.strip(),
            history=request.history or [],
        ):
            yield f"data: {chunk}\n\n"

    return StreamingResponse(
        generate(),
        media_type="text/event-stream",
        headers={"Cache-Control": "no-cache", "Connection": "keep-alive"},
    )
