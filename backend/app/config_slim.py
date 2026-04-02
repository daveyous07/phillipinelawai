"""
Simple config - no pydantic. Works with any Python.

LLM backends (important: only one is fully local):
  - ollama — DEFAULT. Runs on your PC via Ollama; no LLM traffic to Google/cloud.
    For Google's open-weight family locally, use e.g. OLLAMA_MODEL=gemma3 (after ollama pull gemma3).
  - gemini — Calls Google's Gemini API over the internet (NOT local). Requires GOOGLE_API_KEY.
    Colab/notebook tutorials often use this same API; it always goes online.
"""
import os

# "ollama" = local (default). "gemini" = cloud API only.
LLM_BACKEND = os.environ.get("LLM_BACKEND", "ollama").strip().lower()

OLLAMA_BASE_URL = os.environ.get("OLLAMA_BASE_URL", "http://localhost:11434")
OLLAMA_MODEL = os.environ.get("OLLAMA_MODEL", "llama3.2")
# Local Google open models: gemma3, gemma2, etc. (ollama pull <name>)

# Cloud only — https://aistudio.google.com/apikey
GEMINI_MODEL = os.environ.get("GEMINI_MODEL", "gemini-2.0-flash")
