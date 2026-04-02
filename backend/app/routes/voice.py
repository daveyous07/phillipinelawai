"""
Voice API - Accept transcribed text (voice input handled client-side via Web Speech API).
Returns text response; TTS handled client-side via SpeechSynthesis.
"""
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

from app.services.llm_service import llm_service

router = APIRouter()


class VoiceChatRequest(BaseModel):
    """Voice flow: client sends transcribed text from Web Speech API."""
    message: str
    history: list = []


@router.post("/chat")
async def voice_chat(request: VoiceChatRequest):
    """
    Chat endpoint for voice mode.
    Client uses Web Speech API for speech-to-text, sends text here,
    receives text response. Client uses SpeechSynthesis for TTS.
    """
    if not request.message or not request.message.strip():
        raise HTTPException(status_code=400, detail="Message cannot be empty")
    response = await llm_service.chat(
        message=request.message.strip(),
        history=request.history or [],
    )
    return {"response": response}
