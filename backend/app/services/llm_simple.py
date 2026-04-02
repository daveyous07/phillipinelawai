"""
LLM Service — default is local Ollama. Set LLM_BACKEND=gemini only for the online Google API.
"""
import json
from typing import Iterator, List

import requests

from app.config_slim import GEMINI_MODEL, LLM_BACKEND, OLLAMA_BASE_URL, OLLAMA_MODEL
from app.prompts import PHILIPPINE_LAW_TUTOR_SYSTEM
from app.services.gemini_client import generate_content_sync, stream_content_sync
from app.services.rag_simple import retrieve

SYSTEM_PROMPT = PHILIPPINE_LAW_TUTOR_SYSTEM

OLLAMA_OPTIONS = {
    "num_predict": 512,
    "temperature": 0.6,
    "repeat_penalty": 1.1,
    "top_p": 0.9,
}


def _build_context(retrieved: List[dict]) -> str:
    if not retrieved:
        return ""
    parts = ["Relevant provisions (cite these only):\n"]
    for r in retrieved:
        raw = str(r.get("content", ""))
        content = " ".join(raw.split())
        parts.append(f"[{r['source']}]\n{content}\n")
    return "\n".join(parts)


def _limit_history(history: List[dict], max_turns: int = 4) -> List[dict]:
    if not history or len(history) <= max_turns:
        return history or []
    return history[-max_turns:]


def _ollama_chat(message: str, history: List[dict], use_rag: bool = True) -> str:
    context = ""
    if use_rag:
        retrieved = retrieve(message, top_k=5)
        context = _build_context(retrieved)
    user_message = f"{context}\n\nUser question: {message}" if context else message

    messages = [
        {"role": "system", "content": SYSTEM_PROMPT},
        *[{"role": h["role"], "content": h["content"]} for h in _limit_history(history or [])],
        {"role": "user", "content": user_message},
    ]
    try:
        r = requests.post(
            f"{OLLAMA_BASE_URL}/api/chat",
            json={
                "model": OLLAMA_MODEL,
                "messages": messages,
                "stream": False,
                "options": OLLAMA_OPTIONS,
            },
            timeout=120,
        )
        r.raise_for_status()
        data = r.json()
        return data.get("message", {}).get("content", "") or ""
    except Exception as e:
        return f"I encountered an error: {str(e)}. Is Ollama running? Try `ollama serve` and `ollama pull {OLLAMA_MODEL}`."


def _gemini_chat(message: str, history: List[dict], use_rag: bool = True) -> str:
    context = ""
    if use_rag:
        retrieved = retrieve(message, top_k=5)
        context = _build_context(retrieved)
    user_message = f"{context}\n\nUser question: {message}" if context else message

    messages = [
        {"role": "system", "content": SYSTEM_PROMPT},
        *[{"role": h["role"], "content": h["content"]} for h in _limit_history(history or [])],
        {"role": "user", "content": user_message},
    ]
    return generate_content_sync(GEMINI_MODEL, messages).strip()


def chat(message: str, history: List[dict], use_rag: bool = True) -> str:
    if LLM_BACKEND == "ollama":
        return _ollama_chat(message, history, use_rag)
    return _gemini_chat(message, history, use_rag)


def _ollama_chat_stream(message: str, history: List[dict], use_rag: bool = True) -> Iterator[str]:
    context = ""
    if use_rag:
        retrieved = retrieve(message, top_k=5)
        context = _build_context(retrieved)
    user_message = f"{context}\n\nUser question: {message}" if context else message

    messages = [
        {"role": "system", "content": SYSTEM_PROMPT},
        *[{"role": h["role"], "content": h["content"]} for h in _limit_history(history or [])],
        {"role": "user", "content": user_message},
    ]
    try:
        r = requests.post(
            f"{OLLAMA_BASE_URL}/api/chat",
            json={
                "model": OLLAMA_MODEL,
                "messages": messages,
                "stream": True,
                "options": OLLAMA_OPTIONS,
            },
            stream=True,
            timeout=120,
        )
        r.raise_for_status()
        for line in r.iter_lines(decode_unicode=True):
            if line is None or not line.strip():
                continue
            if isinstance(line, bytes):
                line = line.decode("utf-8", errors="replace")
            try:
                j = json.loads(line)
                content = j.get("message", {}).get("content", "")
                if content:
                    yield content
                if j.get("done"):
                    break
            except json.JSONDecodeError:
                pass
    except Exception as e:
        yield f"I encountered an error: {str(e)}. Is Ollama running?"


def _gemini_chat_stream(message: str, history: List[dict], use_rag: bool = True) -> Iterator[str]:
    context = ""
    if use_rag:
        retrieved = retrieve(message, top_k=5)
        context = _build_context(retrieved)
    user_message = f"{context}\n\nUser question: {message}" if context else message

    messages = [
        {"role": "system", "content": SYSTEM_PROMPT},
        *[{"role": h["role"], "content": h["content"]} for h in _limit_history(history or [])],
        {"role": "user", "content": user_message},
    ]
    yield from stream_content_sync(GEMINI_MODEL, messages)


def chat_stream(message: str, history: List[dict], use_rag: bool = True) -> Iterator[str]:
    if LLM_BACKEND == "ollama":
        yield from _ollama_chat_stream(message, history, use_rag)
    else:
        yield from _gemini_chat_stream(message, history, use_rag)


def _ollama_chat_for_test(prompt: str, system: str = "") -> str:
    messages = [{"role": "system", "content": system or "You are a Philippine law exam writer."}, {"role": "user", "content": prompt}]
    try:
        r = requests.post(
            f"{OLLAMA_BASE_URL}/api/chat",
            json={"model": OLLAMA_MODEL, "messages": messages, "stream": False},
            timeout=120,
        )
        r.raise_for_status()
        return r.json().get("message", {}).get("content", "") or ""
    except Exception as e:
        return str(e)


def _gemini_chat_for_test(prompt: str, system: str = "") -> str:
    messages = [{"role": "system", "content": system or "You are a Philippine law exam writer."}, {"role": "user", "content": prompt}]
    return generate_content_sync(GEMINI_MODEL, messages).strip()


def chat_for_test(prompt: str, system: str = "") -> str:
    if LLM_BACKEND == "ollama":
        return _ollama_chat_for_test(prompt, system)
    return _gemini_chat_for_test(prompt, system)
