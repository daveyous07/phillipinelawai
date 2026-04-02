"""
Export the same document list as rag_simple.ALL_DOCS to mobile/assets/rag_index.json
for on-device keyword RAG in the Expo app.

Run from repo root or backend/:
  py -3 scripts/export_mobile_rag.py
"""
from __future__ import annotations

import json
from pathlib import Path

SCRIPT = Path(__file__).resolve()
BACKEND = SCRIPT.parents[1]
MOBILE_ASSETS = BACKEND.parent / "mobile" / "assets"
OUT = MOBILE_ASSETS / "rag_index.json"


def main() -> None:
    import sys

    sys.path.insert(0, str(BACKEND))
    from app.services.rag_simple import ALL_DOCS  # noqa: E402

    payload = [{"content": d["content"], "source": d["source"]} for d in ALL_DOCS]
    MOBILE_ASSETS.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(payload, ensure_ascii=False), encoding="utf-8")
    print(f"Wrote {len(payload)} docs ({OUT.stat().st_size // 1024} KB) -> {OUT}")


if __name__ == "__main__":
    main()
