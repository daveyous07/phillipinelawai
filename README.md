# Philippine Law Assistant — Google Colab (GPU)

[`philippine_law_assistant_colab.ipynb`](philippine_law_assistant_colab.ipynb) runs the same **RAG + law tutor prompt** using **GPU inference** in [Google Colab](https://colab.research.google.com/).

**Open in Colab:**  
[philippine_law_assistant_colab.ipynb](https://colab.research.google.com/github/daveyous07/phillipinelawai/blob/main/philippine_law_assistant_colab.ipynb)

## Backend code (included)

This repo contains **`backend/`** (Python `app/` package with prompts + `rag_simple`). The notebook **clones this repository by default** — no manual upload unless you want a different fork.

## Model

Default Hugging Face model is `Qwen/Qwen2.5-1.5B-Instruct`. Override with env `PHLAW_MODEL_ID` if needed.
