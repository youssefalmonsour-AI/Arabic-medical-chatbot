import re
import numpy as np
import faiss
from sentence_transformers import SentenceTransformer
from config import *

# تنظيف النص العربي
def clean_text(text):
    text = re.sub(r'[\u064b-\u065f]', '', text)  # حذف التشكيل
    text = re.sub(r'[^\u0600-\u06FF\s؟]', '', text)  # حذف الرموز غير العربية
    return text.strip()

# تحميل فهرس FAISS وبيانات الأسئلة
def load_faiss():
    print(" تحميل فهرس FAISS والتضمينات...")
    index = faiss.read_index(FAISS_INDEX_PATH)
    questions = np.load(EMBEDDINGS_PATH, allow_pickle=True)
    return index, questions

# تحميل نموذج SBERT للاسترجاع
def load_retriever():
    print(" تحميل نموذج SBERT للاسترجاع...")
    return SentenceTransformer(RETRIEVER_MODEL)

# استرجاع أقرب سؤال من قاعدة المعرفة
def retrieve(user_question, index, questions, retriever, top_k=1):
    query_embedding = retriever.encode([user_question], convert_to_numpy=True)
    D, I = index.search(np.array(query_embedding).astype("float32"), top_k)
    return questions[I[0][0]]["output"].removeprefix("إجابة:").strip()  # ← تعديل هنا

# الرد باستخدام السؤال المسترجع
def generate_answer(user_question, retrieved_question):
    return f"وفقًا للمعلومة الأقرب: {retrieved_question}"