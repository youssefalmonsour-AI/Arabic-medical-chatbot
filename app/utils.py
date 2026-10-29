import re

import numpy as np
import faiss
from sentence_transformers import SentenceTransformer

from app.config import (
    EMBEDDINGS_NPY_PATH,
    FAISS_INDEX_PATH,
    RETRIEVER_MODEL,
    ensure_data_files,
)


def clean_text(text):
    if text is None:
        return ""
    text = re.sub(r'[\u064b-\u065f]', '', text)
    text = re.sub(r'[^\u0600-\u06FF\s؟]', '', text)
    return text.strip()


def load_faiss():
    ensure_data_files()
    print("تحميل فهرس FAISS والتضمينات...")
    index = faiss.read_index(str(FAISS_INDEX_PATH))
    questions = np.load(str(EMBEDDINGS_NPY_PATH), allow_pickle=True)
    return index, questions


def load_retriever():
    print("تحميل نموذج SBERT للاسترجاع...")
    return SentenceTransformer(RETRIEVER_MODEL)


def retrieve(user_question, index, questions, retriever, top_k=1):
    if not user_question:
        return ""

    query_embedding = retriever.encode([user_question], convert_to_numpy=True)
    if query_embedding.ndim == 1:
        query_embedding = np.array([query_embedding], dtype="float32")
    else:
        query_embedding = np.asarray(query_embedding, dtype="float32")

    _, indices = index.search(query_embedding, top_k)
    idx = int(indices[0][0])
    matched = questions[idx]
    answer = matched.get("output", "") if isinstance(matched, dict) else str(matched)
    if answer.startswith("إجابة:"):
        answer = answer[len("إجابة:"):]
    return answer.strip()


def generate_answer(user_question, retrieved_question):
    return f"وفقًا للمعلومة الأقرب: {retrieved_question}"
