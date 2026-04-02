"""
LLM Service — default local Ollama; optional cloud Gemini when llm_backend=gemini.
"""
from typing import AsyncGenerator, List

from ollama import AsyncClient

from app.config import settings
from app.prompts import PHILIPPINE_LAW_TUTOR_SYSTEM
from app.services.gemini_client import generate_content_async, stream_content_async
from app.services.rag_service import rag_service

SYSTEM_PROMPT = PHILIPPINE_LAW_TUTOR_SYSTEM

TEST_SYSTEM_PROMPT = """You are a Philippine law exam simulator. Generate practice questions 
that test understanding of the 1987 Constitution and Philippine laws. Format questions 
clearly. Provide 4 options (A, B, C, D) with exactly one correct answer. Be precise and 
academically rigorous."""


class LLMService:
    """RAG-augmented chat; backend selected by llm_backend."""

    def __init__(self) -> None:
        self._ollama = AsyncClient(host=settings.ollama_base_url)

    def _build_context(self, retrieved: List[dict]) -> str:
        if not retrieved:
            return ""
        parts = ["Relevant provisions:\n"]
        for r in retrieved:
            parts.append(f"[{r['source']}]\n{r['content']}\n")
        return "\n".join(parts)

    def _messages(self, message: str, history: List[dict], use_rag: bool) -> List[dict]:
        context = ""
        if use_rag:
            retrieved = rag_service.retrieve(message)
            context = self._build_context(retrieved)
        user_message = f"{context}\n\nUser question: {message}" if context else message
        return [
            {"role": "system", "content": SYSTEM_PROMPT},
            *[{"role": h["role"], "content": h["content"]} for h in history],
            {"role": "user", "content": user_message},
        ]

    async def chat(self, message: str, history: List[dict], use_rag: bool = True) -> str:
        messages = self._messages(message, history, use_rag)
        if settings.llm_backend.strip().lower() == "ollama":
            try:
                response = await self._ollama.chat(model=settings.ollama_model, messages=messages)
                return response.message.content or ""
            except Exception as e:
                return (
                    f"I encountered an error: {str(e)}. Is Ollama running? "
                    f"Try `ollama serve` and `ollama pull {settings.ollama_model}`."
                )
        return await generate_content_async(
            settings.gemini_model,
            messages,
            api_key=settings.google_api_key or None,
        )

    async def chat_stream(
        self,
        message: str,
        history: List[dict],
        use_rag: bool = True,
    ) -> AsyncGenerator[str, None]:
        messages = self._messages(message, history, use_rag)
        if settings.llm_backend.strip().lower() == "ollama":
            try:
                stream = await self._ollama.chat(
                    model=settings.ollama_model,
                    messages=messages,
                    stream=True,
                )
                async for chunk in stream:
                    if chunk.message and chunk.message.content:
                        yield chunk.message.content
            except Exception as e:
                yield f"I encountered an error: {str(e)}. Is Ollama running?"
            return

        async for piece in stream_content_async(
            settings.gemini_model,
            messages,
            api_key=settings.google_api_key or None,
        ):
            yield piece


llm_service = LLMService()
