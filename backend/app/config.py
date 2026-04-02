"""
Application configuration - centralized settings for maintainability.
"""
from pydantic import AliasChoices, Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """Application settings loaded from environment or .env."""

    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8", extra="ignore")

    # LLM routing: ollama (local, default) | gemini (cloud API only, requires key)
    llm_backend: str = Field(default="ollama", validation_alias=AliasChoices("LLM_BACKEND"))
    gemini_model: str = Field(default="gemini-2.0-flash", validation_alias=AliasChoices("GEMINI_MODEL"))
    google_api_key: str = Field(
        default="",
        validation_alias=AliasChoices("GOOGLE_API_KEY", "GEMINI_API_KEY"),
    )

    # Ollama
    ollama_base_url: str = "http://localhost:11434"
    ollama_model: str = "llama3.2"
    ollama_embedding_model: str = "nomic-embed-text"

    # RAG
    rag_top_k: int = 5
    rag_chunk_size: int = 512
    rag_chunk_overlap: int = 128

    # Paths
    knowledge_base_path: str = "knowledge_base"
    chroma_persist_path: str = "data/chroma_db"


settings = Settings()
