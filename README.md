# Philippine Law Assistant — Google Colab (GPU)

[`philippine_law_assistant_colab.ipynb`](philippine_law_assistant_colab.ipynb) runs the same **RAG + law tutor prompt** as the project backend using **GPU inference** in [Google Colab](https://colab.research.google.com/).

**Open in Colab (while signed in as your Google account, e.g. daveyous07@gmail.com):**  
[Open `philippine_law_assistant_colab.ipynb` in Colab](https://colab.research.google.com/github/daveyous07/phillipinelawai/blob/main/philippine_law_assistant_colab.ipynb)

You can also upload the `.ipynb` via *File → Upload notebook* in Colab.

## Backend code (required)

The notebook imports `app.prompts` and `app.services.rag_simple` from **`philippine-law-assistant/backend/`**. This repository only stores the notebook. Use one of:

1. **Environment variable** — set `PHLAW_REPO_URL` to a git URL whose tree includes `philippine-law-assistant/backend/` (e.g. your monorepo root), then run the clone cell.
2. **Manual upload** — zip your local `philippine-law-assistant` folder, upload to Colab, unzip under `/content/`, and set `BACKEND_ROOT` as described in the notebook.

## Model

Default Hugging Face model is `Qwen/Qwen2.5-1.5B-Instruct`. Override with env `PHLAW_MODEL_ID` if needed.
