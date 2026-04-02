"""
RAG (Retrieval-Augmented Generation) Service.
Retrieves relevant Philippine law context for LLM augmentation.
"""
import os
from typing import List, Optional

import chromadb
from chromadb.config import Settings as ChromaSettings
from chromadb.utils import embedding_functions

from app.config import settings
from app.knowledge.ph_constitution import PH_CONSTITUTION_DOCUMENTS
from app.knowledge.ph_laws import PH_LAWS_DOCUMENTS


class RAGService:
    """Handles vector storage and retrieval of Philippine law documents."""

    COLLECTION_NAME = "philippine_laws"
    BATCH_SIZE = 32

    def __init__(self) -> None:
        self._client: Optional[chromadb.PersistentClient] = None
        self._collection = None
        self._embedding_fn = None

    def _get_client(self) -> chromadb.PersistentClient:
        """Lazy-initialize ChromaDB client and collection."""
        if self._client is None:
            os.makedirs(settings.chroma_persist_path, exist_ok=True)
            self._client = chromadb.PersistentClient(
                path=settings.chroma_persist_path,
                settings=ChromaSettings(anonymized_telemetry=False),
            )
            # Use Ollama embeddings if available, else sentence-transformers
            try:
                from chromadb.utils.embedding_functions import OllamaEmbeddingFunction
                self._embedding_fn = OllamaEmbeddingFunction(
                    url=settings.ollama_base_url,
                    model_name=settings.ollama_embedding_model,
                )
            except (ImportError, Exception):
                self._embedding_fn = embedding_functions.SentenceTransformerEmbeddingFunction(
                    model_name="paraphrase-multilingual-MiniLM-L12-v2"
                )
            self._collection = self._client.get_or_create_collection(
                name=self.COLLECTION_NAME,
                embedding_function=self._embedding_fn,
                metadata={"description": "Philippine Constitution and Laws"},
            )
        return self._client

    @property
    def collection(self):
        """Get or create the collection."""
        self._get_client()
        return self._collection

    def build_index(self) -> int:
        """
        Index all knowledge base documents. Returns count of indexed documents.
        Call this on first run or when documents change.
        """
        all_docs = PH_CONSTITUTION_DOCUMENTS + PH_LAWS_DOCUMENTS
        ids = [f"doc_{i}" for i in range(len(all_docs))]
        documents = [d["content"].strip() for d in all_docs]
        metadatas = [{"source": d["source"]} for d in all_docs]

        # ChromaDB handles batching internally for add
        self.collection.add(ids=ids, documents=documents, metadatas=metadatas)
        return len(all_docs)

    def reindex_if_empty(self) -> None:
        """Build index only if collection is empty."""
        if self.collection.count() == 0:
            self.build_index()

    def retrieve(self, query: str, top_k: Optional[int] = None) -> List[dict]:
        """
        Retrieve top-k most relevant chunks for a query.
        Returns list of dicts with 'content' and 'source'.
        """
        count = self.collection.count()
        if count == 0:
            return []
        k = top_k or settings.rag_top_k
        results = self.collection.query(
            query_texts=[query],
            n_results=min(k, count),
            include=["documents", "metadatas"],
        )
        if not results or not results["documents"] or not results["documents"][0]:
            return []
        out = []
        for i, doc in enumerate(results["documents"][0]):
            meta = results["metadatas"][0][i] if results["metadatas"] else {}
            out.append({"content": doc, "source": meta.get("source", "Unknown")})
        return out


# Singleton for app lifetime
rag_service = RAGService()
