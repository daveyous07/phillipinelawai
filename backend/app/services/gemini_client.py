"""
Google Gemini **cloud** API (Google AI Studio). Requests go to Google over the internet — not local.

For a **local** Google-affiliated model, use LLM_BACKEND=ollama and a Gemma model (e.g. OLLAMA_MODEL=gemma3).

Uses REST in sync paths (Flask slim); httpx for async (FastAPI).
"""
from __future__ import annotations

import json
from typing import Any, AsyncGenerator, Dict, Iterator, List, Optional, Tuple

import requests

# Async path (FastAPI) — import lazily inside async functions if missing
try:
    import httpx
except ImportError:  # pragma: no cover - slim stack has no httpx
    httpx = None  # type: ignore

GEMINI_REST_BASE = "https://generativelanguage.googleapis.com/v1beta"

# Aligned with former Ollama tuning where possible
DEFAULT_GENERATION_CONFIG = {
    "temperature": 0.6,
    "topP": 0.9,
    "maxOutputTokens": 512,
}


def _api_key(explicit: Optional[str] = None) -> str:
    import os

    if explicit:
        return explicit.strip()
    return (os.environ.get("GOOGLE_API_KEY") or os.environ.get("GEMINI_API_KEY") or "").strip()


def ollama_style_messages_to_gemini(
    messages: List[Dict[str, str]],
) -> Tuple[Optional[Dict[str, Any]], List[Dict[str, Any]]]:
    """Split system message from Ollama/OpenAI-style list into Gemini systemInstruction + contents."""
    system_instruction: Optional[Dict[str, Any]] = None
    rest = messages
    if messages and messages[0].get("role") == "system":
        system_instruction = {"parts": [{"text": messages[0].get("content", "")}]}
        rest = messages[1:]
    contents: List[Dict[str, Any]] = []
    for m in rest:
        role = m.get("role", "")
        text = m.get("content", "")
        if role == "user":
            contents.append({"role": "user", "parts": [{"text": text}]})
        elif role == "assistant":
            contents.append({"role": "model", "parts": [{"text": text}]})
    return system_instruction, contents


def _generate_payload(messages: List[Dict[str, str]], generation_config: Optional[dict] = None) -> dict:
    system_instruction, contents = ollama_style_messages_to_gemini(messages)
    body: Dict[str, Any] = {
        "contents": contents,
        "generationConfig": generation_config or DEFAULT_GENERATION_CONFIG,
    }
    if system_instruction:
        body["systemInstruction"] = system_instruction
    return body


def _extract_text_from_response(data: dict) -> str:
    candidates = data.get("candidates") or []
    if not candidates:
        return ""
    parts = (candidates[0].get("content") or {}).get("parts") or []
    texts = [p.get("text", "") for p in parts if isinstance(p, dict)]
    return "".join(texts)


def generate_content_sync(
    model: str,
    messages: List[Dict[str, str]],
    api_key: Optional[str] = None,
    timeout: int = 120,
) -> str:
    key = _api_key(api_key)
    if not key:
        return (
            "Missing API key. Create one at Google AI Studio (https://aistudio.google.com/apikey) "
            "and set GOOGLE_API_KEY or GEMINI_API_KEY. To use local Ollama instead, set LLM_BACKEND=ollama."
        )
    url = f"{GEMINI_REST_BASE}/models/{model}:generateContent"
    body = _generate_payload(messages)
    try:
        r = requests.post(url, params={"key": key}, json=body, timeout=timeout)
        r.raise_for_status()
        return _extract_text_from_response(r.json()) or ""
    except requests.HTTPError as e:
        detail = ""
        try:
            detail = e.response.text[:500] if e.response is not None else ""
        except Exception:
            pass
        return f"Gemini API error ({e}): {detail}. Check GEMINI_MODEL and API key."
    except Exception as e:
        return f"Gemini request failed: {e}"


def stream_content_sync(
    model: str,
    messages: List[Dict[str, str]],
    api_key: Optional[str] = None,
    timeout: int = 120,
) -> Iterator[str]:
    key = _api_key(api_key)
    if not key:
        yield (
            "Missing API key. Set GOOGLE_API_KEY (Google AI Studio). "
            "Or set LLM_BACKEND=ollama for local Ollama."
        )
        return
    url = f"{GEMINI_REST_BASE}/models/{model}:streamGenerateContent"
    body = _generate_payload(messages)
    try:
        with requests.post(
            url,
            params={"key": key, "alt": "sse"},
            json=body,
            stream=True,
            timeout=timeout,
        ) as r:
            r.raise_for_status()
            for raw in r.iter_lines(decode_unicode=True):
                if not raw:
                    continue
                line = raw if isinstance(raw, str) else raw.decode("utf-8", errors="replace")
                if line.startswith("data: "):
                    payload = line[6:].strip()
                    if payload in ("", "[DONE]"):
                        continue
                    try:
                        chunk = json.loads(payload)
                        piece = _extract_text_from_response(chunk)
                        if piece:
                            yield piece
                    except json.JSONDecodeError:
                        continue
    except requests.HTTPError as e:
        yield f"Gemini stream error: {e}"
    except Exception as e:
        yield f"Gemini stream failed: {e}"


async def generate_content_async(
    model: str,
    messages: List[Dict[str, str]],
    api_key: Optional[str] = None,
    timeout: int = 120,
) -> str:
    if httpx is None:
        return "Install httpx for FastAPI + Gemini: pip install httpx"
    key = _api_key(api_key)
    if not key:
        return (
            "Missing API key. Set GOOGLE_API_KEY or GEMINI_API_KEY. "
            "Or set LLM_BACKEND=ollama for local Ollama."
        )
    url = f"{GEMINI_REST_BASE}/models/{model}:generateContent"
    body = _generate_payload(messages)
    try:
        async with httpx.AsyncClient(timeout=timeout) as client:
            r = await client.post(url, params={"key": key}, json=body)
            r.raise_for_status()
            return _extract_text_from_response(r.json()) or ""
    except httpx.HTTPStatusError as e:
        detail = ""
        try:
            detail = e.response.text[:500]
        except Exception:
            pass
        return f"Gemini API error: {detail}"
    except Exception as e:
        return f"Gemini request failed: {e}"


async def stream_content_async(
    model: str,
    messages: List[Dict[str, str]],
    api_key: Optional[str] = None,
    timeout: int = 120,
) -> AsyncGenerator[str, None]:
    if httpx is None:
        yield "Install httpx for streaming Gemini with FastAPI: pip install httpx"
        return
    key = _api_key(api_key)
    if not key:
        yield "Missing GOOGLE_API_KEY. Or use LLM_BACKEND=ollama."
        return
    url = f"{GEMINI_REST_BASE}/models/{model}:streamGenerateContent"
    body = _generate_payload(messages)
    try:
        async with httpx.AsyncClient(timeout=timeout) as client:
            async with client.stream("POST", url, params={"key": key, "alt": "sse"}, json=body) as r:
                r.raise_for_status()
                async for line in r.aiter_lines():
                    if not line or not line.startswith("data: "):
                        continue
                    payload = line[6:].strip()
                    if payload in ("", "[DONE]"):
                        continue
                    try:
                        chunk = json.loads(payload)
                        piece = _extract_text_from_response(chunk)
                        if piece:
                            yield piece
                    except json.JSONDecodeError:
                        continue
    except httpx.HTTPStatusError as e:
        yield f"Gemini stream error: {e}"
    except Exception as e:
        yield f"Gemini stream failed: {e}"
