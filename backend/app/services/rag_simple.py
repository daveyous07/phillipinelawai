"""
Simple RAG - Keyword-based retrieval. No ChromaDB, no embeddings.
Works with any Python version.
"""
from typing import List

from app.knowledge.ph_constitution import PH_CONSTITUTION_DOCUMENTS
from app.knowledge.ph_laws import PH_LAWS_DOCUMENTS
from app.knowledge.ph_shariah import PH_SHARIAH_DOCUMENTS
from app.knowledge.ph_legalhub import PH_LEGALHUB_DOCUMENTS
from app.knowledge.ph_lawphil import PH_LAWPHIL_DOCUMENTS
from app.knowledge.jd_curriculum import JD_CURRICULUM_DOCUMENTS
from app.knowledge.ph_cases import PH_CASES_DOCUMENTS
from app.knowledge.ph_academic import PH_ACADEMIC_DOCUMENTS
from app.knowledge.ph_interpretations import PH_INTERPRETATIONS_DOCUMENTS

ALL_DOCS = (
    PH_CONSTITUTION_DOCUMENTS
    + PH_LAWS_DOCUMENTS
    + PH_SHARIAH_DOCUMENTS
    + PH_LEGALHUB_DOCUMENTS
    + PH_LAWPHIL_DOCUMENTS
    + JD_CURRICULUM_DOCUMENTS
    + PH_CASES_DOCUMENTS
    + PH_ACADEMIC_DOCUMENTS
    + PH_INTERPRETATIONS_DOCUMENTS
)


def _normalize_query(query: str) -> str:
    """Expand common legal abbreviations for better matching."""
    q = query.lower()
    replacements = [
        ("art. ", "article "), ("art ", "article "),
        ("sec. ", "section "), ("sec ", "section "),
        ("bill of rights", "article iii"), ("b or ", "bill of rights "),
        ("muslim personal law", "pd 1083 shariah"), ("code of muslim", "pd 1083"),
        ("shariah civil", "shariah pd 1083 civil law family code distinct"),
        ("lawphil", "lawphil constitution statutes jurisprudence republic acts"),
    ]
    for old, new in replacements:
        q = q.replace(old, new)
    return q


def retrieve(query: str, top_k: int = 5) -> List[dict]:
    """
    Retrieve relevant docs by keyword overlap (content + source).
    Returns list of dicts with 'content' and 'source'.
    """
    q_norm = _normalize_query(query)
    q_words = set(w for w in q_norm.replace(",", " ").replace(".", " ").split() if len(w) > 2)

    scored = []
    for doc in ALL_DOCS:
        content = doc["content"].lower()
        source = doc["source"].lower()
        # Match against both content and source (source has "Article III", "1987 Constitution")
        combined = content + " " + source
        matches = sum(1 for w in q_words if w in combined)
        if matches > 0:
            scored.append((matches, {"content": doc["content"], "source": doc["source"]}))

    scored.sort(key=lambda x: -x[0])
    return [s[1] for s in scored[:top_k]]
