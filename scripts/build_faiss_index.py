from pathlib import Path

BASE_DIR = Path(__file__).resolve().parents[1]
DATA_DIR = BASE_DIR / "data"
EMBEDDINGS_DIR = BASE_DIR / "embeddings"
FAISS_INDEX_PATH = EMBEDDINGS_DIR / "faiss_index.bin"
EMBEDDINGS_NPY_PATH = EMBEDDINGS_DIR / "medical_questions.npy"
CSV_PATH = DATA_DIR / "cleaned_for_generation.csv"
MODEL_NAME = "sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2"


def ensure_dataset_exists():
    if not CSV_PATH.exists():
        raise FileNotFoundError(
            "Dataset file not found. Expected: "
            f"{CSV_PATH}\nPlease prepare the data first or place the CSV file there."
        )


def ensure_embeddings_exist():
    missing = [str(path) for path in (FAISS_INDEX_PATH, EMBEDDINGS_NPY_PATH) if not path.exists()]
    if missing:
        raise FileNotFoundError(
            "FAISS files are missing. Run: python scripts/build_faiss_index.py\n"
            f"Missing: {', '.join(missing)}"
        )
