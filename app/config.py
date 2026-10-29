from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
EMBEDDINGS_DIR = BASE_DIR / "embeddings"
FAISS_INDEX_PATH = EMBEDDINGS_DIR / "faiss_index.bin"
EMBEDDINGS_NPY_PATH = EMBEDDINGS_DIR / "medical_questions.npy"
RETRIEVER_MODEL = "sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2"
LOG_FILE = BASE_DIR / "conversations.json"


def ensure_data_files():
    missing = [str(path) for path in (FAISS_INDEX_PATH, EMBEDDINGS_NPY_PATH) if not path.exists()]
    if missing:
        raise FileNotFoundError(
            "Missing embedding files. Please generate them first by running: "
            "python scripts/build_faiss_index.py\n"
            f"Missing: {', '.join(missing)}"
        )
